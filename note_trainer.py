import traceback
import numpy
from scipy.signal import fftconvolve

from constants import NOTES, NOTES_DICTIONNARY, RATE, SOUND_GATE
from sound_recorder import SoundRecorder

class NoteTrainer:
    def __init__(self, note_listener):
        self.note_listener = note_listener

    def main():
        print("Initiating SoundRecorder...")
        sound_recorder = SoundRecorder()

        while True:
            try:
                sound_recorder.setup()
                raw_data_signal = sound_recorder.get_audio()
                signal_level = round(abs(loudness(raw_data_signal)), 2)

                try:
                    frequence = freq_from_autocorr(raw_data_signal, RATE)
                    input_note = round(frequence, 2)
                except Exception as e:
                    input_note = 0

                sound_recorder.close()

                if input_note > NOTES[len(NOTES_DICTIONNARY)-1] or input_note < NOTES[0]:
                    continue
                if signal_level > SOUND_GATE:
                    continue

                target_note = closest_value_index(NOTES, round(input_note, 2))

                print("signal_level:", signal_level, targetnote)
                print("frequency: ", str(inputnote)+"Hz")
                print("tuner note", NOTES_DICTIONNARY[NOTES[target_note]])
                print("target note: ", target_note)

                if self.note_listener != None:
                    self.note_listener.note(input_note)

            except Exception as e:
                print(traceback.format_exc())


def loudness(chunk):
    data = numpy.array(chunk, dtype=float) / 32768.0
    ms = math.sqrt(numpy.sum(data ** 2.0) / len(data))
    if ms < 10e-8: ms = 10e-8
    return 10.0 * math.log(ms, 10.0)


# See https://github.com/endolith/waveform-analyzer/blob/master/frequency_estimator.py
def freq_from_autocorr(raw_data_signal, fs):
    corr = fftconvolve(raw_data_signal, raw_data_signal[::-1], mode='full')
    corr = corr[int(math.floor(len(corr)/2)):]
    d = numpy.diff(corr)
    start = find(d > 0)[0]
    peak = numpy.argmax(corr[start:]) + start
    px, py = parabolic(corr, peak)
    return fs / px

def find(condition):
    res, = nonzero(ravel(condition))
    return res

# See https://github.com/endolith/waveform-analyzer/blob/master/frequency_estimator.py
def parabolic(f, x):
    xv = 1/2. * (f[x-1] - f[x+1]) / (f[x-1] - 2 * f[x] + f[x+1]) + x
    yv = f[x] - 1/4. * (f[x-1] - f[x+1]) * (xv - x)
    return (xv, yv)


def closest_value_index(array, guessValue):
    # Find closest element in the array, value wise
    closestValue = find_nearest(array, guessValue)
    # Find indices of closestValue
    indexArray = numpy.where(array==closestValue)
    # Numpys 'where' returns a 2D array with the element index as the value
    return indexArray[0][0]
    
def find_nearest(array, value):
    index = (numpy.abs(array - value)).argmin()
    return array[index]
