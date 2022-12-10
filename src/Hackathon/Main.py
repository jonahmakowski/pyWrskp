import pygame
import time
import random

pygame.init()

class Dino:
    def __init__(self):
        self.RED = (255, 0, 0)
        self.BLUE = (0, 0, 255)
        self.screen = pygame.display.set_mode([1375,750])
        redRectangle = pygame.Rect((0, 0), (50, 50))
        blueRectangle = pygame.Rect((0, 0), (50, 50))
        pygame.draw.rect(screen, self.RED, redRectangle)
        pygame.draw.rect(screen, self.BLUE, blueRectangle)
        pygame.display.update()

Test = Dino()
