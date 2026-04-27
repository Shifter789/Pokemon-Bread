# main game logic here
# other files just import

#import pokemon_battle as pokemon_battle
import helper_functions
import twoD as td
import pygame
import os

pygame.init()

# frames_setup    
size = (500, 500)
clock = pygame.time.Clock()


# screen_setup    

screen = pygame.display.set_mode(size, pygame.RESIZABLE)
screen_full = False


fps = helper_functions.get_monitor_refresh_rate()

#fps = 120

pygame.display.set_caption("Pokemon Green Apatite")
pygame.mouse.set_visible(0)


# images
bg = pygame.image.load(os.path.join("assets", "map", "world.png")).convert() # this is just for now later we need a bg with a resoultion of (4096, 4096)
bg_scaled = helper_functions.rescale(bg, 500, 500)


# movement    

chr_x = 50.0
chr_y = 50.0

width = 40
height = 40

vel = 300

# main_loop    

frame_count = 0
dt = 0
running = True
    
while running:


    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.VIDEORESIZE:
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

    # keyboard_presses    

    keys = pygame.key.get_pressed()

    # keyboard_movement_checks 
        
    if keys[pygame.K_w] and chr_y > 0:
        chr_y -= vel * dt

    if keys[pygame.K_a] and chr_x > 0:
        chr_x -= vel * dt

    if keys[pygame.K_s] and chr_y < screen_height - height:
        chr_y += vel * dt

    if keys[pygame.K_d] and chr_x < screen_width - width:
        chr_x += vel * dt


    # player_repositon
    if chr_x > screen_width - width:
        chr_x = screen_width - width

    if chr_y > screen_height - height:
        chr_y = screen_height - height

    
    screen.blit(bg_scaled, (0, 0))

    frame_count += 1
    if frame_count % 30 == 0:
        pygame.display.set_caption(f"Pokemon Green Apatite | FPS: {round(clock.get_fps())}") # fps counter yayy

    pygame.draw.rect(screen, (255, 0, 0), (round(chr_x), round(chr_y), width, height))

    pygame.display.update()
    dt = clock.tick(fps) / 1000


pygame.quit()