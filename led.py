
import threading
#import Adafruit_PCA9685
import time

FADE_INTERVAL = 0.2
FADE_INCREMENT = 10
LED_VALUES = [100] * 10

# Initialise the PCA9685 using the default address (0x40).
#pwm = Adafruit_PCA9685.PCA9685()

def fade_callback(led):
    if LED_VALUES[led] <= 0:
        return

    LED_VALUES[led] -= FADE_INCREMENT

    #print(f'Led Update, Led:{led}, Value:{LED_VALUES[led]}')
    # todo i2c call here
    threading.Timer(FADE_INTERVAL, fade_callback, [led]).start()


def fade(led):
    threading.Timer(FADE_INTERVAL, fade_callback, [led]).start()

def blink(led):
    #pwm.setPWM(led, 0, 4095)
    #time.sleep(1)
    #pwm.setPwm(led, 4095, 0)
