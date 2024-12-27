import librosa
from tqdm import tqdm
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

def play_audio(y, sr):
    sd.play(y, sr)
    sd.wait()  # Wait until audio playback is finished

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
    
def harmonic_percussive_separation(y):
    # Perform HPSS
    y_harmonic, y_percussive = librosa.effects.hpss(y)
    
    # Plot waveforms for visualization
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

def extract_notes_in_sequence(y, sr):
    # Compute spectrogram
    spectrogram = librosa.stft(y)
    spectrogram_db = librosa.amplitude_to_db(np.abs(spectrogram), ref=np.max)
    
    # Identify prominent frequencies at each time frame
    prominent_freq = np.argmax(np.abs(spectrogram), axis=0)  
    prominent_freq_hz = prominent_freq * (sr / spectrogram.shape[0])
    
    # Replace invalid frequencies
    prominent_freq_hz = np.nan_to_num(prominent_freq_hz, nan=0.0, posinf=0.0, neginf=0.0)
    
    # Clip frequencies to audible range (20 Hz to 20,000 Hz)
    prominent_freq_hz = np.clip(prominent_freq_hz, 20, 20000)
    
    # Convert frequencies to notes in sequence
    notes_sequence = librosa.hz_to_note(prominent_freq_hz)
    
    # Calculate time per frame and durations
    frame_times = librosa.frames_to_time(np.arange(len(prominent_freq_hz)), sr=sr)
    durations = np.diff(frame_times, append=frame_times[-1])  # Duration per note

    return notes_sequence, prominent_freq_hz, durations

if __name__ == "__main__":
    file_path = "mp3-files/sample-test-1.mp3"
    
    # Analyze audio and extract features
    y, sr, result = analyze_audio(file_path)
    print(f"Duration: {result['duration']} seconds")
    print(f"Spectral Centroid (mean): {result['spectral_centroid'].mean()}")
    
    # Perform Harmonic-Percussive Separation (HPSS)
    y_harmonic, y_percussive = harmonic_percussive_separation(y,sr)
    
    # Extract notes from the harmonic component (melody/vocals)
    notes_sequence, freq_sequence, durations = extract_notes_in_sequence(y_harmonic, sr)
    
    print("Sequential Notes (in order of appearance):")
    for note, dur in zip(notes_sequence, durations):
        print(f"{note}: {dur:.2f} sec")
    
    # Play the harmonic (melodic) component
    print("Playing harmonic (melodic) part...")
    play_audio(y_harmonic, sr)
