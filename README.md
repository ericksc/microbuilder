# microbuilder

A collection of beginner-friendly MicroPython examples for microcontrollers such as the Raspberry Pi Pico, ESP32, and ESP8266.

## Examples

| File | What it demonstrates |
|------|----------------------|
| [01_blink.py](examples/01_blink.py) | Blink the built-in LED – the "Hello, World!" of hardware |
| [02_button.py](examples/02_button.py) | Read a push-button with an internal pull-up resistor |
| [03_pwm_led.py](examples/03_pwm_led.py) | Fade an LED in and out with PWM |
| [04_adc.py](examples/04_adc.py) | Read an analog value (potentiometer / sensor) via ADC |
| [05_uart.py](examples/05_uart.py) | Send and receive data over UART serial |
| [06_i2c_scan.py](examples/06_i2c_scan.py) | Scan the I2C bus and list connected device addresses |
| [07_timer.py](examples/07_timer.py) | Blink an LED with a hardware timer (non-blocking) |
| [08_neopixel.py](examples/08_neopixel.py) | Cycle colours on a NeoPixel (WS2812B) LED strip |

## Getting started

1. Install [MicroPython](https://micropython.org/download/) on your board.
2. Copy the example file you want to your board using [Thonny](https://thonny.org/) or `mpremote`.
3. Run the file – adjust pin numbers at the top of each script to match your wiring.

## Requirements

- MicroPython v1.20 or later
- No third-party libraries needed; all examples use the MicroPython standard library