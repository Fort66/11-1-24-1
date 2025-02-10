from pygame.sprite import Sprite
from pygame.transform import scale, flip, rotozoom, scale_by
from pygame.image import load
from pygame.locals import MOUSEWHEEL, K_a, K_d, K_w, K_s
from pygame.math import Vector2
from pygame.key import get_pressed

import math
from icecream import ic

from random import randint, choice, uniform

scale_value = .2

enemies = {
        0: scale_by(load('images/Enemies/enemy1/ship1.png').convert_alpha(), scale_value), # 0
        22: scale_by(load('images/Enemies/enemy1/ship2.png').convert_alpha(), scale_value), # 22
        45: scale_by(load('images/Enemies/enemy1/ship3.png').convert_alpha(), scale_value), # 45
        67: scale_by(load('images/Enemies/enemy1/ship4.png').convert_alpha(), scale_value), # 67
        90: scale_by(load('images/Enemies/enemy1/ship5.png').convert_alpha(), scale_value), # 90
        112: flip(scale_by(load('images/Enemies/enemy1/ship4.png').convert_alpha(), scale_value), False, True),
        135: flip(scale_by(load('images/Enemies/enemy1/ship3.png').convert_alpha(), scale_value), False, True),
        157: flip(scale_by(load('images/Enemies/enemy1/ship2.png').convert_alpha(), scale_value), False, True),
        180: flip(scale_by(load('images/Enemies/enemy1/ship1.png').convert_alpha(), scale_value), False, True),
        202: flip(scale_by(load('images/Enemies/enemy1/ship2.png').convert_alpha(), scale_value), False, True),
        225: flip(scale_by(load('images/Enemies/enemy1/ship3.png').convert_alpha(), scale_value), False, True),
        247: flip(scale_by(load('images/Enemies/enemy1/ship4.png').convert_alpha(), scale_value), False, True),
        270: flip(scale_by(load('images/Enemies/enemy1/ship5.png').convert_alpha(), scale_value), False, True),
        292: flip(flip(scale_by(load('images/Enemies/enemy1/ship4.png').convert_alpha(), scale_value), False, True), False, True),
        315: flip(flip(scale_by(load('images/Enemies/enemy1/ship3.png').convert_alpha(), scale_value), False, True), False, True),
        337: flip(flip(scale_by(load('images/Enemies/enemy1/ship2.png').convert_alpha(), scale_value), False, True), False, True),
        359: scale_by(load('images/Enemies/enemy1/ship1.png').convert_alpha(), scale_value),
}




class Enemy(Sprite):
    def __init__(self,
                group=None,
                game=None,
                player=None):
        super().__init__(group)

        self.game = game
        self.group = group
        self.player = player
        self.direction_list = [0, 1, -1]
        self.angle = 0
        self.speed = randint(0, 10)
        self.move_count = randint(0, 600)
        self.moveX = choice(self.direction_list)
        self.moveY = choice(self.direction_list)
        self.shots = False
        self.is_min_distance = False
        self.min_distance = 300
        self.shot_distance = 1500
        self.__post_init__()


    def __post_init__(self):
        self.image = enemies[0]
        self.image_rotation = enemies[0]
        
        self.pos = (
                    uniform(self.group.background_rect.left + 200,
                            self.group.background_rect.right - 200),
                    uniform(self.group.background_rect.top + 200,
                            self.group.background_rect.bottom - 200)
        )
        
        self.rect = self.image_rotation.get_rect(center=self.pos)
        self.direction = Vector2(self.pos)


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
        
        for i in enemies:
            if self.angle <= i:
                self.image = enemies[i]
                break

        self.image_rotation = self.image
        self.image_rotation = rotozoom(self.image, self.angle, 1)
        self.rect = self.image_rotation.get_rect(center=self.rect.center)
        
        
    def check_move_count(self):
        if self.move_count <= 0:
            self.move_count = randint(0, 600)
            self.speed = randint(0, 10)
            self.change_direction()
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

        
    def update(self):
        self.check_position()
        self.rotation()
        self.check_move_count()
        self.move()





