from utilities import millis, wheel
from constants import LED_COUNT

class NoteListener:
    def __init__(self, neopixel, frequency_start, frequency_end):
        self.neopixel = neopixel
        self.index = 0
        self.frequency_start = frequency_start
        self.frequency_end = frequency_end
        self.wide = frequency_start - frequency_end
        self.last_update = millis
        self.brightness=1.0

    def fade(self):
        if self.last_update+90 < millis():
            if self.brightness > 0.02:
                self.brightness -= 0.02
        elif self.brightness < 0.97:
            self.brightness += 0.2
        self.neopixel.brightness = self.brightness

    def note(self, frequency):
        if frequency < self.frequency_end and frequency > selffrequency_start:
            pos = int((frequency-self.frequency_start) / self.wide * 255)
            self.neopixel[self.index] = wheel(pos)
            self.neopixel.show()
            self.inc

    def increment(self):
        self.index += 1
        if self.index >= LED_COUNT:
            self.index = 0
        self.last_update = millis()
