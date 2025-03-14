import sys
import pygame
import pygame_gui

from pygame_gui import UIManager
from app.screens.menu import MenuScreen
from app.screens.program import ProgramScreen


class UIFacade:
    def __init__(self, display: pygame.display, manager: UIManager):
        self.state: str = "MENU"
        self.display: pygame.display = display
        self.manager: pygame_gui.UIManager = manager
        self.menu_screen: MenuScreen = MenuScreen(self.manager)
        self.program_screen: ProgramScreen = ProgramScreen(self.manager)

    def render(self):
        if self.state == 'MENU':
            self.menu_screen.render()
        elif self.state == 'PROGRAM':
            self.program_screen.render()

    def handle(self, event: pygame.event.Event):
        if self.state == 'MENU':
            self.state = self.menu_screen.handle(event)
        elif self.state == 'PROGRAM':
            self.state = self.program_screen.handle(event)

    @staticmethod
    def quit():
        pygame.quit()
        sys.exit()
