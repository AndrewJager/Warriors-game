import pygame, sys
from clan import Clan
from Namegen import *
from cat import Cat
from pygame.locals import *
from PIL import Image

EveryCat = []

kitty = Cat(6,'kit')
kitty.Setup()
kitty.Ceramony("Apprentice")

warriors = 10
WindClan = Clan("WindClan",warriors,EveryCat)
WindClan.AddCat(kitty,"Apprentice",EveryCat)
#WindClan.SayCats()
WindClan.ChooseMentor(kitty)
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
ground = pygame.Rect(100,100,1000,10)
#evil = pygame.image.load('cat.png')

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
#cat.show()
'''
'''
pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption('Warriors')

def getKey(key):
    return pygame.key.get_pressed()[eval("pygame.K_"+key)]
                                  
#main loop
while run:
    for event in pygame.event.get(): #handle exiting
        if event.type == QUIT:
            run = False 
            break

    screen.fill(white)
    pygame.draw.rect(screen, black, player)
    pygame.draw.rect(screen, gray, ground)
    screen.blit(evil, (20, 20))

    #main code
    if getKey("UP"): player.y-=1
    if getKey("DOWN"): player.y+=1
    if getKey("LEFT"): player.x-=1
    if getKey("RIGHT"): player.x+=1
    pygame.display.flip()
    clock.tick(60)
pygame.quit() # Quits the window
'''
