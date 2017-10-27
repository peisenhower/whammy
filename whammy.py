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
    "sounds/haltales.mp3",
    "sounds/psychoz.mp3",
    "sounds/thisishalloween3.mp3"
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
    pygame.mixer.music.load(MUSIC_LIST[random.randint(0,5)])
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

def non_repeating_random(num):
    val = random.randint(1,9)
    while val == num:
        val = random.randint(1,9)
    return val

def check_win(pin):
    if pin == 1 or pin == 3 or pin == 4 or pin == 6 or pin == 8:
        return 1
    if pin == 2 or pin == 7:
        return 2
    if pin == 5 or pin == 9:
        return 3

def main():
    count = 0 #slows down the loop
    pin = 0 #pin number of LED to light
    idle()
    while True:
        count+=1

        #start the game sequence
        if is_button_pressed() == 0:
            print(game_state)
            if game_state == "idle":
                game()
                sound("laugh")
            
            #check results of game
            elif game_state == "game":
                print("pressed from game")
                if check_win(pin) == 1:
                    #normal win
                    print("normal: "+str(pin))
                elif check_win(pin) == 2:
                    #double win
                    print("double: "+str(pin))
                elif check_win(pin) == 3:
                    #whammy
                    print("whammy: "+str(pin))
                time.sleep(1)
                idle()
                
            time.sleep(.5)

        #Game blinks at higher rate
        if count == 25 or count == 50 or count == 75:
            if game_state == "game":
                pin = non_repeating_random(pin)
                print("blink "+str(pin))
                led.blink(pin)

        if count > 100:
            count = 0

            #once ambient sound complete and state is idle pick another song
            if pygame.mixer.music.get_busy() == 0 and game_state == "idle":
                music()

            #depending on state blink lights
            if game_state == "game":
                pin = non_repeating_random(pin)
                print("blink "+ str(pin))
                led.blink(pin)
            elif game_state == "idle":
                pin = non_repeating_random(pin)
                print("fade "+str(pin))
                led.fade(pin)
        time.sleep(.01) #slow loop down a bit

if __name__ == "__main__":
    pygame.mixer.init()
    button_setup()
    main()
