from typing import Union, List
import os

def raw_tokens_to_text(tokens: Union[List[str], str]) -> str:
    if isinstance(tokens, str):
        if not os.path.exists(tokens):
            raise ValueError(f"File {tokens} does not exist.")
        else:
            with open(tokens, "r") as f:
                tokens = [t.strip() for t in f.readlines()]

    return " ".join(tokens)