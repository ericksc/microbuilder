# 04_adc.py
# Read an analog value from a potentiometer (or any analog sensor).
# Works on: Raspberry Pi Pico, ESP32, ESP8266
#
# Wiring (potentiometer):
#   - Left pin  → 3.3 V
#   - Middle pin → ADC pin (GPIO 26 on Pico / GPIO 34 on ESP32)
#   - Right pin  → GND

import machine
import utime

adc = machine.ADC(26)  # GPIO 26 = ADC0 on Pico; change pin for ESP32

while True:
    raw = adc.read_u16()           # 16-bit value: 0 – 65535
    voltage = raw * 3.3 / 65535    # convert to volts (3.3 V reference)
    print(f"Raw: {raw:5d}  |  Voltage: {voltage:.2f} V")
    utime.sleep_ms(500)
