import pygame
import helper_functions

# screen
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

TITLE = "Pokemon Green Apatite"
ICON = ("assets", "sprites", "icon.png")

FONT = ('freesansbold.ttf', 24)

FULLSCREEN = False

# performance
FPS = helper_functions.get_monitor_refresh_rate() + 10
#FPS = helper_functions.get_monitor_refresh_rate()
#FPS = 120

# player
PLAYER_SPEED = 155

# assets

#splash
BG_PATH_SPLASH = ("assets", "Splash", "Bg_Splash.png" )

#menu
MENU_BUTTON_UNCLICKED = ("assets", "Menu", "Button_unclicked.png")

#overworld
BG_PATH_OVERWORLD = ("assets", "map", "world.png")

#misc
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
