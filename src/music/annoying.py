import pygame
import time

pygame.init()

while True:
    input("press enter to continue")

    pygame.mixer.music.load("../music/alarm.mp3")
    pygame.mixer.music.play()
    time.sleep(10)
