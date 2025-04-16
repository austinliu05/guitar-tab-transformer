from tokenizers import ByteLevelBPETokenizer
from pathlib import Path

token_files_dir = Path("./examples")

paths = [str(x) for x in token_files_dir.glob("**/*.txt")]

print(f"Found {len(paths)} token file(s) for training.")

# Initialize the tokenizer (we're using ByteLevelBPETokenizer for fine-grained tokenization)
tokenizer = ByteLevelBPETokenizer()

# Train the tokenizer
tokenizer.train(
    files=paths,
    vocab_size=52000,
    min_frequency=2,
    special_tokens=[
        "start",   # marks the beginning of the token sequence in your file
        "end",     # marks the end
        "new_measure",  # indicates a new measure/bar in the music
        "rest",     # used for rests; reserving it avoids duplications from overlapping tracks
        "note",
        "nfx"
    ]
)

output_dir = Path("./vocabs")
output_dir.mkdir(exist_ok=True)

tokenizer.save_model(str(output_dir), "vocab")

print(
    f"Tokenizer training complete. Vocabulary and merges saved to: {output_dir}")
