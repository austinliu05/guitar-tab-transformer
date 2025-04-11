import collections
import json
import os
from dataclasses import dataclass
from typing import List, Union

from transformers.models.bert.tokenization_bert import load_vocab, whitespace_tokenize, WordpieceTokenizer
from transformers.tokenization_utils import PreTrainedTokenizer
from transformers.utils import ModelOutput

# @dataclass
# class GttTokenizerOutput():

def raw_tokens_to_text(tokens: Union[List[str], str]) -> str:
    if isinstance(tokens, str):
        if not os.path.exists(tokens):
            raise ValueError(f"File {tokens} does not exist.")
        else:
            with open(tokens, "r") as f:
                tokens = [t.strip() for t in f.readlines()]

    return " ".join(tokens)


class GttTokenizer(PreTrainedTokenizer):
    def __init__(
        self,
        vocab_file,
        unk_token="[UNK]",
        rsep_token="[RSEP]",
        msep_token ="[MSEP]",
        cls_token="[CLS]",
        pad_token="<pad>",
        mask_token="[MASK]",
        **kwargs
    ):
        if not os.path.isfile(vocab_file):
            raise ValueError(
                f"Can't find a vocabulary file at path '{vocab_file}'. To load the vocabulary from a Google pretrained"
                " model use `tokenizer = BertTokenizer.from_pretrained(PRETRAINED_MODEL_NAME)`"
            )
        self.vocab = load_vocab(vocab_file)
        self.ids_to_tokens = collections.OrderedDict(
            [(ids, tok) for tok, ids in self.vocab.items()]
        )

        self.wordpiece_tokenizer = WordpieceTokenizer(vocab=self.vocab, unk_token=str(unk_token))
        super().__init__(
            unk_token=unk_token,
            rsep_token=rsep_token,
            msep_token=msep_token,
            pad_token=pad_token,
            cls_token=cls_token,
            mask_token=mask_token,
            **kwargs
        )

    @property
    def vocab_size(self):
        return len(self.vocab)

    def _tokenize(self, text, split_special_tokens=False):
        split_tokens = []
        if self.do_basic_tokenize:
            for token in self.basic_tokenizer.tokenize(
                text, never_split=self.all_special_tokens if not split_special_tokens else None
            ):
                # If the token is part of the never_split set
                if token in self.basic_tokenizer.never_split:
                    split_tokens.append(token)
                else:
                    split_tokens += self.wordpiece_tokenizer.tokenize(token)
        else:
            split_tokens = self.wordpiece_tokenizer.tokenize(text)
        return split_tokens
