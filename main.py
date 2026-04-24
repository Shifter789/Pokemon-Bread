# main game logic here
# other files just import

import pokemon
import pokemon_battle
import pygame


pygame.init()

# frames_setup    

size=[500,500]
clock = pygame.time.Clock()
fps = 75

# screen_setup    

screen = pygame.display.set_mode(size, pygame.RESIZABLE)
screen_full = False

#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

pygame.display.set_caption("Title_holder")

# movement    

chr_x = 50
chr_y = 50
width = 40
height = 40
vel = 3

# main_loop    

running = True
    
while running:

    pygame.time.delay(10)


    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.VIDEORESIZE:
            size = [event.w, event.h]
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

        # full_screen_toggle
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                screen_full = not screen_full

                if screen_full:
                    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode(size, pygame.RESIZABLE)

    # screen updating
    screen_width = screen.get_width()
    screen_height = screen.get_height()

    # keyboard_presses    

    keys = pygame.key.get_pressed()

        # keyboard_movement_checks 
        
    if keys[pygame.K_w] and chr_y > 0:
        chr_y -= vel

    if keys[pygame.K_a] and chr_x > 0:
        chr_x -= vel

    if keys[pygame.K_s] and chr_y < screen_height - height:
        chr_y += vel

    if keys[pygame.K_d] and chr_x < screen_width - width:
        chr_x += vel


    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255, 0, 0), (chr_x, chr_y, width, height))
    pygame.display.update()
    clock.tick(fps)


pygame.quit