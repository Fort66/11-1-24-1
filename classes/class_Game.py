import pygame as pg

pg.mixer.pre_init(44100, -16, 2, 2048)

from icecream import ic

from config.create_Objects import screen, levels_game

from classes.class_CheckEvents import CheckEvents
from classes.class_CameraGroup import CameraGroup
from classes.class_SpriteGroups import SpriteGroups
from classes.class_BackgroundScreen import BackgroundScreen

from units.class_Player import Player
from units.class_Enemies import Enemy

from logic.class_LevelsGame import LevelsGame

from UI.Screens.class_MiniMap import MiniMap


class Game:
    def __init__(self):
        self.run = True
        self.clock = pg.time.Clock()
        self.fps = 100
        self.screen = screen
        self.old_screen_size = self.screen.window.get_size()
        self.check_events = CheckEvents(self)
        self.sprite_groups = SpriteGroups()
        self.sprite_groups.camera_group = CameraGroup(self)
        self.mini_map = MiniMap(scale_value=0.1, color_map=(0, 100, 0, 170))
        self.background_animate()
        self.setup()

    def setup(self):
        self.player = Player(pos=screen.rect.center)

        for _ in range(levels_game.enemies_amount):
            self.sprite_groups.camera_group.add(Enemy(player=self.player))

    def background_animate(self):
        self.back_animate = BackgroundScreen(
            dir_path='images/back_animate/1',
            speed_frame=.1,
            loops=-1,
            size=(
                self.screen.rect[2],
                self.screen.rect[3]
            ),
            no_group=True,
            owner=self.screen
        )

    def check_screen_size(self):
        if self.old_screen_size != self.screen.window.get_size():
            self.background_animate()
            self.old_screen_size = self.screen.window.get_size()

    def run_game(self):
        while self.run:
            screen.window.fill(screen.color)

            self.check_events.check_events()

            if len(self.sprite_groups.enemies_group) == 0:
                levels_game.attack_level += 1
                levels_game.current_level += 1
                self.sprite_groups.camera_group.set_background()
                levels_game.update_levels()
                self.setup()

            if len(self.sprite_groups.player_group) == 0:
                levels_game.attack_level = 0
                levels_game.current_level = 1
                self.sprite_groups.camera_group.set_background()
                levels_game.update_levels()
                self.setup()

            self.check_screen_size()
            self.back_animate.update()
            self.sprite_groups.camera_group.update()

            self.screen.update_caption(f"{str(round(self.clock.get_fps(), 2))}")
            pg.display.update()
            self.clock.tick(self.fps)
