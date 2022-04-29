import pygame
import random

class Particle:

    def __init__(self, x, y, WIN):
        self.x = x 
        self.y = y 
        self.vy = 0
        self.vx = 0
        self.ay = 0
        self.ax = 0
        self.WIN = WIN
        self.speed = 6
        self.color = (201, 67, 0)
        self.timer = 0

        while self.vx == 0:
            self.vx = random.randint(-self.speed, self.speed)

        while self.vy == 0:
            self.vy = random.randint(-self.speed, self.speed)

        if self.vx < 0:
            self.ax = random.uniform(0.2, 0.4)
        elif self.vx > 0:
            self.ax = -random.uniform(0.2, 0.4)

        if self.vy < 0:
            self.ay = random.uniform(0.2, 0.4)
        elif self.vy > 0:
            self.ay = -random.uniform(0.2, 0.4)


    def draw(self):
            rect = pygame.Rect(self.x, self.y, 7, 7)
            pygame.draw.rect(self.WIN, self.color, rect)
            rect.move(self.x, self.y)

    def update(self):
        if self.vy + self.ay > 0:
            if self.vy > 0:
                self.vy += self.ay
            elif self.vy < 0:
                self.vy = 0
        elif self.vy + self.ay < 0:
            if self.vy > 0:
                self.vy = 0
            elif self.vy < 0:
                self.vy += self.ay
        elif self.vy + self.ay == 0:
            self.vy = 0

        self.y += self.vy 

        if self.vx + self.ax > 0:
            if self.vx > 0:
                self.vx += self.ax
            elif self.vx < 0:
                self.vx = 0
        elif self.vx + self.ax < 0:
            if self.vx > 0:
                self.vx = 0
            elif self.vx < 0:
                self.vx += self.ax
        elif self.vx + self.ax == 0:
            self.vx = 0

        self.x += self.vx

        if self.timer == 120*3:
            self.color = (200, 200, 200)
        else:
            self.timer += 1