import pygame, sys
from spritesheet import Player, Wall
from clan import Clan
from Namegen import *
from cat import Cat
from pygame.locals import *
from PIL import Image
from globalvars import *

EveryCat = []

kitty = Cat(6,'Kit')
#kitty.Setup()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)

warriors = 2
WindClan = Clan("WindClan",warriors,EveryCat)
#WindClan.AddCat(kitty,"Apprentice",EveryCat)
#WindClan.SayCats()
#WindClan.ChooseMentor(kitty)
ThunderClan = Clan("ThunderClan",warriors+10,EveryCat)
#ThunderClan.SayCats()
ShadowClan = Clan("ShadowClan",0,EveryCat)#ShadowClan is dead
#ShadowClan.SayCats()
RiverClan = Clan("RiverClan",warriors,EveryCat)
#RiverClan.SayCats()
#SkyClan isn't a real clan

I=0
while I < len(EveryCat):
    print (EveryCat[I].SayRank() + ": " + EveryCat[I].SayName())
    I=I + 1



run = True
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)
gray = (200,200,200)
player = pygame.Rect(100,100,300,150)
playerspeed = 2
jump = False
Gravity = 1
ground = pygame.Rect(10,400,1000,10)
evil = pygame.image.load('cat.png')

'''
#sprite testing
cat = Image.open("cat.png")
pix=cat.load()
value = (45, 35, 65, 255)
background = (255, 255, 255, 0)
keyvalue = (56,56,56,255)
keyvalue2 = (164, 117, 160, 255)
I = 0
II = 0
while I < 274:
    II = 0
    while II < 100:
        if pix[I,II] == keyvalue:#key cat
            pix[I,II] = value
        if pix[I,II] == keyvalue2:#key background
            pix[I,II] = background
        II = II + 1
    I= I+1
cat.show()
'''

# List to hold all the sprites
all_sprite_list = pygame.sprite.Group()
 
# Make the walls. (x_pos, y_pos, width, height)
wall_list = pygame.sprite.Group()
 
wall = Wall(0, 0, 10, 600)
wall_list.add(wall)
all_sprite_list.add(wall)
 
wall = Wall(10, 0, 790, 10)
wall_list.add(wall)
all_sprite_list.add(wall)
 
wall2 = Wall(30, 300, 1000, 10)
wall_list.add(wall2)
all_sprite_list.add(wall2)
 
# Create the player paddle object
player = Player(50, 50,(135,135,135))
player.walls = wall_list
all_sprite_list.add(player)

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption('Warriors')

def getKey(key):
    return pygame.key.get_pressed()[eval("pygame.K_"+key)]
imagey = 20
imagex = 20
#main loop
done = False
while not done:
    if onground == True:
        gravity = 0
    else:
        gravity = gravity + 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
       
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-speed, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(speed, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -speed)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, speed)
 
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(speed, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-speed, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, gravity)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -speed)
                
 
    all_sprite_list.update()
    print(gravity)
    screen.fill(BLACK)
 
    all_sprite_list.draw(screen)
 
    pygame.display.flip()
 
    clock.tick(60)
pygame.quit() # Quits the window

