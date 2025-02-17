import pygame as pg

pg.mixer.pre_init(44100, -16, 2, 2048)

from icecream import ic

from config.create_Objects import screen
from classes.class_CheckEvents import CheckEvents
from classes.class_CameraGroup import CameraGroup
from units.class_Player import Player
from units.class_Enemies import Enemy

from classes.class_SpriteGroups import SpriteGroups

from UI.Screens.class_MiniMap import MiniMap


class Game:
    def __init__(self):
        self.run = True
        self.clock = pg.time.Clock()
        self.fps = 100
        self.screen = screen
        self.win_width = screen.window.get_width()
        self.win_height = screen.window.get_height()
        self.check_events = CheckEvents(self)
        self.sprite_groups = SpriteGroups()
        self.sprite_groups.camera_group = CameraGroup(self)
        self.mini_map = MiniMap(scale_value=0.2, color_map=(0, 100, 0, 170))
        self.setup()

    def setup(self):
        self.player = Player(pos=screen.rect.center)

        for _ in range(10):
            self.sprite_groups.camera_group.add(Enemy(player=self.player))

    def run_game(self):
        while self.run:
            screen.window.fill(screen.color)

            self.check_events.check_events()

            self.sprite_groups.camera_group.update()
            self.sprite_groups.camera_group.custom_draw(self.player)

            self.screen.update_caption(f"{str(round(self.clock.get_fps(), 2))}")
            pg.display.update()
            self.clock.tick(self.fps)
