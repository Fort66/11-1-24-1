import pygame as pg
from dataclasses import dataclass
from pygame.display import set_mode, set_caption, set_icon, get_desktop_sizes
from pygame.locals import RESIZABLE, FULLSCREEN
from  pygame.image import load

pg.init()

@dataclass
class ScreenGame:
    size: tuple = (0, 0)
    color: str | tuple[int, int, int] = 'SteelBlue'
    caption: str = 'Game'
    icon: str = ''
    is_resizable: bool = False
    is_fullscreen: bool = False

    def __post_init__(self):
        if self.is_resizable:
            self.window = set_mode(self.size, RESIZABLE)
        elif self.is_fullscreen:
            self.current_screen_resolution = get_desktop_sizes()[0]
            print(self.current_screen_resolution)
            self.window = set_mode(self.current_screen_resolution, FULLSCREEN)
        else:
            self.window = set_mode(self.size)
        if self.caption:
            self.caption = set_caption(self.caption)
        if self.icon:
            self.icon = set_icon(load(self.icon))

        self.rect = self.window.get_rect()

    def update_caption(self, caption):
        self.caption = set_caption(caption)
