from utilities import millis, wheel
from constants import LED_COUNT, FREQUENCY_START, FREQUENCY_END, WIDE

class NoteListener:
    def __init__(self, neopixel):
        self.neopixel = neopixel
        self.index = 0
        self.last_update = millis()
        self.brightness=1.0

    def fade(self):
        if self.last_update+90 < millis():
            if self.brightness > 0.02:
                self.brightness -= 0.02
        elif self.brightness < 0.97:
            self.brightness += 0.2
        self.neopixel.brightness = self.brightness

    def note(self, frequency):
        if frequency < FREQUENCY_END and frequency > FREQUENCY_START:
            pos = int((frequency-FREQUENCY_START) / WIDE * 255)
            self.neopixel[self.index] = wheel(pos)
            print("pos: ", pos)
            print("wheel position: ", wheel(pos))
            self.neopixel.show()
            self.increment()

    def increment(self):
        self.index += 1
        if self.index >= LED_COUNT:
            self.index = 0
        self.last_update = millis()
