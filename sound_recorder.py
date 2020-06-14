import pyaudio
import numpy
from alsa_error_manager import ErrorManager
from constants import RATE, BUFFER_SIZE

class SoundRecorder:
    def __init__(self):
        self.py_audio = None
        # self.device_index = self.get_micro_device_index()
        self.device_index = 2
        self.in_stream = None

    def get_micro_device_index(self):
        print("Creating pyaudio instance")
        py_audio = pyaudio.PyAudio()
        device_index = 0
        try:
            device_count = py_audio.get_device_count()
            print("Device_count: ", device_count)
            for ii in range(device_count):
                    device = py_audio.get_device_info_by_index(ii)
                    if 'USB' in device['name']:
                            print('micro index is', ii)
                            device_index = ii

            if device_index is 0:
                print('No micro device found')
        except Exception as e:
            print("Error getting device index")
            print(e)

        return device_index

    
    def setup(self):
        self.py_audio = pyaudio.PyAudio()
        self.in_stream = self.py_audio.open(input_device_index=self.device_index, format=pyaudio.paInt16, channels=1,
                                            rate=RATE, input=True, frames_per_buffer=BUFFER_SIZE)

    def close(self):
        self.py_audio.close(self.in_stream)


    def get_audio(self):
        audio_string = self.in_stream.read(BUFFER_SIZE)
        numpy_audio = numpy.fromstring(audio_string, dtype=numpy.int16)
        return numpy_audio
