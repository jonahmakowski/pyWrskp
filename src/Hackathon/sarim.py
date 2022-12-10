import pygame
import time
import random

pygame.init()

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