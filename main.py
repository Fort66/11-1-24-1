import pygame as pg

from loguru import logger
from sys import exit, stdout

pg.init()



logger.add(
    stdout,
    format='{time} {level} {message}',
    level = 'ERROR'
)


@logger.catch
def main():
    from classes.classGame import Game
    game = Game()
    game.runGame()


if __name__ == '__main__':
    # try:
    main()
    # finally:
    pg.quit()
    exit()

