from pygame.sprite import Sprite
from pygame.transform import rotozoom
from pygame.locals import (
    MOUSEWHEEL,
    MOUSEBUTTONDOWN,
    K_a,
    K_d,
    K_w,
    K_s
    )
from pygame.math import Vector2
from pygame.key import get_pressed

from time import time

from config.create_Objects import (
    checks,
    weapons,
    screen
    )

from units.class_Shots import Shots
from units.class_Guardian import Guardian

from classes.class_SpriteGroups import SpriteGroups

from functions.function_player_collision import player_collision
from functions.function_load_source import load_python_file_source

HERO = load_python_file_source(
    dir_path='config.sources.heroes',
    module_name='source',
    level=1,
    name_source='HERO'
)


class Player(Sprite):
    def __init__(
        self,
        pos=(0, 0),
    ):
        self.sprite_groups = SpriteGroups()
        super().__init__(self.sprite_groups.camera_group)
        self.sprite_groups.camera_group.add(self)
        self.sprite_groups.player_group.add(self)

        self.pos = pos
        self.direction = Vector2(pos)
        self.angle = 0
        self.rotation_speed = HERO['rotation_speed']
        self.speed = HERO['speed']
        self.shot_time = 1
        self.permission_shot = HERO['permission_shot']
        self.hp = HERO['hp']
        self.first_shot = False
        self.__post_init__()

    def __post_init__(self):
        self.image_rotation = HERO["angle"][0]["sprite"]
        self.rect = self.image_rotation.get_rect(center=self.pos)

        self.sprite_groups.camera_group.add(shield:= Guardian(
            types=1,
            angle=self.angle,
            size=self.rect.size,
            owner=self
        ))
        self.sprite_groups.player_guard_group.add(shield)

        self.prepare_weapon(0)


    def handle_event(self, event):
        if event.type == MOUSEWHEEL:
            if event.y == -1:
                self.angle = (self.angle - self.rotation_speed) % 360
                self.rotation()
            elif event.y == 1:
                self.angle = (self.angle + self.rotation_speed) % 360
                self.rotation()

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if not self.first_shot:
                    self.first_shot = not self.first_shot
                self.shot()

    def prepare_weapon(self, angle):
        weapons.load_weapons(obj=self, source=HERO["angle"][angle]["weapons"], angle=angle)

    def pos_weapons_rotation(self):
        return weapons.pos_rotation(self, self.angle)

    def rotation(self):
        for value in HERO["angle"]:
            if self.angle <= value:
                self.image = HERO["angle"][value]["sprite"]
                self.prepare_weapon(value)
                break

        self.image_rotation = self.image
        self.image_rotation = rotozoom(self.image_rotation, self.angle, 1)
        self.rect = self.image_rotation.get_rect(center=self.rect.center)

    def check_position(self):
        checks.position(self, self.sprite_groups.camera_group.background_rect)

    def move(self):
        keys = get_pressed()
        if keys[K_a]:
            self.rect.move_ip(-self.speed, 0)
        if keys[K_w]:
            self.rect.move_ip(0, -self.speed)
        if keys[K_s]:
            self.rect.move_ip(0, self.speed)
        if keys[K_d]:
            self.rect.move_ip(self.speed, 0)

    def shot(self):
        if self.shot_time == 0:
            self.shot_time = time()
        if time() - self.shot_time >= self.permission_shot:
            value = self.pos_weapons_rotation()
            for pos in value:
                self.sprite_groups.camera_group.add(
                    shot := Shots(
                        types=2,
                        pos=(pos),
                        angle=self.angle,
                        owner=self
                    )
                )
                self.sprite_groups.player_shot_group.add(shot)
                self.shot_time = time()

    def decrease_hp(self, value):
        if self.hp > 0:
            self.hp -= value
        if self.hp <= 0:
            self.kill()

    def update(self):
        self.check_position()
        self.move()
        player_collision()
        weapons.update_weapons(self, self.angle)
