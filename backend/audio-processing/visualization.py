import librosa 
import librosa.display
import matplotlib.pyplot as plt

def visualize_waveform(file_path):
    y, sr = librosa.load(file_path, sr=None)
    
    # Plotting waveform
    plt.figure(figsize=(10,4))
    librosa.display.waveshow(y, sr=sr)
    plt.title("Waveform")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.show()
    
def visualize_spectral_centroid(file_path):
    y, sr = librosa.load(file_path, sr=None)

    # Calculate spectral centroid
    spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
    times = librosa.times_like(spectral_centroid, sr=sr)

    # Plot waveform with spectral centroid
    plt.figure(figsize=(10, 4))
    librosa.display.waveshow(y, sr=sr, alpha=0.4)
    plt.plot(times, spectral_centroid[0], color='r', label='Spectral Centroid')
    plt.title('Spectral Centroid')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.show()
