"""
TODO

1. Figure out if the tokens contain more than 1 track
2. Merge track by:

"""

import re
from typing import List, Union

def sort_notes(pruned_notes: List[str]):
    # Define a key function for sorting
    def extract_s_number(s):
        match = re.search(r's(\d+):', s)
        # return int(match.group(1)) if match else float('inf')  # fallback to inf if no match
        return int(match.group(1))
    # Sort the list
    sorted_notes = sorted(pruned_notes, key=extract_s_number)
    return sorted_notes

def merge_tracks_and_prune(notes: List[str]):
    processed_notes = []
    for token in notes:
        if token.startswith("clean0"):
            processed_notes.append(token.replace("clean0:", ""))
        else:
            if token.endswith("rest"):
                continue
            else:
                processed_notes.append(re.sub(r"clean\d+:", "", token))

    return sort_notes(processed_notes)


def process_raw_acoustic_solo_tokens(tokens: Union[str, List[str]]):

    if isinstance(tokens, str):
        try:
            with open(tokens, 'r') as f:
                tokens = [t.strip() for t in f.readlines()]
        except FileNotFoundError:
            raise ValueError("Please provide either encoded tokens or the path to the token file")

    start = 0
    end = 0

    result = []

    for i, t in enumerate(tokens):
        if "clean" in t:
            if end + 1 == i:
                end = i
            else:
                start = i
                end = i
        else:

            if end +1 == i:
                notes = tokens[start: i]
                processed_notes = merge_tracks_and_prune(notes)
                result.extend(processed_notes)

            result.append(t)

    if end == len(tokens) - 1 and "clean" in tokens[end]:
        notes = tokens[start:]
        processed_notes = merge_tracks_and_prune(notes)
        result.extend(processed_notes)

    return result
