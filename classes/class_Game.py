import pygame as pg


from icecream import ic

# Инициализация звука. Инициализация плейера. (частота, биты (Если значение отрицательное, то будут использоваться подписанные значения выборки. Положительные значения означают, что будут использоваться неподписанные аудиосэмплированные выборки. Неверное значение вызывает исключение), каналы, буфер)
pg.mixer.pre_init(44100, -16, 2, 2048)

from pygame.locals import QUIT, KEYDOWN, K_ESCAPE


from config.create_Objects import screen
from classes.class_CheckEvents import CheckEvents
from classes.class_CameraGroup import CameraGroup
from units.class_Player import Player
from units.class_Enemies import Enemy




class Game:
    def __init__(self):
        self.run = True
        self.clock = pg.time.Clock()
        self.fps = 100
        self.screen = screen
        self.win_width = screen.window.get_width()
        self.win_height = screen.window.get_height()
        self.check_events = CheckEvents(self)
        self.create_groups()
        self.setup()
        
    def setup(self):
        self.player = Player(
                            pos=screen.rect.center,
                            group=self.camera_group,
                            )

        
        for _ in range(10):
            self.camera_group.add(
                                Enemy(
                                    group=self.camera_group,
                                    player=self.player
                                    )
                                )
    
    def create_groups(self):
        self.camera_group = CameraGroup(self)


    def run_game(self):
        while self.run:
            screen.window.fill(screen.color)
            # gifBack.render(screen.window, gifBackRect)
            # обработка игровых событий
            self.check_events.check_events()
            
            self.camera_group.update()
            self.camera_group.custom_draw(self.player)


            pg.display.update()
            self.clock.tick(self.fps)