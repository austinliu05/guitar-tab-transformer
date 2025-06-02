import re
from typing import List, Union
import os

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
    # Clean up previously processed files
    for fname in os.listdir(examples_folder):
        if "processed" in fname:
            path = os.path.join(examples_folder, fname)
            if os.path.isfile(path):
                os.remove(path)

    if not os.path.isdir(examples_folder):
        print(f"The folder '{examples_folder}' does not exist.")
        return

    # Process only .txt files in the examples folder.
    for filename in os.listdir(examples_folder):
        if filename.endswith(".txt"):
            filepath = os.path.join(examples_folder, filename)
            if os.path.isfile(filepath):
                print(f"\nProcessing file: {filename}")
                try:
                    processed_tokens = process_raw_acoustic_solo_tokens(filepath)
                    
                    # Create a new filename by appending "_processed" to the original name.
                    name, ext = os.path.splitext(filename)
                    new_filename = f"{name}_processed{ext}"
                    new_filepath = os.path.join(examples_folder, new_filename)
                    
                    with open(new_filepath, 'w') as outfile:
                        outfile.write("\n".join(processed_tokens))
                    
                    print(f"Processed tokens saved to: {new_filename}")
                except Exception as e:
                    print(f"An error occurred while processing {filename}: {e}")

if __name__ == "__main__":
    main()
