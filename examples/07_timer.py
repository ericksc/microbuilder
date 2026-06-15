# 07_timer.py
# Use a hardware Timer to blink an LED without blocking the main loop.
# Works on: Raspberry Pi Pico, ESP32, ESP8266
#
# Wiring: no extra hardware needed – uses the built-in LED.

import machine

led = machine.Pin("LED", machine.Pin.OUT)  # use Pin(25) for standard Pico

def toggle_led(timer):
    """Callback invoked by the timer interrupt."""
    led.toggle()

# Fire the callback every 500 ms (2 Hz blink)
timer = machine.Timer()
timer.init(period=500, mode=machine.Timer.PERIODIC, callback=toggle_led)

print("Timer started. The LED blinks every 500 ms.")
print("The main loop is free to do other work.")

counter = 0
while True:
    print(f"Main loop tick {counter}")
    counter += 1
    machine.idle()  # sleep until the next interrupt to save power
