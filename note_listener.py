import time
from utilities import millis, wheel
from constants import LED_COUNT, FREQUENCY_START, FREQUENCY_END, WIDE

class NoteListener:
    def __init__(self, neopixels):
        self.neopixels = neopixels
        self.index = 0
        self.last_update = millis()
        self.brightness=0.9

    def fade(self):
        pass
        # if self.last_update+90 < millis():
        #     if self.brightness > 0.02:
        #         self.brightness -= 0.02
        #     else:
        #         self.brightness = 0.
        # elif self.brightness < 0.97:
        #     self.brightness += 0.2
        # self.neopixels.brightness = self.brightness
        # self.neopixels.show()

    def note(self, frequency):
        if frequency < FREQUENCY_END and frequency > FREQUENCY_START:
            pos = int((frequency-FREQUENCY_START) / WIDE * 255)
            color =  wheel(pos)
            # self.neopixels[self.index] = color
            self.neopixels.fill((255, 0, 0))
            self.neopixels.brightness = 0.9
            self.neopixels.show()
            print("Color: ", wheel(pos))
            print("neopixels: ", self.neopixels)
            print("Brightness: ", self.neopixels.brightness)

            self.increment()
            time.sleep(4)

    def increment(self):
        self.index += 1
        if self.index >= LED_COUNT:
            self.index = 0
        self.last_update = millis()
