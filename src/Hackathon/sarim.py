import pygame
import time
import random
import os
import sys
import math


pygame.init()

bg = pygame.image.load(os.path.join('images','bg.png')).convert()
bgX = 0
bgX2 = bg.get_width()

run = True
speed = 30  # NEW

while run:
    clock.tick(speed)  # NEW
    bgX -= 1.4  # Move both background images back
    bgX2 -= 1.4

    if bgX < bg.get_width() * -1:  # If our bg is at the -width then reset its position
        bgX = bg.get_width()
    
    if bgX2 < bg.get_width() * -1:
        bgX2 = bg.get_width()

    for event in pygame.event.get():  
        if event.type == pygame.QUIT: 
            run = False    
            pygame.quit() 
            quit()

width = 650
height = 750

pixel = 64

screen = pygame.display.set_mode((width,height))
cactus = pygame.image.load("cactus.png")

playerimage = pygame.image.load("dino4python.png")

playerxposition = (width/2) - (pixel/2)
playerxpositionCHANGE = 0
playeryposition = height-pixel-10

cactusxposition = random.randint(0, (width - pixel))

pygame.display.flip()
