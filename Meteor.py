import pygame
import random

class Meteor(pygame.sprite.Sprite):
    def __init__(self, groups, surf, window_width=1280, window_height=720):
        super().__init__(groups)
        self.image = surf
        self.window_width = window_width
        self.window_height = window_height
        self.rect = self.image.get_frect(center = (random.randint(80, self.window_width - 80), -100))
        self.speed = 150
        self.direction = pygame.math.Vector2(random.uniform(-0.5,0.5),1)
        
    def update(self,dt):
        if self.rect.left<=0 or self.rect.right>=self.window_width:
            self.direction.x *= -1
        self.direction.normalize()
        self.rect.center += self.direction * self.speed * dt
        if self.rect.bottom > self.window_height:
            self.kill()
