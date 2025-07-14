import pygame
import random

class Meteor(pygame.sprite.Sprite):
    def __init__(self, groups, surf):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center = (random.randint(80,1000),-100))
        self.current_time = pygame.time.get_ticks()
        self.speed = 150
        self.direction = pygame.math.Vector2(random.uniform(-0.5,0.5),1)
        
    def update(self,dt):
        if self.rect.left<=0 or self.rect.right>=1280:
            self.direction.x *= -1
        self.direction.normalize()
        self.rect.center += self.direction * self.speed * dt
        if self.rect.bottom > 720:
            self.kill()
    