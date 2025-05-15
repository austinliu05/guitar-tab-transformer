from tokenizers import Tokenizer, models
from tokenizers.trainers import WordPieceTrainer
from tokenizers.pre_tokenizers import Sequence, Split, Whitespace
from pathlib import Path

# 1) Gather your processed files
token_files_dir = Path("./examples")
paths = [str(x) for x in token_files_dir.glob("**/*processed.txt")]

# 2) Initialize WordPiece
tokenizer = Tokenizer(models.WordPiece(unk_token="[UNK]"))

# 3) Pre-tokenize: first break out “:”, then split on whitespace
tokenizer.pre_tokenizer = Sequence([
    Split(pattern=":", behavior="isolated"),
    Whitespace()
])

# 4) Trainer
trainer = WordPieceTrainer(
    vocab_size=52000,
    min_frequency=1,
    special_tokens=["[UNK]", "rest", "wait", "note", "bfs", "nfx"]
)

# 5) Train & inspect
tokenizer.train(files=paths, trainer=trainer)
full_vocab = tokenizer.get_vocab()
print("New vocab size:", len(full_vocab))
for tok, idx in list(full_vocab.items())[:20]:
    print(idx, tok)

# 6) Save
output_dir = Path("./vocabs")
output_dir.mkdir(exist_ok=True)
tokenizer.save(str(output_dir / "word_piece_vocab.json"))
