import pygame
from os.path import join

from Player import Player
from Meteor import Meteor

pygame.init()

WINDOW_WIDTH,WINDOW_HEIGHT = 1280,720
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('SpaceShooter')
running = True

clock = pygame.time.Clock() 

Player_surf = pygame.image.load(join("images","shooter.png")).convert_alpha()
meteor_surf = pygame.transform.scale(pygame.image.load(join("images","astroid.png")).convert_alpha(),(150,150))

score = 0 
font = pygame.font.Font(None,40)

all_sprites = pygame.sprite.Group()
meteor_sprites = pygame.sprite.Group()
player = Player(all_sprites,WINDOW_HEIGHT, Player_surf,WINDOW_WIDTH)


meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 2000)

def update_score(score):
    font_surf = font.render(str(score),True, "red")
    return font_surf

while running:
    dt = clock.tick() / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == meteor_event:
            Meteor((all_sprites,meteor_sprites), meteor_surf)

    all_sprites.update(dt)
    if pygame.sprite.spritecollide(player,meteor_sprites,False):
        running = False
    
    for laser in player.laser_sprites:
        if pygame.sprite.spritecollide(laser,meteor_sprites,True):
            score+=1
            laser.kill()

    
    display_surface.fill('gray')
    all_sprites.draw(display_surface)

    display_surface.blit(update_score(score),(WINDOW_WIDTH - 100,10))
    pygame.display.update()


pygame.quit()