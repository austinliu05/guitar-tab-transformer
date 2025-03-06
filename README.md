# 🎸 Guitar Tab Transformer  

A tool for converting **Guitar Pro files (.gp5)** into a **tokenized** format and vice versa. Also includes audio processing utilities for isolating vocals.

---

## Features
- **Encode & Decode Guitar Pro Files** – Convert `.gp5` files into tokens and back.
- **Support for Clean Guitar Tabs** – Works exclusively with clean guitar tracks.
- **Audio Separation with Demucs** – Extract vocals from a song.

---

## Setup & Installation

### **1️⃣ Install Dependencies**
Ensure you have Python and required libraries installed:

```bash
pip install -r requirements.txt
```

### **2️⃣ Install Demucs for Audio Separation**
```bash
pip install demucs
```

---

## 🎵 Audio Separation with Demucs
To extract vocals from an audio file:
```bash
demucs --two-stems=vocals mp3-files/sample-test-1.mp3
```

---

## 🎼 Encoding & Decoding Guitar Pro Files

### **🔹 Encode a Guitar Pro (.gp5) file into tokens**
This is the original dada.py file
```bash
python dadagp.py encode examples/ed_sheeran-supermarket_flowers.gp5 examples/ed_sheeran-supermarket_flowers.txt ed-sheeran
```
This is the simpolified version, simpified for GTT purposes.
```bash
python simplified_dadagp.py encode examples/ed_sheeran-supermarket_flowers.gp5 examples/ed_sheeran-supermarket_flowers.txt ed-sheeran
```

### **🔹 Decode a tokenized file back into a Guitar Pro (.gp5) file**
```bash
python dadagp.py decode examples/ed_sheeran-supermarket_flowers.txt examples/ed_sheeran-supermarket_flowers_decoded.gp5
```

---

## 🎸 Useful Links
- **[Download Guitar Pro Files](https://gtptabs.com/)** – Find `.gp5` files for testing.
- **[Supermarket Flowers (Audio)](https://www.youtube.com/watch?v=XEZJEaPEaVQ)** – Song reference.
- **[Supermarket Flowers (Tab)](https://flat.io/score/6799c4e23a886d4545faadf8-supermarket-flowers?sharingKey=4ab4c45c53859d172998d7cacc4d619f4cae7e6634c74291b555c631953d08edd8a9ffe896ac82b2d8807bb44885cbf34d3221a3944303f27a6db986e35ea131)** – Guitar tab reference.

---

## ⚡ Testing & Debugging
To verify functionality, run:
```bash
python dadagp.py encode examples/test_file.gp5 examples/test_file.txt test-artist
python dadagp.py decode examples/test_file.txt examples/test_file_decoded.gp5
```
Ensure the decoded `.gp5` matches the original file.

---

## 📌 Notes
- **Only supports clean guitar tracks**.
- **Drums, bass, and other instruments are not included**.
- **Instrument changes within a song are not supported**.

---

## 🎯 Future Improvements
- Add support for additional guitar tunings.
- Implement better handling for rhythm variations.
- Improve AI-based tab transcriptions from audio.