# DadaGP

[**Paper**](https://archives.ismir.net/ismir2021/paper/000076.pdf) | [**Generation Results**](https://drive.google.com/drive/folders/1USNH8olG9uy6vodslM3iXInBT725zult?usp=sharing) | [**ISMIR Poster**](https://s3.eu-west-1.amazonaws.com/production-main-contentbucket52d4b12c-1x4mwd6yn8qjn/8ed232c2-bcce-46aa-a735-d24b865644ef.pdf) 

DadaGP is:

* a dataset of 26,181 GuitarPro songs in 739 genres, converted to a token sequence format suitable for generative language models like GPT2, TransformerXL, etc.
* an encoder/decoder (v1.1) that converts gp3, gp4, gp5 files to/from this token format.

#### ENCODE (guitar pro --> tokens)
```
python simplified_dadagp.py encode examples/input.gp3 output.txt [artist_name]
```

#### DECODE (tokens --> guitar pro)
```
python simplified_dadagp.py decode examples/input.txt output.gp5
```