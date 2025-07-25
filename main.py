import pygame
from os.path import join
import sys

from Player import Player
from Meteor import Meteor

pygame.init()

WINDOW_WIDTH,WINDOW_HEIGHT = 1280,720
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('SpaceShooter')
running = True

clock = pygame.time.Clock() 

# Load images with error handling
try:
    Player_surf = pygame.image.load(join("Images","shooter.png")).convert_alpha()
    meteor_surf = pygame.transform.scale(pygame.image.load(join("Images","astroid.png")).convert_alpha(),(150,150))
except pygame.error as e:
    print(f"Error loading images: {e}")
    print("Make sure the Images folder contains: shooter.png, astroid.png, laser.png")
    pygame.quit()
    sys.exit()

score = 0 
previous_score = -1
font = pygame.font.Font(None,40)
score_surf = font.render("0", True, "red")
score_rect = score_surf.get_frect(left=WINDOW_WIDTH - 100,top=20)

all_sprites = pygame.sprite.Group()
meteor_sprites = pygame.sprite.Group()
player = Player(all_sprites,WINDOW_HEIGHT, Player_surf,WINDOW_WIDTH)


meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 2000)

while running:
    dt = clock.tick() / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == meteor_event:
            Meteor((all_sprites,meteor_sprites), meteor_surf, WINDOW_WIDTH, WINDOW_HEIGHT)

    all_sprites.update(dt)
    if pygame.sprite.spritecollide(player,meteor_sprites,False,pygame.sprite.collide_mask):
        running = False
    
    for laser in player.laser_sprites:
        if pygame.sprite.spritecollide(laser,meteor_sprites,True, pygame.sprite.collide_mask):
            score+=1
            laser.kill()

    # Only update score surface when score changes
    if score != previous_score:
        score_surf = font.render(str(score), True, "red")
        previous_score = score
    
    display_surface.fill('gray')
    all_sprites.draw(display_surface)
    display_surface.blit(score_surf, score_rect)
    pygame.draw.rect(display_surface,"red",score_rect.inflate(20,20),2)
    pygame.display.update()


pygame.quit()
