"""
This module is used to pull individual sprites from sprite sheets.
"""
import pygame
 
class SpriteSheet(object):
    """ Class used to grab images out of a sprite sheet. """
 
    def __init__(self, file_name):
        """ Constructor. Pass in the file name of the sprite sheet. """
 
        # Load the sprite sheet.
        self.sprite_sheet = pygame.image.load(file_name).convert()
        self.backgroundcol = (164,117,160)
 
 
    def get_image(self, x, y, width, height):
        """ Grab a single image out of a larger spritesheet
            Pass in the x, y location of the sprite
            and the width and height of the sprite. """
 
        # Create a new blank image
        image = pygame.Surface([width, height]).convert()
 
        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
 
        # Assuming black works as the transparent color
        image.set_colorkey(self.backgroundcol)
 
        # Return the image
        return image

class GameEntity(object):
    def __init__(self):
        self.sheet = SpriteSheet('cat.png')
        self.spritewidth = 22
        self.spriteheight = 22
        self.frames = [(0,0,self.spritewidth,self.spriteheight),
                       (22,22,self.spritewidth,self.spriteheight),
                       (22,48,self.spritewidth,self.spriteheight)]
        self.images = []
        I = 0
        while I < len(self.frames):
            self.images.append(self.sheet.get_image(self.frames[I]))
        self.index = 0
        self.image = self.images[self.index]
    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
