# 01_blink.py
# Blink the onboard LED every second.
# Works on: Raspberry Pi Pico, ESP32, ESP8266
#
# Wiring: no extra hardware needed – uses the built-in LED.

import machine
import utime

# On most boards the built-in LED is on pin 25 (Pico) or pin 2 (ESP32).
# Change the pin number to match your board if needed.
led = machine.Pin("LED", machine.Pin.OUT)  # "LED" works on Pico W; use Pin(25) for Pico

while True:
    led.toggle()
    utime.sleep(1)  # wait 1 second
