import pygame
import helper_functions

# screen
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
TITLE = "Pokemon Green Apatite"
FULLSCREEN = False

# performance
FPS = helper_functions.get_monitor_refresh_rate() + 10
#FPS = helper_functions.get_monitor_refresh_rate()
#FPS = 120

# player
PLAYER_SPEED = 155

# assestets
BG_PATH_SPLASH = ("assets", "Splash", "Bg_Splash.png" )
BG_PATH_OVERWORLD = ("assets", "map", "world.png")
PLAYER_PATH = ("assets", "sprites", "Player.png")

# colors
BLACK = (0,   0,   0  )
WHITE = (255, 255, 255)

# controls
KEY_UP       = "w"
KEY_DOWN     = "s"
KEY_LEFT     = "a"
KEY_RIGHT    = "d"
KEY_FULLSCREEN = "F11"
