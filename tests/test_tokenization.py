import pytest
import os

from gtt.tokenization_gtt import GttTokenizer
from gtt.processing_gtt import raw_tokens_to_text


DATA_FOLDER_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tests", "data"
)

def test_folder():
    print(DATA_FOLDER_PATH)

def test_tokenizer():
    tokenizer = GttTokenizer(os.path.join(DATA_FOLDER_PATH, "vocab.txt"))
    tokens_str = raw_tokens_to_text(os.path.join(DATA_FOLDER_PATH, "short_gp_tokens.txt"))
    results = tokenizer._tokenize(tokens_str)
    print(results)