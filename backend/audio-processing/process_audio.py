import librosa
from tqdm import tqdm
import numpy as np

def analyze_audio(file_path):
    # Loading the audio file
    '''
    y: NumPy array
        - Represents the audio time series (waveform).
        - Contains the amplitude values of the audio signal over time.
        - If the audio is mono, `y` will be a 1D array.
        - If the audio is stereo, `y` will be a 2D array where each row corresponds to a channel.
    
    sr: int
        - Sampling rate of the audio file (number of samples per second).
        - If `sr=None`, the original sampling rate of the audio file is preserved.
        - Default sampling rate in librosa is 22,050 Hz if `sr` is not explicitly set.
    '''
    y, sr = librosa.load(file_path, sr = None)
    
    features = {}
    with tqdm(total=2, desc="Extracting features") as pbar:
        features['duration'] = librosa.get_duration(y=y, sr=sr)
        pbar.update(1)
        
        spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
        features['spectral_centroid'] = spectral_centroid.mean()
        pbar.update(1)
    
    return y, sr, features
    
def extract_notes(y, sr):    
    # Compute spectrogram
    spectrogram = librosa.stft(y)
    spectrogram_db = librosa.amplitude_to_db(np.abs(spectrogram), ref=np.max)
    
    # Identifying prominent features
    prominent_freq = np.argmax(np.abs(spectrogram), axis = 0) # Finds index of the maximum value 
    prominent_freq_hz = prominent_freq * (sr / spectrogram.shape[0]) # Converting freq into hertz
    
    # Handle invalid frequencies
    prominent_freq_hz = np.nan_to_num(prominent_freq_hz, nan=0.0, posinf=0.0, neginf=0.0)
    valid_freq_hz = prominent_freq_hz[prominent_freq_hz > 0]  # Retain only positive frequencies
    
    # Convert valid frequencies to notes
    notes = librosa.hz_to_note(valid_freq_hz)
    
    # Aggregate and filter notes (optional, to remove duplicates or noise)
    unique_notes, counts = np.unique(notes, return_counts=True)
    note_frequencies = dict(zip(unique_notes, counts))

    return note_frequencies
if __name__ == "__main__":
    file_path = "mp3-files/sample-test-1.mp3"
    
    # Analyze audio and extract features
    y,sr, result = analyze_audio(file_path)
    print(f"Duration: {result['duration']} seconds")
    print(f"Spectral Centroid (mean): {result['spectral_centroid'].mean()}")
    
    # Extract notes for the entire song
    note_frequencies = extract_notes(y, sr)
    print("Extracted Notes:")
    for note, count in note_frequencies.items():
        print(f"{note}: {count} occurrences")