import pygame
from settings import *

class Snake:
    def __init__(self):
        self.size =10
        self.body = [[100, 50], [90, 50], [80, 50]]
        self.direction = pygame.RIGHT

    def move(self):
        head_x, head_y = self.body[0]
        if self.direction == pygame.K_RIGHT:
            head_x += self.size
        elif self.direction == pygame.K_LEFT:
            head_x -= self.size
        elif self.direction == pygame.K_UP:
            head_y -= self.size
        elif self.direction == pygame.K_DOWN:
            head_y += self.size

        new_head = (head_x, head_y)
        self.body = [new_head] + self.body[:-1]

    def grow(self):
        self.body.append(self.body[-1])

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (*segment, self.size, self.size))