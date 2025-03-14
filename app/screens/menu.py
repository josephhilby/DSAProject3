import sys

import pygame
import pygame_gui

from pygame_gui.elements import UIButton

from app.components.text import *

class MenuScreen:
    def __init__(self, manager):
        self.manager: pygame_gui.UIManager = manager
        self.display: bool = False
        self.exit_button: UIButton | None = None
        self.start_button: UIButton | None = None

    def render(self):
        if self.start_button is None:
            self.start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN_WIDTH * 0.72, SCREEN_HEIGHT * 0.86), (100, 50)),
                                                         text='Start',
                                                         manager=self.manager)
        if self.exit_button is None:
            self.exit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN_WIDTH * 0.85, SCREEN_HEIGHT * 0.86), (100, 50)),
                                                         text='Exit',
                                                         manager=self.manager)

    def handle(self, event: pygame.event.Event):
        if event.ui_element == self.start_button:
            print("hello world")

        if event.ui_element == self.exit_button:
            pygame.quit()
            sys.exit()

    def clear(self):
        self.start_button.kill()
        self.start_button = None

