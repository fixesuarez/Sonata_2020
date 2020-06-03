import pyaudio
from alsa_error_manager import ErrorManager

with ErrorManager():
	py_audio = pyaudio.PyAudio()
	for ii in range(py_audio.get_device_count()):
			device = py_audio.get_device_info_by_index(ii)
			if 'USB' in device['name']:
					print('micro index is', ii)
			else:
					print('No USB micro found')
