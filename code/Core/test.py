# main game logic here
# other files just import

#import pokemon_battle as pokemon_battle
#import twoD as td

import helper_functions
import settings

import pygame
import os
import enum

pygame.init()


# setup  

size = (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
fps = settings.FPS
vel = settings.PLAYER_SPEED
screen_full = settings.FULLSCREEN

clock = pygame.time.Clock()

screen = pygame.display.set_mode(size, pygame.RESIZABLE)
pygame.display.set_caption(settings.TITLE)
pygame.mouse.set_visible(0)


# images
bg = pygame.image.load(os.path.join(*settings.BG_PATH)).convert() # this is just for now later we need a bg with a resoultion of (4096, 4096)
bg_scaled = helper_functions.rescale(bg, 500, 500)


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        img = pygame.image.load(os.path.join(*settings.PLAYER_PATH)).convert_alpha()
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()


# player
player = Player()  

player.rect.x = 0  
player.rect.y = 0 
player_x = float(player.rect.x)
player_y = float(player.rect.y)

width = player.rect.width
height = player.rect.height

vel = 150

player_list = pygame.sprite.Group()
player_list.add(player)



# main_loop    

frame_count = 0
dt = 0
running = True
    
while running:


    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.VIDEORESIZE and pygame.version.vernum[0] < 2:
            size = (event.w, event.h)
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            bg_scaled = helper_functions.rescale(bg, event.w, event.h)

        # full_screen_toggle

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                screen_full = not screen_full

                if screen_full:
                    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                    bg_scaled = helper_functions.rescale(bg, screen.get_width(), screen.get_height())
                else:
                    screen = pygame.display.set_mode(size, pygame.RESIZABLE)
                    bg_scaled = helper_functions.rescale(bg, size[0], size[1])


    # screen updating

    screen_width = screen.get_width()
    screen_height = screen.get_height()

    if (screen_width, screen_height) != bg_scaled.get_size():
        bg_scaled = helper_functions.rescale(bg, screen_width, screen_height)

    # keyboard_presses    

    keys = pygame.key.get_pressed()

    # keyboard_movement_checks 
        


    if keys[pygame.K_w] and player_y > 0:
        player_y -= vel * dt

    if keys[pygame.K_a] and player_x > 0:
        player_x -= vel * dt

    if keys[pygame.K_s] and player_y < screen_height - height:
        player_y += vel * dt

    if keys[pygame.K_d] and player_x < screen_width - width:
        player_x += vel * dt


    # player_repositon
    player_x = max(0, min(player_x, screen_width - width))
    player_y = max(0, min(player_y, screen_height - height))

    player.rect.x = round(player_x) 
    player.rect.y = round(player_y)

    
    screen.blit(bg_scaled, (0, 0))

    frame_count += 1
    if frame_count % 30 == 0:
        pygame.display.set_caption(f"{settings.TITLE} | FPS: {round(clock.get_fps())}") # fps counter yayy

    #pygame.draw.rect(screen, (255, 0, 0), (round(player.rect.x), round(player.rect.y), width, height))
    player_list.draw(screen)
    pygame.display.update()
    dt = clock.tick(fps) / 1000


pygame.quit()