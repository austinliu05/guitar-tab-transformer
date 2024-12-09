import librosa
from tqdm import tqdm
from visualization import visualize_spectral_centroid, visualize_waveform

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
    
    return features
    
if __name__ == "__main__":
    file_path = "mp3-files/sample-test-1.mp3"
    
    # Analyze audio and extract features
    result = analyze_audio(file_path)
    print(f"Duration: {result['duration']} seconds")
    print(f"Spectral Centroid (mean): {result['spectral_centroid'].mean()}")

    # Visualize the waveform and spectral centroid
    visualize_waveform(file_path)
    visualize_spectral_centroid(file_path)