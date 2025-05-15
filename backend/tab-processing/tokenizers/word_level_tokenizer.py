from tokenizers import Tokenizer, models, pre_tokenizers, trainers
from pathlib import Path

# Locating processed token files
token_files_dir = Path("../examples")
paths = [str(x) for x in token_files_dir.glob("**/*processed.txt")]

# Initialize a WordLevel tokenizer
tokenizer = Tokenizer(models.WordLevel(unk_token="[UNK]"))
# Split on whitespace so each token line is treated as a “word”
tokenizer.pre_tokenizer = pre_tokenizers.Whitespace()

# Configure the trainer
trainer = trainers.WordLevelTrainer(
    vocab_size=52000,
    min_frequency=2,
    special_tokens=[
        "[UNK]",      # required for OOV tokens
        "rest",
        "wait",
        "note",
        "bfs",
        "nfx"
    ]
)

# Training
tokenizer.train(files=paths, trainer=trainer)

# Save vocab.json
output_dir = Path("./vocabs")
output_dir.mkdir(exist_ok=True)
tokenizer.save(str(output_dir / "word_level_vocab.json"))
