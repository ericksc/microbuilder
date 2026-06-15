# 06_i2c_scan.py
# Scan the I2C bus and print the addresses of all connected devices.
# Works on: Raspberry Pi Pico, ESP32, ESP8266
#
# Wiring:
#   - SDA → GPIO 4   (Pico default I2C0 SDA)
#   - SCL → GPIO 5   (Pico default I2C0 SCL)
#   - Device VCC → 3.3 V
#   - Device GND → GND
#   Most I2C devices need 4.7 kΩ pull-up resistors on SDA and SCL.

import machine

i2c = machine.I2C(0, sda=machine.Pin(4), scl=machine.Pin(5), freq=400_000)

devices = i2c.scan()

if devices:
    print(f"Found {len(devices)} I2C device(s):")
    for addr in devices:
        print(f"  Address: 0x{addr:02X}  (decimal {addr})")
else:
    print("No I2C devices found. Check your wiring.")
