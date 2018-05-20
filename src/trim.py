import numpy as np
import wave
import struct
import sys

def print_usage():
    print("Usage: python trim.py input-wave-file output-wave-file")

def trim_sound():
    None

if len(sys.argv) != 3:
    print_usage()
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

with wave.open(input_file, 'rb') as input_wave:
    frames = input_wave.readframes(input_wave.getnframes())
    wave_params = input_wave.getparams()
    data = np.frombuffer(frames, dtype="int16")

    with wave.open(output_file, "wb") as output_wave:
        output_wave.setparams(wave_params)
        output_wave.writeframes(b''.join(data))
        output_wave.close()