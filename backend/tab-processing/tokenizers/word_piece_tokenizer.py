from tokenizers import Tokenizer, models, pre_tokenizers
from tokenizers.trainers import WordPieceTrainer
from pathlib import Path
from tokenizers.pre_tokenizers import Sequence, Whitespace, Punctuation

# Collect processed token files
token_files_dir = Path("./examples")
paths = [str(x) for x in token_files_dir.glob("**/*processed.txt")]

print(f"Found {len(paths)} token file(s) for training.")

# Initialize a WordPiece tokenizer
tokenizer = Tokenizer(models.WordPiece(unk_token="[UNK]"))
# Split on whitespace so each token line is one subword candidate
tokenizer.pre_tokenizer = Sequence([
    Whitespace(),
    Punctuation()   # splits off “:”, “,”, etc., before BPE/WordPiece merges
])

# Configure the WordPiece trainer
trainer = WordPieceTrainer(
    vocab_size=52000,
    min_frequency=1,
    special_tokens=[
        "[UNK]",     # for OOV tokens
        "rest",
        "wait",
        "note",
        "bfs",
        "nfx"
    ]
)

# Train the tokenizer
tokenizer.train(files=paths, trainer=trainer)

# Save the trained vocab
output_dir = Path("./vocabs")
output_dir.mkdir(exist_ok=True)
tokenizer.save(str(output_dir / "word_piece_vocab.json"))

