import pygame
import time
import random

pygame.init()

class Dino:
    def __init__(self):
        self.RED = (255, 0, 0)
        self.BLUE = (0, 0, 255)
        self.display = pygame.display.set_mode((400, 300))
        
        pygame.draw.rect(self.display, self.BLUE, pygame.Rect(90, 30, 60, 120))
        pygame.draw.rect(self.display, self.RED, pygame.Rect(30, 30, 60, 120))
        pygame.display.flip()

Test = Dino()
