import pygame

import globalvars
from random import randint
import platforms

class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    # Lists of sprites used in all levels. Add or remove
    # lists as needed for your game. """
    platform_list = None
    enemy_list = None

    # Background image
    background = None

    # How far this world has been scrolled left/right
    world_shift = 0
    level_limit = -1000

    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        screen.fill(globalvars.BLUE)
        screen.blit(self.background,(self.world_shift // 3,0))

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("Images/background.png").convert()
        self.background.set_colorkey(globalvars.WHITE)
        self.level_limit = -2500

        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.ROCK_GROUND, 400, 560],
                  [platforms.ROCK, 700, 550],
                 [platforms.ROCK,1000,550],
                 [platforms.ROCK,1000,500],
                 [platforms.ROCK,0,550]
                  ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)


# Create platforms for the level
class Level_02(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("Images/background1.png").convert()
        self.background.set_colorkey(globalvars.WHITE)
        self.level_limit = -1000

        platform_x = globalvars.SCREEN_WIDTH / 24
        ground_base = 550
        shift = 35
        noise = 5

        # Array with type of platform, and x, y location of the platform.
        level = [[platforms.ROCK,(platform_x * 1) - shift,ground_base + randint(-noise,noise)],
                 [platforms.ROCK,(platform_x * 2) - shift,ground_base + randint(-noise,noise)],
                 [platforms.ROCK,(platform_x * 3) - shift,ground_base + randint(-noise,noise)],
                 [platforms.ROCK,(platform_x * 4) - shift,ground_base + randint(-noise,noise)],
                 [platforms.ROCK,(platform_x * 5) - shift,ground_base + randint(-noise,noise)],
                 [platforms.ROCK,(platform_x * 6) - shift,ground_base + randint(-noise,noise)],
                 [platforms.ROCK,(platform_x * 7) - shift,ground_base + randint(-noise,noise)],
                 [platforms.ROCK,(platform_x * 8) - shift,ground_base + randint(-noise,noise)],
                 [platforms.ROCK,(platform_x * 9) - shift,ground_base + randint(-noise,noise)],
                 [platforms.ROCK,(platform_x * 10) - shift,ground_base + randint(-noise,noise)],
                 [platforms.ROCK,(platform_x * 11) - shift,ground_base + randint(-noise,noise)],
                 [platforms.ROCK,(platform_x * 12) - shift,ground_base + randint(-noise,noise)],
                 [platforms.ROCK,(platform_x * 13) - shift,ground_base + randint(-noise,noise)],
                 [platforms.ROCK,(platform_x * 14) - shift,ground_base + randint(-noise,noise)],
                 [platforms.ROCK,(platform_x * 15) - shift,ground_base + randint(-noise,noise)],
                 [platforms.ROCK,(platform_x * 16) - shift,ground_base + randint(-noise,noise)],
                 [platforms.ROCK,(platform_x * 17) - shift,ground_base + randint(-noise,noise)],
                 [platforms.ROCK,(platform_x * 18) - shift,ground_base + randint(-noise,noise)],
                 [platforms.ROCK,(platform_x * 19) - shift,ground_base + randint(-noise,noise)],
                 [platforms.ROCK,(platform_x * 20) - shift,ground_base + randint(-noise,noise)],
                 [platforms.ROCK,(platform_x * 21) - shift,ground_base + randint(-noise,noise)],
                 [platforms.ROCK,(platform_x * 22) - shift,ground_base + randint(-noise,noise)],
                 [platforms.ROCK,(platform_x * 23) - shift,ground_base + randint(-noise,noise)],
                 [platforms.ROCK,(platform_x * 24) - shift,ground_base + randint(-noise,noise)]
                  ]
        
        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
class ForestCamp(Level):
    #thunderclan camp
    
    def __init__ (self, player):
        # Call the parent constructor
        Level.__init__(self, player)
        
        self.background = pygame.image.load("Images/background.png").convert()
        self.background.set_colorkey(globalvars.WHITE)
        
        Level = []
        
        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        
