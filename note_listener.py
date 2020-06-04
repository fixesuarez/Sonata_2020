from utilities import millis

class NoteListener:
    def __init__(self, neopixel, frequency_start, frequency_end):
        self.neopixel = neopixel
        self.index = 0
        self.frequency_start = frequency_start
        self.frequency_end = frequency_end
        self.wide = frequency_start - frequency_end
        self.last_update = millis
        self.brightness=255
