import time
import neopixel

millis = lambda: int(round(time.time() * 1000))

def launch_loading_animation(frame_delay, neopixels, count_leds):
    for i in range(3):
        rainbow_cycle(frame_delay, neopixels, count_leds)

    while neopixels.brightness > 0.:
            neopixels.brightness -= 0.01
            neopixels.show()
            time.sleep(0.005)


def rainbow_cycle(frame_delay, neopixels, count_leds):
    for j in range(255):
        for i in range(count_leds):
            pixel_index = (i * 256 // count_leds) + j
            neopixels[i] = wheel(pixel_index & 255)
        neopixels.show()
        time.sleep(frame_delay)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b)