import pygame as pg
from pygame.sprite import Sprite
from pygame.math import Vector2
from pygame.transform import rotozoom

from icecream import ic


class Shots(Sprite):
    def __init__(
                self,
                pos=(0, 0),
                group=None,
                screen=None,
                size=(10, 2),
                color='white',
                speed=0,
                angle=0,
                shoter=None,
                kill_shot_distance=None
                ):
        super().__init__(group)

        self.screen = screen
        self.group = group
        self.shoter = shoter
        self.kill_shot_distance = kill_shot_distance
        self.angle = angle
        self.speed = speed
        self.size = size
        self.old_shot_coordinate = Vector2(self.shoter.rect.center)
        self.image = pg.Surface(self.size, pg.SRCALPHA)
        self.image.fill(color)
        self.image_rotation = rotozoom(self.image, self.angle, 1)
        self.rect = self.image_rotation.get_rect(center=pos)
        self.offset =  Vector2().rotate(self.angle)
        self.pos = Vector2(pos) + self.offset
        self.direction = Vector2(1, 0).rotate(-self.angle)


    def check_position(self):
        if Vector2(self.rect.center).distance_to(self.old_shot_coordinate) > self.kill_shot_distance:
            self.kill()

    def move(self):
        self.pos += self.direction * self.speed
        self.rect.center = self.pos


    def update(self):
        self.check_position()
        self.move()