from tokenizers import ByteLevelBPETokenizer
from pathlib import Path

# 1) Gather your processed files
token_files_dir = Path("./examples")
paths = [str(x) for x in token_files_dir.glob("**/*processed.txt")]

print(f"Found {len(paths)} token file(s) for training.")

# 2) Instantiate Byte-Level BPE
tokenizer = ByteLevelBPETokenizer()

# 3) Train on your files
tokenizer.train(
    files=paths,
    vocab_size=52000,
    min_frequency=1,
    special_tokens=[
        "[UNK]", "rest", "wait", "note", "bfs", "nfx"
    ]
)

# 4) Save both vocab.json and merges.txt
output_dir = Path("./vocabs")
output_dir.mkdir(exist_ok=True)
tokenizer.save_model(str(output_dir), prefix="bpe")

print("BPE vocab + merges saved to:", output_dir)
