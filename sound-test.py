#!/usr/bin/python3

import pygame
import time

pygame.mixer.init()
pygame.mixer.music.load("sounds/happy.mp3")
pygame.mixer.music.play()

print("playing")

time.sleep(3)

pygame.mixer.music.stop()

print("exiting")
