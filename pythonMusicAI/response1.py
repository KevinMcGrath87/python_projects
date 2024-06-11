import math
import simpleaudio as sa  # A basic audio playback library


frequencies = {
    'C4': 261.63,
    'C#4': 277.18,
    'D4': 293.66,
    # ... add more notes for your desired range
}


def generate_sine_wave(frequency, duration, amplitude=0.5, sample_rate=44100):
    samples = int(duration * sample_rate / 1000) 
    waveform = [amplitude * math.sin(2 * math.pi * frequency * t / sample_rate)
                for t in range(samples)]
    return waveform


def play_note(note, duration_ms):
    frequency = frequencies.get(note)
    if frequency:
        waveform = generate_sine_wave(frequency, duration_ms)

        # Convert waveform to appropriate format for simpleaudio
        audio = sa.play_buffer(waveform, 1, 2, sample_rate)  
        audio.wait_done()
    else:
        print("Invalid note provided.")