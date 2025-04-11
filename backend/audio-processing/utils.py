def calculate_time_per_measure(tempo, time_signature):
    '''
    Calculate the time duration of each measure in seconds.

    Parameters:
        tempo (float): The tempo in beats per minute (BPM).
        time_signature (tuple): A tuple representing the time signature (e.g., (4, 4) for 4/4).

    Returns:
        float: Time duration of each measure in seconds.
    '''
    beats_per_measure = time_signature[0] # Numerator in the time signature
    time_per_beat = 60 / tempo # Number of seconds per beat
    return beats_per_measure * time_per_beat