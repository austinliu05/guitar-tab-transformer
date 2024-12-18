import librosa 
import librosa.display
import matplotlib.pyplot as plt
from utils import calculate_time_per_measure
import numpy as np 
import os

def visualize_waveform(file_path):
    y, sr = librosa.load(file_path, sr=None)

    # Plotting waveform
    plt.figure(figsize=(10,4))
    librosa.display.waveshow(y, sr=sr)
    plt.title("Waveform")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")

    # Save the visualization
    file_name = file_path.split('/')[-1]
    os.makedirs('results', exist_ok=True)
    plt.savefig(f'results/{file_name}_waveform.png')
    plt.close()

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

    # Save the visualization
    file_name = file_path.split('/')[-1]
    os.makedirs('results', exist_ok=True)
    plt.savefig(f'results/{file_name}_spectral_centroid.png')
    plt.close()

def visualize_spectrogram_with_bars(file_path, tempo, time_signature):
    y, sr = librosa.load(file_path, sr=None)

    # Calculate measure duration
    measure_duration = calculate_time_per_measure(tempo, time_signature)

    total_duration = librosa.get_duration(y=y, sr=sr)
    measure_boundaries = np.arange(0, total_duration, measure_duration)

    # Compute spectrogram
    spectrogram = librosa.stft(y)
    spectrogram_db = librosa.amplitude_to_db(np.abs(spectrogram), ref=np.max)

    # Plot the spectrogram
    plt.figure(figsize=(12, 6))
    librosa.display.specshow(
        spectrogram_db, sr=sr, x_axis='time', y_axis='log', cmap='magma'
    )

    measures = 0
    # Overlay bar boundaries as vertical lines
    for measure_time in measure_boundaries:
        plt.axvline(x=measure_time, color='cyan', linestyle='--', linewidth=1)
        measures+=1

    plt.title("Spectrogram with Bar Boundaries")
    plt.colorbar(format='%+2.0f dB')
    plt.xlabel("Time (s)")
    plt.ylabel("Frequency (Hz)")

    # Save the visualization
    file_name = file_path.split('/')[-1]
    os.makedirs('results', exist_ok=True)
    plt.savefig(f'results/{file_name}_spectrogram_with_bars.png')
    plt.close()

    print("Measures: ", measures)
    print("Bar duration: ", measure_duration)

if __name__ == "__main__":
    file_path = "mp3-files/sample-test-1.mp3"

    # Visualize the waveform and spectral centroid
    visualize_waveform(file_path)
    visualize_spectral_centroid(file_path)
    visualize_spectrogram_with_bars(file_path, 78, (4,4))
