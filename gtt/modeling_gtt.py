from dataclasses import dataclass
from transformers.utils import ModelOutput
from typing import Tuple, Optional
import torch

@dataclass
class GTTOutput(ModelOutput):
    """
    Based on seamless_m4t.SeamlessM4Tv2GenerationOutput

    Class defining the generated outputs from [`SeamlessM4TModel`], [`SeamlessM4TForTextToText`],
    [`SeamlessM4TForTextToSpeech`], [`SeamlessM4TForSpeechToSpeech`] and [`SeamlessM4TForTextToSpeech`].

    Args:
        sequences (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
            The generated translated sequences. This is the output of the text-to-text or the speech-to-text models.
            The second dimension (sequence_length) is either equal to `max_length` or shorter if all batches finished
            early due to the `eos_token_id`.
        unit_sequences (`torch.LongTensor` of shape `(batch_size, unit_sequence_length)`, *optional*):
            The generated translated unit sequences. This is the output of the text-to-units model. The second
            dimension (unit_sequence_length) is either equal to `t2u_max_length` or shorter if all batches finished
            early due to the `t2u_eos_token_id`.
    """

    sequences: Optional[Tuple[torch.FloatTensor]] = None
    unit_sequences: Optional[Tuple[torch.FloatTensor]] = None