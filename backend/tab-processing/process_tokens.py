import re
from typing import List, Union
import os

def sort_notes(pruned_notes: List[str]):
    # Define a key function for sorting based on "s<number>:" in the token.
    def extract_s_number(s):
        match = re.search(r's(\d+):', s)
        # If not found, push token to the end.
        return int(match.group(1)) if match else float('inf')
    # Return the list sorted by the extracted number.
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

def process_raw_acoustic_solo_tokens(tokens: Union[str, List[str]]):
    if isinstance(tokens, str):
        try:
            with open(tokens, 'r') as f:
                tokens = [t.strip() for t in f.readlines() if t.strip()]
        except FileNotFoundError:
            raise ValueError("Please provide either encoded tokens or the path to the token file")
    
    # Split tokens into header, body, and footer.
    # (Assuming the file contains "start" and "end" markers.)
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
    
    # Process body tokens by grouping consecutive tokens that start with "clean"
    processed_body = []
    current_group = []

    for token in body:
        if token.startswith("clean"):
            current_group.append(token)
        else:
            if current_group:
                merged = merge_tracks_and_prune(current_group)
                processed_body.extend(merged)
                current_group = []
            processed_body.append(token)
    
    if current_group:
        merged = merge_tracks_and_prune(current_group)
        processed_body.extend(merged)
    
    # Reassemble header, processed body, and footer.
    return header + processed_body + footer

def main():
    examples_folder = "examples"
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
