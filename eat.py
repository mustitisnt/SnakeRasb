import pygame
import random
pygame.init()
white = (255, 255, 255)

class eat:
    def __init__(self, screen, h, w):
        self.speed = 2
        self.size = 50
        self.length = 1
        self.direction = 1  # dann eben 1, 2, 3, 4
        self.nextDirection = 1
        self.x = random.randint(0, 7) * 50
        self.y = random.randint(0, 7) * 50
        self.screen = screen
        self.h = h
        self.w = w
    def draw(self):
        pygame.draw.rect(self.screen, white, (self.x, self.y, self.size, self.size))
