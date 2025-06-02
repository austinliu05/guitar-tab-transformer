import re
from typing import List, Dict, Tuple, Union
import os

def is_instrumental(token: str) -> bool:
    return token.startswith("note:")

def strip_non_instrumental(tokens: List[str]) -> Tuple[List[str], Dict[int, str]]:
    """
    Returns:
      - pure_tokens:    [ all tokens t where is_instrumental(t) is True ]
      - removed_map:    { original_index: removed_token } for each token
                        where is_instrumental(token) is False.
    """
    pure_tokens: List[str] = []
    removed_map: Dict[int, str] = {}
    
    for idx, tok in enumerate(tokens):
        if is_instrumental(tok):
            pure_tokens.append(tok)
        else:
            removed_map[idx] = tok
    return pure_tokens, removed_map

def restore_non_instrumental(pure_tokens: List[str], removed_map: Dict[int, str]) -> List[str]:
    """
    Rebuilds a full token list.

    - Places each removed_map[idx] at index `idx`.
    - Fills the remaining None slots (in ascending index order) with the
        items from pure_tokens, in order.
    """
    total_length = len(pure_tokens) + len(removed_map)
    reconstructed = [None] * total_length  
    
    for idx, tok in removed_map.items():
        reconstructed[idx] = tok

    i_pure = 0
    for i in range(total_length):
        if reconstructed[i] is None:
            reconstructed[i] = pure_tokens[i_pure]
            i_pure += 1

    return reconstructed

def sort_notes(pruned_notes: List[str]):
    # Define a key function for sorting based on "s<number>:" in the token.
    def extract_s_number(s):
        match = re.search(r's(\d+):', s)
        # If not found, push token to the end.
        return int(match.group(1)) if match else float('inf')
    sorted_notes = sorted(pruned_notes, key=extract_s_number)
    return sorted_notes

def merge_tracks_and_prune(notes: List[str]):
    processed_notes = []
    has_rest = False 
    
    for token in notes:
        # Remove any track prefix ("clean0:" or "clean1:" etc).
        cleaned_token = re.sub(r"clean\d+:", "", token)
        
        if cleaned_token == "rest":
            # If we haven't already added a rest token for this group, add it.
            if not has_rest:
                processed_notes.append("rest")
                has_rest = True
        else:
            processed_notes.append(cleaned_token)
    
    return sort_notes(processed_notes)

def expand_repeats(tokens: List[str]) -> List[str]:
    """
    Scan through tokens. Whenever "measure:repeat_open" is found, collect everything
    up to the matching "measure:repeat_close:<count>" and repeat those inner tokens <count> times.
    Drop the measure markers themselves.
    """
    expanded = []
    i = 0
    n = len(tokens)

    while i < n:
        token = tokens[i]
        if token.startswith("measure:repeat_open"):
            j = i + 1
            while j < n and not tokens[j].startswith("measure:repeat_close"):
                j += 1
            if j >= n:
                expanded.append(token)
                i += 1
                continue

            # Extract repeat count from "measure:repeat_close:<count>"
            repeat_close_token = tokens[j]
            m = re.match(r"measure:repeat_close:(\d+)", repeat_close_token)
            if not m:
                expanded.append(token)
                i += 1
                continue

            count = int(m.group(1))
            inner_tokens = tokens[i+1:j]

            for _ in range(count):
                expanded.extend(inner_tokens)

            i = j + 1
        else:
            # Not a repeat marker, keep as-is
            expanded.append(token)
            i += 1

    return expanded

def process_raw_acoustic_solo_tokens(tokens: Union[str, List[str]]):
    if isinstance(tokens, str):
        try:
            with open(tokens, 'r') as f:
                tokens = [t.strip() for t in f.readlines() if t.strip()]
        except FileNotFoundError:
            raise ValueError("Please provide either encoded tokens or the path to the token file")
    
    # Split tokens into header, body, and footer.
    header = []
    body = []
    footer = []
    in_body = False

    for token in tokens:
        if token == "start":
            in_body = True
            header.append(token)
        elif token == "end":
            in_body = False
            footer.append(token)
        elif in_body:
            body.append(token)
        else:
            # Tokens before "start" go to header; tokens after "end" go to footer.
            if not in_body:
                header.append(token)
            else:
                footer.append(token)
    
    expanded_body = expand_repeats(body)

    # Process body tokens by grouping consecutive 'clean' tokens,
    processed_body = []
    current_group = []

    prefixes = ("note", "bfs", "nfx", "wait")
    for token in expanded_body:
        # Group any 'clean' tracks
        if token.startswith("clean"):
            current_group.append(token)
            continue

        # Skip tokens that don't start with one of the desired prefixes
        if not token.startswith(prefixes):
            continue

        if current_group:
            merged = merge_tracks_and_prune(current_group)
            processed_body.extend(merged)
            current_group = []

        processed_body.append(token)
    
    if current_group:
        merged = merge_tracks_and_prune(current_group)
        processed_body.extend(merged)
    
    return processed_body


def main():
    examples_folder = "examples"

    # Clean up any previously processed files
    for fname in os.listdir(examples_folder):
        if "processed" in fname:
            path = os.path.join(examples_folder, fname)
            if os.path.isfile(path):
                os.remove(path)

    if not os.path.isdir(examples_folder):
        print(f"The folder '{examples_folder}' does not exist.")
        return

    for filename in os.listdir(examples_folder):
        if not filename.endswith(".txt"):
            continue

        filepath = os.path.join(examples_folder, filename)
        if not os.path.isfile(filepath):
            continue

        print(f"\nProcessing file: {filename}")
        try:
            # Get a “fully processed” list:
            processed_tokens: List[str] = process_raw_acoustic_solo_tokens(filepath)

            # Strip out all non‐instrumental tokens
            pure_tokens, removed_map = strip_non_instrumental(processed_tokens)
            base_name, ext = os.path.splitext(filename)
            predicted_pure = pure_tokens.copy()

            # Re‐insert the non‐instrumental tokens in exactly the same spots:
            reconstructed = restore_non_instrumental(predicted_pure, removed_map)

            base_name, ext = os.path.splitext(filename)
            processed_filename = f"{base_name}_processed{ext}"
            with open(os.path.join(examples_folder, processed_filename), "w") as f_proc:
                f_proc.write("\n".join(processed_tokens))
            print(f"  → Fully processed tokens saved to: {processed_filename}")

            reconstructed_filename = f"{base_name}_reconstructed{ext}"
            with open(os.path.join(examples_folder, reconstructed_filename), "w") as f_recon:
                f_recon.write("\n".join(reconstructed))
            print(f"  → Reconstructed tokens saved to: {reconstructed_filename}")

        except Exception as e:
            print(f"An error occurred while processing {filename}: {e}")

if __name__ == "__main__":
    main()