import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self, groups, pos, laser_surf):
        super().__init__(groups)
        self.image =laser_surf
        self.rect = self.image.get_frect(midbottom = pos)
        self.speed = 400
    
    def update(self,dt):
        self.rect.centery -= dt * self.speed 
        if self.rect.bottom < 0:
            self.kill()
        