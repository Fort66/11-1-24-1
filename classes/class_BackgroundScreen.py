import pygame as pg
from pygame.locals import K_RIGHT, K_LEFT
from pygame.transform import scale
from pygame.image import load
from pygame.key import get_pressed


from dataclasses import dataclass, field


@dataclass
class BackgroundScreen:
    image_background: str = field(default = '')
    screen: object = field(default = None)
    speed: int = field(default = 0)
    long: int = 1
    transformation: bool = False
    scrolling: bool = False
    
    
    def __post_init__(self):
        self.scr_widht = self.screen.get_width()
        self.scr_height = self.screen.get_height()
        
        self.bg = scale(load(self.image_background).convert_alpha(), (self.scr_widht, self.scr_height))
        
        self.bg_list = [self.bg for _ in range(3)]
        
        self.bg_rect_left = self.bg_list[0].get_rect()
        self.bg_rect_center = self.bg_list[1].get_rect()
        self.bg_rect_right = self.bg_list[2].get_rect()
        
    
    def eventKey(self):
        keys = get_pressed()
        
        if keys[K_RIGHT]:
            self.scroll('right')
            
        if keys[K_LEFT]:
            self.scroll('left')

    
    def scroll(self, direction):
        if direction =='right':
            if self.bg_rect_center.x <= - self.scr_widht:
                self.bg_rect_center.x = 0
            self.bg_rect_center.x -= self.speed
            
        if direction =='left':
            if self.bg_rect_center.x >= self.scr_widht:
                self.bg_rect_center.x = 0
            self.bg_rect_center.x += self.speed

        self.bg_rect_left.x = self.bg_rect_center.x - (self.bg_rect_center[2] - self.speed)
        self.bg_rect_right.x = self.bg_rect_center.x + (self.bg_rect_center[2] - self.speed)

    def blitBG(self):
        self.screen.blit(self.bg_list[0], self.bg_rect_left)
        self.screen.blit(self.bg_list[1], self.bg_rect_center)
        self.screen.blit(self.bg_list[2], self.bg_rect_right)