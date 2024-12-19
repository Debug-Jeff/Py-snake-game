import pygame
import random
from settings import *

class Food:
    def __init__(self):
        self.size = 10
        self.position = self.random_position()

    def random_position(self):
        x = random.randint(0, (SCREEN_WIDTH - self.size) // self.size) * self.size
        y = random.randint(0, (SCREEN_HEIGHT - self.size) // self.size) * self.size
        return (x, y)

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (*self.position, self.size, self.size))