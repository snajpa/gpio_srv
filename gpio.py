#!/usr/bin/env python
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

defaults = {'on': GPIO.LOW, 'off': GPIO.HIGH, 'default': 'off'}

INFO = {
    18: defaults,
    23: defaults,
    24: defaults,
    25: defaults,
}

PINS = INFO.keys()

def setup():
    for pin, info in INFO.items():
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, info[info['default']])

def valid(val):
    return val >= 0 and val < len(PINS)


def on(pmap):
    pin = PINS[pmap]
    info = INFO[pin]
    GPIO.output(pin, info['on'])


def off(pmap):
    pin = PINS[pmap]
    info = INFO[pin]
    GPIO.output(pin, info['off'])

if __name__ == '__main__':
    setup()
