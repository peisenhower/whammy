#!/usr/bin/python3


import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
import pygame
import time
import threading
import led
import random

SOUNDS_TABLE = {
    "happy-halloween" : "sounds/happy.mp3",
    "laugh": "sounds/laugh.mp3"
}
MUSIC_LIST = [
    "sounds/add_famwltz.mp3",
    "sounds/creepy.mp3",
    "sounds/ghosts.mp3",
    "sounds/halloween.mp3",
    "sounds/haltales.mp3",
    "sounds/inslcy.mp3",
    "sounds/psychoz.mp3"
]

BUTTON_PIN = 17 # Broadcom pin 17 (P1 pin 11)
game_state = ""

def button_setup():
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def is_button_pressed():
    # button is low when pressed
    return GPIO.input(BUTTON_PIN)


def sound(name):
    pygame.mixer.music.fadeout(1)
    pygame.mixer.music.load(SOUNDS_TABLE[name])
    pygame.mixer.music.play()
def music():
    pygame.mixer.music.fadeout(1)
    pygame.mixer.music.load(MUSIC_LIST[random.randint(0,6)])
    pygame.mixer.music.play()

def game():
    print("game on")
    global game_state
    game_state = "game"

def idle():
    global game_state
    game_state = "idle"
    print("going idle")
    music()

def main():
    count = 0
    idle()
    while True:
        count+=1
        if is_button_pressed() == 0:
            print(game_state)
            if game_state == "idle":
                game()
                sound("laugh")
                
            elif game_state == "game":
                print("pressed from game")
                idle()
                
            time.sleep(.5)
        #led.fade(count)
        if count > 100:
            count = 0
            #print(game_state)
            if pygame.mixer.music.get_busy() == 0 and game_state == "idle":
                music()
        time.sleep(.01)

if __name__ == "__main__":
    pygame.mixer.init()
    button_setup()
    main()
