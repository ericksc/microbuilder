# 03_pwm_led.py
# Fade an LED in and out using PWM (Pulse Width Modulation).
# Works on: Raspberry Pi Pico, ESP32, ESP8266
#
# Wiring:
#   - LED anode  (long leg)  → 330 Ω resistor → GPIO 15
#   - LED cathode (short leg) → GND

import machine
import utime

led = machine.PWM(machine.Pin(15))
led.freq(1000)  # 1 kHz PWM frequency

while True:
    # Fade in: 0 → max duty
    for duty in range(0, 65536, 512):
        led.duty_u16(duty)
        utime.sleep_ms(10)

    # Fade out: max duty → 0
    for duty in range(65535, -1, -512):
        led.duty_u16(duty)
        utime.sleep_ms(10)
