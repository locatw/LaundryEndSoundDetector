from matplotlib import pyplot
import numpy as np
import sys
import wave

DPI = 64
FFT_SAMPLE_LEN = 1024

input_file = sys.argv[1]
output_file = sys.argv[2]

# Setup to save spectrogram image without axes.
fig, axis = pyplot.subplots(1)
fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
axis.axis('off')

with wave.open(input_file, 'rb') as input_wave:
    frames = input_wave.readframes(input_wave.getnframes())
    wave_params = input_wave.getparams()
    data = np.frombuffer(frames, dtype="int16")

    window = np.hamming(FFT_SAMPLE_LEN)
    spec, freqs, spec_t, image = pyplot.specgram(data,
                                                 NFFT=FFT_SAMPLE_LEN,
                                                 Fs=wave_params.framerate,
                                                 noverlap=0,
                                                 window=window)
    pyplot.savefig(output_file, dpi=DPI, frameon='false')