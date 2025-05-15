from tokenizers import Tokenizer, models
from tokenizers.trainers import WordPieceTrainer
from tokenizers.pre_tokenizers import Sequence, Split, Whitespace
from pathlib import Path
import re
import argparse
from tokenizers import ByteLevelBPETokenizer
import json

def train_wordpiece(paths, output_dir):
    tokenizer = Tokenizer(models.WordPiece(unk_token="[UNK]"))
    tokenizer.pre_tokenizer = Sequence([
        Split(pattern=":", behavior="isolated"),
        Whitespace()
    ])
    trainer = WordPieceTrainer(
        vocab_size=1000,
        min_frequency=2,
        special_tokens=["[UNK]", "rest", "wait", "note", "bfs", "nfx"]
    )

    tokenizer.train(files=paths, trainer=trainer)
    tokenizer.save(str(output_dir / "wordpiece_vocab.json"))
    print("WordPiece vocab saved to", output_dir / "wordpiece_vocab.json")

def train_bpe(paths, output_dir):
    bpe = ByteLevelBPETokenizer()
    bpe.train(
        files=paths,
        vocab_size=1000,
        min_frequency=2,
        special_tokens=["[UNK]", "rest", "wait", "note", "bfs", "nfx"]
    )
    bpe.save_model(str(output_dir), prefix="bpe")
    print("BPE vocab + merges saved to", output_dir)
    
    vocab_path = Path("vocabs/bpe-vocab.json")

    # 1) Load the raw (unsorted) token → ID mapping
    with open(vocab_path, 'r', encoding='utf-8') as f:
        vocab = json.load(f)

    # 2) Sort by ID (the values)
    sorted_vocab = dict(sorted(vocab.items(), key=lambda kv: kv[1]))

    # 3) Write out the sorted mapping
    output_path = vocab_path.parent / "full_bpe_vocab.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(sorted_vocab, f, indent=2, ensure_ascii=False)

    print(f"Saved complete BPE vocab (sorted) to: {output_path}")
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--tokenizer", choices=["wordpiece", "bpe"], required=True,
        help="Which tokenizer to train"
    )
    args = parser.parse_args()
    token_files_dir = Path("../examples")
    paths = [str(x) for x in token_files_dir.glob("**/*processed.txt")]
    output_dir = Path("./vocabs")
    output_dir.mkdir(exist_ok=True)

    # Pretokenization
    def pre_tokenize(line):
        tokens = []
        for segment in line.split():  # Whitespace splitting
            parts = re.split(r'(:)', segment)  # Isolate ":" as its own token
            tokens.extend([p for p in parts if p])  # Remove empty strings
        return tokens

    # Example lines
    examples = [
        "note:s2:f4:B4",
        "wait:480",
        "nfx:hammer",
        "nfx:harmonic:4",
        "note:s1:f9:E5 rest"
    ]
    for line in examples:
        print(f"{line!r} → {pre_tokenize(line)}")
    
    if args.tokenizer == "wordpiece":
        train_wordpiece(paths, output_dir)
    else:
        train_bpe(paths, output_dir)
        
if __name__ == "__main__":
    main()