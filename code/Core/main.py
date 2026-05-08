#import pokemon_battle as pokemon_battle
#import twoD as td

import helper_functions
import settings

import pygame
import os
import enum

# state machine
class GameState(enum.Enum):

    SPLASH = "splash"
    MENU = "main_menu"
    OVERWORLD = "overworld"
    BATTLE = "battle"
    PAUSE_MENU = "pause_menu"

state = GameState.SPLASH

# inits
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

icon = pygame.image.load(os.path.join(*settings.ICON)).convert_alpha()
pygame.display.set_icon(icon)


#splash images
bg_splash = pygame.image.load(os.path.join(*settings.BG_PATH_SPLASH)).convert()
bg_splash_scaled = helper_functions.rescale(bg_splash, 500, 500)

#menu images
button_unclicked = pygame.image.load(os.path.join(*settings.MENU_BUTTON_UNCLICKED)).convert_alpha()
button_unclicked_scaled = helper_functions.rescale(button_unclicked, 500, 500)

#overworld images
bg_overworld = pygame.image.load(os.path.join(*settings.BG_PATH_OVERWORLD)).convert() # this is just for now later we need a bg with a resoultion of (4096, 4096)
bg_overworld_scaled = helper_functions.rescale(bg_overworld, 500, 500)


# player class
class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        img = pygame.image.load(os.path.join(*settings.PLAYER_PATH)).convert_alpha()
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

# player setup
player = Player()  

# player movement
player.rect.x = 0  
player.rect.y = 0 
player_x = float(player.rect.x)
player_y = float(player.rect.y)

#player config
width = player.rect.width
height = player.rect.height

#players
player_list = pygame.sprite.Group()
player_list.add(player)

 
#functions
def handle_events(event, state):

    global size, screen_full, screen, bg_splash_scaled, bg_overworld_scaled

    if state == GameState.SPLASH:

        if event.type == pygame.VIDEORESIZE and pygame.version.vernum[0] < 2:
            size = event.w, event.h
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            bg_splash_scaled = helper_functions.rescale(bg_splash, event.w, event.h)


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                screen_full = not screen_full

                if screen_full:
                    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
                    bg_splash_scaled = helper_functions.rescale(bg_splash, screen.get_width(), screen.get_height())


                else:
                    screen = pygame.display.set_mode(size, pygame.RESIZABLE)
                    bg_splash_scaled = helper_functions.rescale(bg_splash, size[0], size[1])


            if event.key == pygame.K_RETURN:
                return GameState.MENU
    
    elif state == GameState.MENU:
        
        if event.type == pygame.VIDEORESIZE and pygame.version.vernum[0] < 2:
            size = event.w, event.h
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return GameState.OVERWORLD
    
    elif state == GameState.OVERWORLD:

        if event.type == pygame.VIDEORESIZE and pygame.version.vernum[0] < 2:
                size = (event.w, event.h)
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                bg_overworld_scaled = helper_functions.rescale(bg_overworld, event.w, event.h)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                screen_full = not screen_full

                if screen_full:
                    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                    bg_overworld_scaled = helper_functions.rescale(bg_overworld, screen.get_width(), screen.get_height())

                else:
                    screen = pygame.display.set_mode(size, pygame.RESIZABLE)
                    bg_overworld_scaled = helper_functions.rescale(bg_overworld, size[0], size[1])

    return state

def input(state, dt):

    if state == GameState.SPLASH:

        pass

    elif state == GameState.MENU:

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]:
            print("w")
        if keys[pygame.K_s]:
            print("s")

    elif state == GameState.OVERWORLD:

        global player_x, player_y, frame_count, screen_width, screen_height

        keys = pygame.key.get_pressed()

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

        frame_count += 1
        if frame_count % 30 == 0:
            pygame.display.set_caption(f"{settings.TITLE} | FPS: {round(clock.get_fps())}") # fps counter yayy

    return state

def draw(screen, state):

    if state == GameState.SPLASH:

        screen.blit(bg_splash_scaled, (0, 0))

        font_size = screen.get_width() // 30
        scaled_font = pygame.font.Font(*settings.FONT[:-1], font_size)
        splash_intro_text = scaled_font.render("Enter to begin the journey :)", True, (255, 255, 255))

        text_x = (screen.get_width() - splash_intro_text.get_width()) // 2
        text_y = int((screen.get_height() - splash_intro_text.get_height()) // 1.8)

        screen.blit(splash_intro_text, (text_x, text_y))

    elif state == GameState.MENU:
        
        screen.fill((150, 150, 150))

        button_gap = int(button_unclicked_scaled.get_height() // 1.99)

        button_1_x = int((screen.get_width() - button_unclicked_scaled.get_width()) / 2)
        button_1_y = screen.get_height() // 900

        button_2_x = int((screen.get_width() - button_unclicked_scaled.get_width()) / 2)
        button_2_y = button_1_y + button_gap

        button_3_x = int((screen.get_width() - button_unclicked_scaled.get_width()) / 2)
        button_3_y = button_2_y + button_gap

        screen.blit(button_unclicked_scaled, (button_1_x, button_1_y))
        screen.blit(button_unclicked_scaled, (button_2_x, button_2_y))
        screen.blit(button_unclicked_scaled, (button_3_x, button_3_y))

        font_size = screen.get_width() // 30
        scaled_font = pygame.font.Font(*settings.FONT[:-1], font_size)

        New_game_text = scaled_font.render("New Game", True, (0, 0, 0))
        Load_game_text = scaled_font.render("Load game", True, (0, 0, 0))
        Settings_text = scaled_font.render("Settings", True, (0, 0, 0))
        
        New_game_text_x = button_1_x + (button_unclicked_scaled.get_width() - New_game_text.get_width()) // 2
        New_game_text_y = button_1_y + (button_unclicked_scaled.get_height() - New_game_text.get_height()) // 2.3
        Load_game_text_x = button_2_x + (button_unclicked_scaled.get_width() - Load_game_text.get_width()) // 2
        Load_game_text_y = button_2_y + (button_unclicked_scaled.get_height() - Load_game_text.get_height()) // 2.3
        Settings_text_x = button_3_x + (button_unclicked_scaled.get_width() - Settings_text.get_width()) // 2
        Settings_text_y = button_3_y + (button_unclicked_scaled.get_height() - Settings_text.get_height()) // 2.3

        screen.blit(New_game_text, (New_game_text_x, New_game_text_y))
        screen.blit(Load_game_text, (Load_game_text_x, Load_game_text_y))
        screen.blit(Settings_text, (Settings_text_x, Settings_text_y))




    elif state == GameState.OVERWORLD:

        screen.blit(bg_overworld_scaled, (0, 0))
        player_list.draw(screen)


    pass


# pre setup
frame_count = 0
dt = 0
running = True 

#loop start
while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        state = handle_events(event, state)

    screen_width = screen.get_width()
    screen_height = screen.get_height()

    button_width = screen_width // 3
    button_height = int(screen_height // 1.8)

    if (screen_width, screen_height) != bg_splash_scaled.get_size():
        bg_splash_scaled = helper_functions.rescale(bg_splash, screen_width, screen_height)

    if (button_width, button_height) != button_unclicked_scaled.get_size():
        button_unclicked_scaled = helper_functions.rescale(button_unclicked, button_width, button_height)

    if (screen_width, screen_height) != bg_overworld_scaled.get_size():
        bg_overworld_scaled = helper_functions.rescale(bg_overworld, screen_width, screen_height)

    state = input(state, dt)

    draw(screen, state)
    

    pygame.display.update()
    dt = clock.tick(fps) / 1000

pygame.quit()