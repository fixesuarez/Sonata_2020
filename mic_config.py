import pyaudio

py_audio = pyaudio.PyAudio()
for ii in range(py_audio.get_device_count()):
	print(py_audio.get_device_info_by_index(ii).get('name'))
