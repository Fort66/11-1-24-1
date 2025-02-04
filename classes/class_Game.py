import pygame as pg


from icecream import ic

# Инициализация звука. Инициализация плейера. (частота, биты (Если значение отрицательное, то будут использоваться подписанные значения выборки. Положительные значения означают, что будут использоваться неподписанные аудиосэмплированные выборки. Неверное значение вызывает исключение), каналы, буфер)
pg.mixer.pre_init(44100, -16, 2, 2048)

from pygame.locals import QUIT, KEYDOWN, K_ESCAPE


from config.create_Objects import screen
from classes.class_CheckEvents import CheckEvents



class Game:
    def __init__(self):
        self.run = True
        self.clock = pg.time.Clock()
        self.fps = 100
        self.win_width = screen.window.get_width()
        self.win_height = screen.window.get_height()
        self.check_events = CheckEvents(self)


    def run_game(self):
        while self.run:
            screen.window.fill(screen.color)
            # gifBack.render(screen.window, gifBackRect)
            # обработка игровых событий
            self.check_events.check_events()


            pg.display.update()
            self.clock.tick(self.fps)