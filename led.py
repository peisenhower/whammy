
import threading


FADE_INTERVAL = 0.2
FADE_INCREMENT = 10
LED_VALUES = [100] * 9

def fade_callback(led):
    if LED_VALUES[led] <= 0:
        return

    LED_VALUES[led] -= FADE_INCREMENT

    #print(f'Led Update, Led:{led}, Value:{LED_VALUES[led]}')
    # todo i2c call here
    threading.Timer(FADE_INTERVAL, fade_callback, [led]).start()


def fade(led):
    threading.Timer(FADE_INTERVAL, fade_callback, [led]).start()

