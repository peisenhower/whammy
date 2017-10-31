#!/usr/bin/python3
import threading
import Adafruit_PCA9685
import time

FADE_INTERVAL = 0.1
FADE_INCREMENT = 200
LED_VALUES = [100] * 10

# Configure min and max servo pulse lengths
servo_min = 50  # Min pulse length out of 4096
servo_max = 400  # Max pulse length out of 4096

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)
pwm.set_pwm(10, 0, 2047)

def fade_callback(led):
    if LED_VALUES[led] >= 4095:
        return

    LED_VALUES[led] += FADE_INCREMENT
    if LED_VALUES[led] > 4094:
        LED_VALUES[led] = 4095

    #print(f'Led Update, Led:{led}, Value:{LED_VALUES[led]}')
    pwm.set_pwm(led, 0, LED_VALUES[led])
    threading.Timer(FADE_INTERVAL, fade_callback, [led]).start()


def fade(led):
    threading.Timer(FADE_INTERVAL, fade_callback, [led]).start()


def off(led):
    pwm.set_pwm(led, 0, 4095)
    LED_VALUES[led] = 4095

def on(led):
    pwm.set_pwm(led, 0, 0)
    LED_VALUES[led] = 0

def blink(old_led, led):
    pwm.set_pwm(led, 0, 0)
    pwm.set_pwm(old_led, 0, 4095)

def whammy():
    pwm.set_pwm(9, 0, servo_max)
    time.sleep(.4)
    pwm.set_pwm(9, 0, servo_min)



if __name__ == "__main__":
    on(0)
    on(1)
    on(2)
    on(3)

    time.sleep(1)

    off(0)
    off(1)
    off(2)
    off(3)

