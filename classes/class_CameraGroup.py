import pygame as pg
from pygame.sprite import Group
from pygame.image import load
from pygame.display import get_surface
from pygame.math import Vector2
# import gif_pygame
# from Game.source import *
# from icecream import ic
# from Game.LevelsGame import LG
# from Game.source import backgroundSection

back = 'images/back6.jpg'


class CameraGroup(Group):
    def __init__(self,
                game: object=None):
        super().__init__(self)

        self.game = game
        self.display_surface = get_surface()
        # camera offset
        self.offset = Vector2()
        self.half = (self.display_surface.get_size()[0] // 2, self.display_surface.get_size()[1] // 2)
        self.camera_rect = pg.Rect(10, 10, 10, 10)
        self.keyboard_speed = None
        self.mouse_speed = None
        self.setBackground()


    def setBackground(self) -> None:
        self.source = back
        # self.source= backgroundSection(LG.currentLevel)
        # self.gifBackgtound = gif_pygame.load('Images/Back/gif/2.gif')
        # self.gifRect = self.gifBackgtound.get_rect()
        self.background_surface = load(self.source).convert_alpha()
        # self.backgroundRect = self.backgroundSurface.get_rect(center = self.half)
        self.backgroundRect = self.background_surface.get_rect()
        # ic(self.backgroundRect)


    def cameraCenter(self, target):
        self.offset.x = target.rect.centerx - self.half[0]
        self.offset.y = target.rect.centery - self.half[1]


    def customDraw(self, player):
        self.cameraCenter(player)
        # background offset
        # self.display_surface.blit(self.gifBackgtound, self.gifRect)
        self.backgroundOffset = self.backgroundRect.topleft - self.offset
        self.display_surface.blit(self.background_surface, self.backgroundOffset)

        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.center):
            offsetPosition = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image_rotation, offsetPosition)
