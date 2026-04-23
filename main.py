# main game logic here
# other files just import

import pokemon
import pokemon_battle
import pygame

pygame.init()


#frames setup
clock = pygame.time.Clock()
fps = 75

#screen setup
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Title_holder")

#movement
test_x = 50
test_y = 50
width = 40
height = 60
vel = 5

#main_loop

running = True
    
while running:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #keyboard presses

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        test_y -= vel

    if keys[pygame.K_a]:
        test_x -= vel

    if keys[pygame.K_s]:
        test_y += vel

    if keys[pygame.K_d]:
        test_x += vel


    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255, 0, 0), (test_x, test_y, width, height))
    pygame.display.update()
    clock.tick(fps)

pygame.quit

