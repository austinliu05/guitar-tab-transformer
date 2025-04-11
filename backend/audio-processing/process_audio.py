import librosa
from tqdm import tqdm
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import torch

# Play audio function
def play_audio(y, sr):
    sd.play(y, sr)
    sd.wait()  # Wait until audio playback is finished

# Analyze audio and extract features
def analyze_audio(file_path):
    y, sr = librosa.load(file_path, sr=None)
    
    features = {}
    with tqdm(total=2, desc="Extracting features") as pbar:
        features['duration'] = librosa.get_duration(y=y, sr=sr)
        pbar.update(1)
        
        spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
        features['spectral_centroid'] = spectral_centroid.mean()
        pbar.update(1)
    
    return y, sr, features

# Harmonic-Percussive Separation (HPSS)
def harmonic_percussive_separation(y, sr):
    y_harmonic, y_percussive = librosa.effects.hpss(y)
    
    plt.figure(figsize=(12, 6))
    plt.subplot(3, 1, 1)
    librosa.display.waveshow(y, sr=sr)
    plt.title("Original Audio")

    plt.subplot(3, 1, 2)
    librosa.display.waveshow(y_harmonic, sr=sr)
    plt.title("Harmonic (Vocals, Melody)")

    plt.subplot(3, 1, 3)
    librosa.display.waveshow(y_percussive, sr=sr)
    plt.title("Percussive (Drums, Rhythm)")

    plt.tight_layout()
    plt.show()
    
    return y_harmonic, y_percussive

# Extract notes in sequence
def extract_notes_in_sequence(y, sr):
    spectrogram = librosa.stft(y)
    spectrogram_db = librosa.amplitude_to_db(np.abs(spectrogram), ref=np.max)
    
    prominent_freq = np.argmax(np.abs(spectrogram), axis=0)  
    prominent_freq_hz = prominent_freq * (sr / spectrogram.shape[0])
    prominent_freq_hz = np.nan_to_num(prominent_freq_hz, nan=0.0, posinf=0.0, neginf=0.0)
    prominent_freq_hz = np.clip(prominent_freq_hz, 20, 20000)
    
    notes_sequence = librosa.hz_to_note(prominent_freq_hz)
    
    frame_times = librosa.frames_to_time(np.arange(len(prominent_freq_hz)), sr=sr)
    durations = np.diff(frame_times, append=frame_times[-1])

    return notes_sequence, prominent_freq_hz, durations

# Convert audio and features to PyTorch tensors
def audio_to_tensor(y, sr, features):
    # Convert waveform to tensor
    y_tensor = torch.tensor(y, dtype=torch.float32)
    
    # Spectrogram conversion
    spectrogram = librosa.feature.melspectrogram(y=y, sr=sr, n_fft=2048, hop_length=512, n_mels=128)
    spectrogram_db = librosa.power_to_db(spectrogram, ref=np.max)
    spectrogram_tensor = torch.tensor(spectrogram_db, dtype=torch.float32)
    
    # Feature tensor
    feature_tensor = torch.tensor([features['duration'], features['spectral_centroid']], dtype=torch.float32)
    
    return y_tensor, spectrogram_tensor, feature_tensor

# Main execution
if __name__ == "__main__":
    file_path = "mp3-files/sample-test-1.mp3"
    
    y, sr, result = analyze_audio(file_path)
    print(f"Duration: {result['duration']} seconds")
    print(f"Spectral Centroid (mean): {result['spectral_centroid']:.2f}")
    
    y_harmonic, y_percussive = harmonic_percussive_separation(y, sr)
    
    notes_sequence, freq_sequence, durations = extract_notes_in_sequence(y_harmonic, sr)
    
    print("Sequential Notes (in order of appearance):")
    for note, dur in zip(notes_sequence, durations):
        print(f"{note}: {dur:.2f} sec")
    
    print("Playing harmonic (melodic) part...")
    play_audio(y_harmonic, sr)
    
    # Convert to tensors
    y_tensor, spectrogram_tensor, feature_tensor = audio_to_tensor(y, sr, result)
    print("Tensor shapes:")
    print(f"Waveform Tensor: {y_tensor.shape}")
    print(f"Spectrogram Tensor: {spectrogram_tensor.shape}")
    print(f"Feature Tensor: {feature_tensor.shape}")
