import pygame
import pygame_gui

from pygame_gui.elements import UIButton
from lib.constants import *


class ProgramScreen:
    def __init__(self, manager: pygame_gui.UIManager):
        self.manager: pygame_gui.UIManager = manager
        self.run_button: UIButton | None = None
        self.reset_button: UIButton | None = None
        self.exit_button: UIButton | None = None

    def render(self):
        if self.run_button is None:
            self.run_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN_WIDTH * 0.59, SCREEN_HEIGHT * 0.86), (100, 50)),
                                                         text='Run',
                                                         manager=self.manager)

        if self.reset_button is None:
            self.reset_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN_WIDTH * 0.72, SCREEN_HEIGHT * 0.86), (100, 50)),
                                                         text='Reset',
                                                         manager=self.manager)
        if self.exit_button is None:
            self.exit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN_WIDTH * 0.85, SCREEN_HEIGHT * 0.86), (100, 50)),
                                                         text='Exit',
                                                         manager=self.manager)

    def handle(self, event: pygame.event.Event):
        if event.ui_element == self.run_button:
            print("run")
        elif event.ui_element == self.reset_button:
            print("reset")
        elif event.ui_element == self.exit_button:
            self.clear()
            return "MENU"

        return "PROGRAM"

    def clear(self):
        self.run_button.kill()
        self.reset_button.kill()
        self.exit_button.kill()
        self.run_button = None
        self.reset_button = None
        self.exit_button = None
