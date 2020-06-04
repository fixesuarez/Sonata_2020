import numpy

LED_COUNT = 15

### SoundRecorder
RATE = 44100
BUFFER_SIZE = 1024 #1024 is a good buffer size 3072 works for Pi
# SECONDS_TO_RECORD = 0.05
# if int(RATE * SECONDS_TO_RECORD / BUFFER_SIZE) == 0 
#     BUFFERS_TO_RECORD = 1
# else 
#     BUFFERS_TO_RECORD = int(RATE * SECONDS_TO_RECORD / BUFFERSIZE)
#SAMPLE_TO_RECORD = int(BUFFER_SIZE * BUFFERS_TO_RECORD)
# CHUNKS_TO_RECORD = int(SAMPLE_TO_RECORD / BUFFER_SIZE)
# SEC_PER_POINT = 1.0 / RATE

NOTES_DICTIONNARY = {
    65.41:'C2',
    69.30:'C2#',
    73.42:'D2',
    77.78:'E2b',
    82.41:'E2',
    87.31:'F2',
    92.50:'F2#',
    98.00:'G2',
    103.80:'G2#',
    110.00:'A2',
    116.50:'B2b',
    123.50:'B2',
    130.80:'C3',
    138.60:'C3#',
    146.80:'D3',
    155.60:'E3b',
    164.80:'E3',
    174.60:'F3',
    185.00:'F3#',
    196.00:'G3',
    207.70:'G3#',
    220.00:'A3',
    233.10:'B3b',
    246.90:'B3',
    261.60:'C4',
    277.20:'C4#',
    293.70:'D4',
    311.10:'E4b',
    329.60:'E4',
    349.20:'F4',
    370.00:'F4#',
    392.00:'G4',
    415.30:'G4#',
    440.00:'A4',
    466.20:'B4b',
    493.90:'B4',
    523.30:'C5',
    554.40:'C5#',
    587.30:'D5',
    622.30:'E5b',
    659.30:'E5',
    698.50:'F5',
    740.00:'F5#',
    784.00:'G5',
    830.60:'G5#',
    880.00:'A5',
    932.30:'B5b',
    987.80:'B5',
    1047.00:'C6',
    1109.0:'C6#',
    1175.0:'D6',
    1245.0:'E6b',
    1319.0:'E6',
    1397.0:'F6',
    1480.0:'F6#',
    1568.0:'G6',
    1661.0:'G6#',
    1760.0:'A6',
    1865.0:'B6b',
    1976.0:'B6',
    2093.0:'C7'
}
NOTES = numpy.array(sorted(NOTES_DICTIONNARY.keys()))

FADE_WORKER_DELAY = 50
SOUND_GATE = 17.5
