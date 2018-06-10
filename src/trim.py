import numpy as np
import wave
import struct
import sys

def print_usage():
    print("Usage: python trim.py input-wave-file output-wave-file start-frame end-frame")

def trim_sound():
    None

if len(sys.argv) != 5:
    print_usage()
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]
start_frame = int(sys.argv[3])
end_frame = int(sys.argv[4])

with wave.open(input_file, 'rb') as input_wave:
    frames = input_wave.readframes(input_wave.getnframes())
    wave_params = input_wave.getparams()
    data = np.frombuffer(frames, dtype="int16")

    with wave.open(output_file, "wb") as output_wave:
        output_frame_count = end_frame - start_frame + 1

        start_index = start_frame * wave_params.nchannels * wave_params.sampwidth
        end_index = (end_frame + 1) * wave_params.nchannels * wave_params.sampwidth
        output_data = b''.join(data)[start_index:end_index]

        output_wave.setnchannels(wave_params.nchannels)
        output_wave.setsampwidth(wave_params.sampwidth)
        output_wave.setframerate(wave_params.framerate)
        output_wave.setnframes(output_frame_count)
        output_wave.writeframes(output_data)
        output_wave.close()