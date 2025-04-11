from tokenizers import ByteLevelBPETokenizer
from pathlib import Path

# Define paths to your text files
paths = [str(x) for x in Path("../examples").glob("**/*.txt")]

# Initialize the tokenizer
tokenizer = ByteLevelBPETokenizer()

# Train the tokenizer
tokenizer.train(files=paths, vocab_size=52000, min_frequency=2, special_tokens=[
    "<s>", "<pad>", "</s>", "<unk>", "<mask>"
])

# Save the vocab.json and merges.txt files
tokenizer.save_model("output_directory", "tokenizer_name")
