import sys
import pygame

class UIFacade:
    def __init__(self, display: pygame.display):
        self.display: pygame.display = display

    def render(self, state: str):
        if state == 'MENU':
            self.menu_screen.render(self.display)
        elif state == 'PROGRAM':
            self.program_screen.render(self.display)

    @staticmethod
    def quit():
        pygame.quit()
        sys.exit()
