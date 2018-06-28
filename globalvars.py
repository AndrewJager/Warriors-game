#global variables
import pygame

gravity = 2
speed = 3
onground = True

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (25,25,225)

# Screen dimensions
SCREEN_WIDTH  = 1080
SCREEN_HEIGHT = 600

BaseSpeed = 3
RunSpeed = 6
JumpBoost = 30

# Player controls (made as variables so I can make an interface to remap them later)
KeyRight = pygame.K_LEFT
KeyLeft = pygame.K_RIGHT
KeyUp = pygame.K_UP
KeyDown = pygame.K_DOWN
KeyCtrl = pygame.K_LCTRL
KeyShift = pygame.K_LSHIFT


KEYCOLOR = (164,117,160)