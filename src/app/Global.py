# FILE CONTAINS GLOBAL VALUES USED THROUGHT THE PROGRAM

# imports
import pygame
from screeninfo import get_monitors

# constants
MONITOR = get_monitors()[0]
MONITOR_RESOLUTION = (MONITOR.width, MONITOR.height)
SCREEN_SIZE = MONITOR_RESOLUTION
SCREEN = pygame.display.set_mode(SCREEN_SIZE)
FPS = 60
CLOCK = pygame.time.Clock()
BG_COLOR = (38, 37, 34)
BUTTON_COLOR = (255, 255, 255)
BUTTON_COLOR_HOVER = (38, 37, 34)
TEXT_COLOR = (38, 37, 34)
TEXT_COLOR_HOVER = (255, 255, 255)