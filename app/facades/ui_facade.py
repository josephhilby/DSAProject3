import sys
import pygame

from lib.constraints import *
from app.screens.menu import *

class UIFacade:
    def __init__(self, display: pygame.display):
        self.display: pygame.display = display
        self.menu_screen: MenuScreen = MenuScreen()

    def render(self, state: str):
        if state == 'MENU':
            self.menu_screen.render(self.display)

    @staticmethod
    def quit():
        pygame.quit()
        sys.exit()
