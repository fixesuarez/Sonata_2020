import pyaudio
import numpy
from alsa_error_manager import ErrorManager
from constants import RATE, BUFFER_SIZE

class SoundRecorder:
    def __init__(self):
        self.py_audio = pyaudio.PyAudio()
        device_index = self.get_micro_device_index()
        self.in_stream = None

    def get_micro_device_index(self):
        device_index = 0
        with ErrorManager():
            for ii in range(self.py_audio.get_device_count()):
                    device = self.py_audio.get_device_info_by_index(ii)
                    if 'USB' in device['name']:
                            print('micro index is', ii)
                            device_index = ii

            if device_index is 0:
                print('No micro device found')

        return device_index

    
    def setup(self):
        self.in_stream = self.py_audio.open(input_device_index=device_index, format=pyaudio.paInt16, channels=1,
                                            rate=RATE, input=True, frames_per_buffer=BUFFER_SIZE)

    def close(self):
        self.py_audio.close(self.in_stream)


    def get_audio(self):
        audio_string = self.in_stream.read(BUFFER_SIZE)
        return numpy.fromstring(audio_string, dtype=numpy.int16)
