#!/usr/bin/python3


# import RPi.GPIO as GPIO
import pygame
import time
import threading
import led

MUSIC_TABLE = {
    "happy-halloween" : "sounds/happy.mp3",
    "laugh": "sounds/laugh.mp3"
}

BUTTON_PIN = 17 # Broadcom pin 17 (P1 pin 11)

# def button_setup():
#     GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def is_button_pressed():
    return False
#     # button is low when pressed
#     return !GPIO.input(BUTTON_PIN)


def music(name):
    pygame.mixer.music.fadeout(1)
    pygame.mixer.music.load(MUSIC_TABLE[name])
    pygame.mixer.music.play()


def game():
    pass

def idle():
    # play idle music
    pass

def main():
    count = 0
    while True:
        if is_button_pressed():
            game()
        # music("laugh")
        print("playing laugh")
        time.sleep(2)
        # break
        count += 1

        led.fade(count)

        if count > 3:
            return

if __name__ == "__main__":
    pygame.mixer.init()
    main()