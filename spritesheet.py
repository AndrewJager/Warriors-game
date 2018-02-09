"""
This module is used to pull individual sprites from sprite sheets.
"""
import pygame, os
from PIL import Image
import globalvars

class SpriteSheet(object):
    """ Class used to grab images out of a sprite sheet. """
    # This points to our sprite sheet image
    sprite_sheet = None

    def __init__(self, file_name,key,cat):
        """ Constructor. Pass in the file name of the sprite sheet. """

        # Load the sprite sheet.
        #self.key_image(file_name,(56,56,56),(200,200,200))
        self.sprite_sheet = pygame.image.load(file_name).convert()
        self.keycolor = cat

    def get_image(self, x, y, width, height):
        """ Grab a single image out of a larger spritesheet
            Pass in the x, y location of the sprite
            and the width and height of the sprite. """

        # Create a new blank image
        image = pygame.Surface([width, height]).convert()

        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        
        # Assuming black works as the transparent color
        image.set_colorkey(self.keycolor)
        
        # Return the image
        return image

def key_image(image, newcolor,path = "C:/Users/DELL/Desktop/Animation/Warriors/Warriors-game/Images",filename="cat.png"):
    cat = Image.open("Images/cat.png")
    pix=cat.load()
    keycolor = pix[9,13] #get current fur color
    shadecolor = pix[14,23]
    newshade = (abs(newcolor[0] // 3),abs(newcolor[1] // 3),abs(newcolor[2] // 3),255)
    I = 0
    II = 0
    while I < 274:
        II = 0
        while II < 100:
            if pix[I,II] == keycolor:#key cat
                pix[I,II] = newcolor
            if pix[I,II] == shadecolor: #key shadowed legs
                pix[I,II] = newshade
            II = II + 1
        I= I+1
    fullpath = os.path.join(path, filename)
    #cat.show()
    cat.save(fullpath)
    cat.close()
