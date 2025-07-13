import pygame
from os.path import join
from Laser import Laser

class Player(pygame.sprite.Sprite):
    def __init__(self, groups,WINDOW_HEIGHT, player_surf, WINDOW_WIDTH):
        super().__init__(groups)
        self.group = groups
        self.WINDOW_HEIGHT=WINDOW_HEIGHT
        self.WINDOW_WIDTH=WINDOW_WIDTH
        self.direction = pygame.math.Vector2()
        self.speed = 300
        self.image = player_surf
        self.rect = self.image.get_frect(bottomleft = (20,WINDOW_HEIGHT - 20))
        self.cooldown_time = 400
        self.last_laser_time = 0
        self.can_fire = True
        self.laser_sprites = pygame.sprite.Group()
        self.laser_surf = pygame.transform.scale(pygame.image.load(join("images","laser.png")).convert_alpha(),(50,50))

    def update_laser_cooldown(self):
        if not self.can_fire:
            game_time = pygame.time.get_ticks()
            if game_time - self.last_laser_time >= self.cooldown_time:
                self.can_fire = True
   
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT] or keys[pygame.K_d]) - int(keys[pygame.K_LEFT] or keys[pygame.K_a])
        self.direction.y = int(keys[pygame.K_DOWN] or keys[pygame.K_s]) - int(keys[pygame.K_UP] or keys[pygame.K_w])
        if self.direction.x != 0 or self.direction.y != 0:
            self.direction = self.direction.normalize()
        self.rect.center += self.direction * self.speed * dt

        if self.rect.left<=0:
            self.rect.left = 0
        if self.rect.right >= self.WINDOW_WIDTH:
            self.rect.right = self.WINDOW_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= self.WINDOW_HEIGHT:
            self.rect.bottom = self.WINDOW_HEIGHT

        if keys[pygame.K_SPACE] and self.can_fire:
            Laser((self.group,self.laser_sprites), self.rect.midtop, self.laser_surf)
            self.last_laser_time = pygame.time.get_ticks()
            self.can_fire = False

        self.update_laser_cooldown()
