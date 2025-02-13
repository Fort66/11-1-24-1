from pygame.sprite import Sprite
from pygame.transform import scale, flip, rotozoom, scale_by
from pygame.image import load
from pygame.locals import MOUSEWHEEL, K_a, K_d, K_w, K_s
from pygame.math import Vector2
from pygame.key import get_pressed

import math
from icecream import ic

from random import randint, choice, uniform

from config.sources.enemies.source import ENEMIES
from units.class_Shots import Shots
from units.class_Guardian import Guardian

from config.create_Objects import screen


class Enemy(Sprite):
    def __init__(self,
                group=None,
                player=None):
        super().__init__(group)

        self.group = group
        self.player = player
        self.angle = 0
        self.shots = False
        self.is_min_distance = False
        self.min_distance = 300
        self.shot_distance = 1500
        self.__post_init__()
        self.random_value()
        self.change_direction()
        self.group.add(self)


    def __post_init__(self):
        self.image = ENEMIES[1]['angle'][0]['sprite']
        self.image_rotation = self.image.copy()

        self.pos = (
                    uniform(self.group.background_rect.left + 200,
                            self.group.background_rect.right - 200),
                    uniform(self.group.background_rect.top + 200,
                            self.group.background_rect.bottom - 200)
        )

        self.rect = self.image_rotation.get_rect(center=self.pos)
        self.direction = Vector2(self.pos)
        
        self.shield = Guardian(
                                dir_path='images/Guards/guard2',
                                speed_frame=.09,
                                obj_rect=self.rect,
                                )


    def random_value(self):
        self.speed = randint(0, 10)
        self.move_count = randint(0, 600)
        self.direction_list = [0, 1, -1]



    def rotate_vector(self, vector, angle):
        vector = Vector2(vector)
        return vector.rotate_rad(angle)


    def rotation(self):
        rotateX = self.player.rect.centerx - self.rect.centerx
        rotateY = self.player.rect.centery - self.rect.centery
        angle_vector = -math.atan2(rotateY, rotateX) * 180 / math.pi

        if angle_vector > 0:
            self.angle = angle_vector
        else:
            self.angle = angle_vector + 360

        for value in ENEMIES[1]['angle']:
            if self.angle <= value:
                self.image = ENEMIES[1]['angle'][value]['sprite']
                break

        self.image_rotation = self.image
        self.image_rotation = rotozoom(self.image, self.angle, 1)
        self.rect = self.image_rotation.get_rect(center=self.rect.center)


    def check_move_count(self):
        if self.move_count <= 0:
            self.random_value()
        else:
            self.move_count -= 1


    def change_direction(self):
        self.moveX = choice(self.direction_list)
        self.moveY = choice(self.direction_list)


    def check_position(self):
        if self.rect.left <= self.group.background_rect.left:
            self.rect.left = self.group.background_rect.left
            self.change_direction()
        if self.rect.right >= self.group.background_rect.right:
            self.rect.right = self.group.background_rect.right
            self.change_direction()
        if self.rect.top <= self.group.background_rect.top:
            self.rect.top = self.group.background_rect.top
            self.change_direction()
        if self.rect.bottom >= self.group.background_rect.bottom:
            self.rect.bottom = self.group.background_rect.bottom
            self.change_direction()

        if not self.is_min_distance:
            if Vector2(self.rect.center).distance_to(self.player.rect.center) < self.min_distance:
                self.is_min_distance = True
                self.change_direction()
        
        if Vector2(self.rect.center).distance_to(self.player.rect.center) > self.min_distance:
                self.is_min_distance = False
    

    def move(self):
        self.rect.move_ip(self.moveX * self.speed, self.moveY * self.speed)
        
        
    def shot(self):
        if Vector2(self.rect.center).distance_to(self.player.rect.center) <= self.shot_distance:
            if self.player.first_shot and randint(0, 100) == 50:
                self.group.add(
                            Shots(
                                pos=self.rect.center,
                                screen=screen,
                                group=self.group,
                                angle=self.angle,
                                speed=10,
                                kill_shot_distance=2000,
                                shoter=self,
                                color=None,
                                image='images/Shots/shot1.png',
                                scale_value=.08
                                )
                            )

        
    def update(self):
        self.check_position()
        self.rotation()
        self.check_move_count()
        self.move()
        self.shot()
        self.shield.animate(self.rect)





