import pygame as pg
from pygame.transform import scale_by

from config.create_Objects import screen
from classes.class_SpriteGroups import SpriteGroups


class MiniMap:
    def __init__(self):
        self.sprite_groups = SpriteGroups()
        self.old_screen_size = screen.window.get_size()
        self.set_map()

    def set_map(self):
        self.map_surface = pg.Surface(screen.window.get_size(), pg.SRCALPHA)
        self.map_surface = scale_by(self.map_surface, .25)
        self.map_size = self.map_surface.get_size()
        self.map_surface.fill((0, 100, 0, 50))
        self.ratioX = (self.map_size[0] /  self.sprite_groups.camera_group.background_rect[2])
        self.ratioY = (self.map_size[1] / self.sprite_groups.camera_group.background_rect[3])
        
        self.map_rect = self.map_surface.get_rect(bottomright=screen.rect.bottomright)
        
    def change_size_map(self):
