import pygame as pg

from loguru import logger
from sys import exit

pg.init()



# logger.add(
#     stdout,в
#     format='{time} {level} {message}',
#     level = 'ERROR'
# )


@logger.catch
def main():
    from classes.class_Game import Game
    game = Game()
    game.run_game()


if __name__ == '__main__':
    # try:
    main()
    # finally:
    pg.quit()
    exit()

