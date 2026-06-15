# 02_button.py
# Read a push-button and print a message when it is pressed.
# Works on: Raspberry Pi Pico, ESP32, ESP8266
#
# Wiring:
#   - One leg of the button → GPIO 14
#   - Other leg            → GND
#   The internal pull-up resistor is enabled, so no external resistor is needed.

import machine
import utime

button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)

print("Press the button!")

while True:
    if button.value() == 0:  # button pulls pin LOW when pressed
        print("Button pressed!")
        utime.sleep_ms(200)  # simple debounce delay
