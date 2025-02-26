import pygame as pg

pg.mixer.pre_init(44100, -16, 2, 2048)

from icecream import ic

from config.create_Objects import screen, levels_game
from classes.class_CheckEvents import CheckEvents
from classes.class_CameraGroup import CameraGroup
from units.class_Player import Player
from units.class_Enemies import Enemy

from classes.class_SpriteGroups import SpriteGroups
from logic.class_LevelsGame import LevelsGame

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
        self.mini_map = MiniMap(scale_value=0.15, color_map=(0, 100, 0, 170))
        self.load_player()
        self.load_enemies()

    def load_player(self):
        self.player = Player(pos=screen.rect.center)

    def load_enemies(self):
        for _ in range(levels_game.enemies_amount):
            self.sprite_groups.camera_group.add(Enemy(player=self.player))

    def run_game(self):
        while self.run:
            screen.window.fill(screen.color)

            self.check_events.check_events()

            if len(self.sprite_groups.enemies_group) == 0:
                levels_game.attack_level += 1
                levels_game.current_level += 1
                self.sprite_groups.camera_group.set_background()
                levels_game.update_levels()
                self.load_enemies()

            if len(self.sprite_groups.player_group) == 0:
                levels_game.attack_level = 0
                levels_game.current_level = 1
                self.sprite_groups.camera_group.set_background()
                levels_game.update_levels()
                self.load_player()
                self.load_enemies()

            self.sprite_groups.camera_group.update()
            self.sprite_groups.camera_group.custom_draw(self.player)

            self.screen.update_caption(f"{str(round(self.clock.get_fps(), 2))}")
            pg.display.update()
            self.clock.tick(self.fps)
