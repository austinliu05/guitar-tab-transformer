# Guitar Tab Transformer (GTT)

Guitar Tab Transformer (GTT) is a passion project aiming to automatically transcribe any song—given its audio file—into guitar tablature. By leveraging neural networks and custom tokenization, GTT seeks to align raw audio waveforms with guitar-friendly notation, bridging the gap between a recorded performance and readable guitar tabs.

## Repository Structure

- **gtt-model**  
  Transformer-based sequence model that takes tokenized inputs and generates corresponding guitar tab tokens.  
  [repo](https://github.com/austinliu05/gtt-model)

- **acoustic-solo-dadaGP**  
  Modified open source `dadaGP` package, tailoring it to handle only acoustic fingerstyle guitar.  
  [repo](https://github.com/austinliu05/acoustic-solo-dadaGP)
