# 08_neopixel.py
# Control a strip of NeoPixel (WS2812B) RGB LEDs.
# Works on: Raspberry Pi Pico, ESP32, ESP8266
#
# Wiring:
#   - NeoPixel DIN (data) → GPIO 16
#   - NeoPixel VCC        → 5 V (or 3.3 V for short strips)
#   - NeoPixel GND        → GND
#
# The neopixel module is built into MicroPython – no extra install needed.

import machine
import neopixel
import utime

NUM_LEDS = 8   # change to match your strip length
PIN      = 16  # data pin

strip = neopixel.NeoPixel(machine.Pin(PIN), NUM_LEDS)

def set_all(r, g, b):
    """Set every LED to the same colour."""
    for i in range(NUM_LEDS):
        strip[i] = (r, g, b)
    strip.write()

colours = [
    (255,   0,   0),  # red
    (  0, 255,   0),  # green
    (  0,   0, 255),  # blue
    (255, 255,   0),  # yellow
    (  0, 255, 255),  # cyan
    (255,   0, 255),  # magenta
    (255, 255, 255),  # white
    (  0,   0,   0),  # off
]

print("Cycling through colours. Press Ctrl-C to stop.")

while True:
    for colour in colours:
        set_all(*colour)
        utime.sleep_ms(500)
