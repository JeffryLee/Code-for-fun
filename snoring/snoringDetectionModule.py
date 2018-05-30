import numpy as np
import scipy.signal as signal
from scipy.io import wavfile

class snoringDetection():
    def myfilter(self, signal, window=20):
        windowForward = window / 2
        windowBackward = window - window / 2
        ret = np.zeros(len(signal))
        accumulator = 0
        for i in range(windowBackward - 1):
            accumulator += signal[i]
        for i in range(len(signal)):
            lowRange = max(0, i - windowForward)
            highRange = min(len(signal), i + windowBackward)

            if lowRange > 0:
                accumulator -= signal[lowRange - 1]

            if highRange <= len(signal):
                accumulator += signal[highRange - 1]

            ret[i] = accumulator / (highRange - lowRange)
        return ret

    def downSampling(self, data, rate):
        sampled = [data[i] for i in range(0, len(data), rate)]
        return np.array(sampled)

    def detect(self, sampFreq, snd):
        if type(snd[0]) != np.int16:
            sndBackup = [snd[i][0] for i in range(len(snd))]
            snd = np.array(sndBackup)

        width = np.array(range(int(0.15 * sampFreq), int(3 * sampFreq), int(0.05 * sampFreq))) / 100

        snd = snd / 1000.0

        power = abs(snd)
        power = self.myfilter(power, sampFreq)

        powerSample = self.downSampling(power, 100)

        window = signal.general_gaussian(500, p=0.5, sig=500)
        filtered = signal.fftconvolve(window, powerSample)
        filtered = (np.average(powerSample) / np.average(filtered)) * filtered
        filtered = np.roll(filtered, -25)

        peaks = signal.find_peaks_cwt(filtered, width)

        peakTimeDiff = [peaks[i] - peaks[i - 1] for i in range(1, len(peaks))]

        return (np.std(peakTimeDiff) / np.mean(peakTimeDiff))<0.4