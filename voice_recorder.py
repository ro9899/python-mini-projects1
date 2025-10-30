"""
voice_recorder.py

Record audio from the default microphone and save as WAV file.

Dependencies:
  pip install sounddevice numpy wavio

Why these?
- sounddevice: cross-platform audio I/O
- numpy: required by sounddevice
- wavio: easy WAV writer

Usage:
  python voice_recorder.py
Then enter duration in seconds and filename (or press Enter for default).
"""
import time
import sys

try:
    import sounddevice as sd
    import numpy as np
    import wavio
except Exception as e:
    print("Missing dependency. Install with: pip install sounddevice numpy wavio")
    print("Error detail:", e)
    sys.exit(1)


def record(duration_sec=5, fs=44100, channels=1):
    """Record audio for duration_sec seconds and return numpy array."""
    print(f"Recording for {duration_sec} seconds... Speak now.")
    recording = sd.rec(int(duration_sec * fs), samplerate=fs, channels=channels, dtype="int16")
    sd.wait()  # wait until recording is finished
    return recording, fs


def main():
    try:
        duration = float(input("Enter duration in seconds (e.g., 5): ") or "5")
    except ValueError:
        print("Invalid number. Using 5 seconds.")
        duration = 5.0

    filename = input("Enter output filename (without extension) [voice_record]: ") or "voice_record"
    out_wav = f"{filename}.wav"

    data, samplerate = record(duration_sec=duration)
    # wavio expects shape (n_samples, channels)
    wavio.write(out_wav, data, samplerate, sampwidth=2)
    print(f"Saved recording to '{out_wav}'.")


if __name__ == "__main__":
    main()
