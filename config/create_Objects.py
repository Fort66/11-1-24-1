from UI.Screens.class_ScreenGame import ScreenGame
from logic.class_Checks import Checks
from config.sources.class_Weapons import Weapons





screen = ScreenGame(size = (1280, 720),
                    caption = 'Game',
                    color = 'SteelBlue',
                    # icon = 'images/icon.jpg', # пример иконки
                    is_resizable = True,
                    is_fullscreen = False)


checks = Checks()
weapons = Weapons()
