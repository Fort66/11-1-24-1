from pygame.sprite import Sprite
from pygame.transform import scale, flip, rotozoom, scale_by
from pygame.image import load
from pygame.locals import MOUSEWHEEL
from pygame import mouse

from icecream import ic

scale_value = 1

heroes = {
        0: scale_by(load('images/hero1.png').convert_alpha(), scale_value), # 0
        22: scale_by(load('images/hero2.png').convert_alpha(), scale_value), # 22
        45: scale_by(load('images/hero3.png').convert_alpha(), scale_value), # 45
        67: scale_by(load('images/hero4.png').convert_alpha(), scale_value), # 67
        90: scale_by(load('images/hero5.png').convert_alpha(), scale_value), # 90
}




class Player(Sprite):
    def __init__(self, pos, group, game, size = (0, 0)):
        super().__init__(group)
        self.game = game
        self.group = group
        self.pos = pos
        self.size = size
        self.angle = 0
        self.negative_angle = 0
        self.__post_init__()
        
    def __post_init__(self):
        self.image_rotation = heroes[0]


