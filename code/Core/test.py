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

vel = settings.PLAYER_SPEED

player_list = pygame.sprite.Group()
player_list.add(player)


# main_loop    

frame_count = 0
dt = 0
running = True
    
class GameState(enum.Enum):
    SPLASH = "splash"
    MAIN_MENU = "main_menu"
    SETTINGS = "settings"
    NAME_ENTRY = "name_entry"
    OVERWORLD = "overworld"
    BATTLE = "battle"
    DIALOGUE = "dialogue"
    PAUSE_MENU = "pause_menu"
    GAME_OVER = "game_over"

state = GameState.SPLASH


