# 05_uart.py
# Send and receive data over UART (serial communication).
# Works on: Raspberry Pi Pico, ESP32, ESP8266
#
# Wiring (loopback test – connect TX to RX on the same board):
#   - GPIO 0 (TX) → GPIO 1 (RX)  [Pico UART0]
#
# To talk to a PC, connect a USB-to-TTL adapter:
#   - Adapter TX → board RX (GPIO 1)
#   - Adapter RX → board TX (GPIO 0)
#   - Adapter GND → board GND

import machine
import utime

uart = machine.UART(0, baudrate=9600, tx=machine.Pin(0), rx=machine.Pin(1))

print("UART ready. Sending a message every 2 seconds.")

counter = 0
while True:
    message = f"Hello from MicroPython! Count: {counter}\n"
    uart.write(message)
    print("Sent:", message.strip())

    if uart.any():
        received = uart.read()
        print("Received:", received)

    counter += 1
    utime.sleep(2)
