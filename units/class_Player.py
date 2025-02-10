from pygame.sprite import Sprite
from pygame.transform import scale, flip, rotozoom, scale_by
from pygame.image import load
from pygame.locals import MOUSEWHEEL, K_a, K_d, K_w, K_s
from pygame.math import Vector2
from pygame.key import get_pressed

from icecream import ic

scale_value = .2

heroes = {
        0: scale_by(load('images/Heroes/hero1/hero1.png').convert_alpha(), scale_value), # 0
        22: scale_by(load('images/Heroes/hero1/hero2.png').convert_alpha(), scale_value), # 22
        45: scale_by(load('images/Heroes/hero1/hero3.png').convert_alpha(), scale_value), # 45
        67: scale_by(load('images/Heroes/hero1/hero4.png').convert_alpha(), scale_value), # 67
        90: scale_by(load('images/Heroes/hero1/hero5.png').convert_alpha(), scale_value), # 90
        112: flip(scale_by(load('images/Heroes/hero1/hero4.png').convert_alpha(), scale_value), False, True),
        135: flip(scale_by(load('images/Heroes/hero1/hero3.png').convert_alpha(), scale_value), False, True),
        157: flip(scale_by(load('images/Heroes/hero1/hero2.png').convert_alpha(), scale_value), False, True),
        180: flip(scale_by(load('images/Heroes/hero1/hero1.png').convert_alpha(), scale_value), False, True),
        202: flip(scale_by(load('images/Heroes/hero1/hero2.png').convert_alpha(), scale_value), False, True),
        225: flip(scale_by(load('images/Heroes/hero1/hero3.png').convert_alpha(), scale_value), False, True),
        247: flip(scale_by(load('images/Heroes/hero1/hero4.png').convert_alpha(), scale_value), False, True),
        270: flip(scale_by(load('images/Heroes/hero1/hero5.png').convert_alpha(), scale_value), False, True),
        292: flip(flip(scale_by(load('images/Heroes/hero1/hero4.png').convert_alpha(), scale_value), False, True), False, True),
        315: flip(flip(scale_by(load('images/Heroes/hero1/hero3.png').convert_alpha(), scale_value), False, True), False, True),
        337: flip(flip(scale_by(load('images/Heroes/hero1/hero2.png').convert_alpha(), scale_value), False, True), False, True),
        359: scale_by(load('images/Heroes/hero1/hero1.png').convert_alpha(), scale_value),
}




class Player(Sprite):
    def __init__(self, pos, group, game):
        super().__init__(group)
        self.game = game
        self.group = group
        self.pos = pos
        # self.size = size
        self.direction = Vector2(pos)
        self.angle = 0
        self.rotation_speed = 10
        self.speed = 7
        self.__post_init__()


    def __post_init__(self):
        self.image_rotation = heroes[0]
        self.rect = self.image_rotation.get_rect(center=self.pos)


    def handle_event(self, event):
        if event.type == MOUSEWHEEL:
            if event.y == 1:
                self.angle = (self.angle - self.rotation_speed) % 360
                self.rotation()
            elif event.y == -1:
                self.angle = (self.angle + self.rotation_speed) % 360
                self.rotation()


    def rotation(self):
        for i in heroes:
            if self.angle <= i:
                self.image = heroes[i]
                break

        self.image_rotation = self.image
        self.image_rotation = rotozoom(self.image_rotation, self.angle, 1)

        self.rect = self.image_rotation.get_rect(center=self.rect.center)


    def check_position(self):
        if self.rect.left <= self.group.background_rect.left:
            self.rect.left = self.group.background_rect.left
        if self.rect.right >= self.group.background_rect.right:
            self.rect.right = self.group.background_rect.right
        if self.rect.top <= self.group.background_rect.top:
            self.rect.top = self.group.background_rect.top
        if self.rect.bottom >= self.group.background_rect.bottom:
            self.rect.bottom = self.group.background_rect.bottom


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


    def update(self):
        self.check_position()
        self.move()






