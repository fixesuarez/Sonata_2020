import time
import board
import neopixel

from utilities import launch_loading_animation
from constants import FADE_WORKER_DELAY
from note_listener import NoteListener
from fade_worker import FadeWorker
from note_trainer import NoteTrainer


# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 15

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

neopixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.9, auto_write=False, pixel_order=ORDER
)

if __name__ == '__main__':
    launch_loading_animation(0.002, neopixels, num_pixels)

    try:
        note_listener = NoteListener(neopixels, 80, 710)
        fade_worker = FadeWorker(note_listener, FADE_WORKER_DELAY)
        fade_worker.start()

        note_trainer = NoteTrainer(note_listener)
        print("Note trainer built")
        note_trainer.main()

    except KeyboardInterrupt:
        neopixels.brightness = 0.
        neopixels.show()
        fade_worker.stop()
        neopixels.deinit()
