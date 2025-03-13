import pygame_gui
from pygame_gui.elements import UIButton

from app.components.text import *

class MenuScreen:
    def __init__(self, manager):
        self.manager: pygame_gui.UIManager = manager
        self.header_text: PyGameText | None = None
        self.start_button = None

    def render(self):
        # self.header_text = text(MENU_TXT, DEFAULT_FONT, MENU_FONT_SIZE, BLACK, 2, 20)
        # render_text(display, self.header_text)
        #
        # self.start_button = button("Start", DEFAULT_FONT, BUTTON_FONT_SIZE, BLACK, 1.3, 1.075)
        # render_button(display, self.start_button)
        #
        # self.exit_button = button("Exit", DEFAULT_FONT, BUTTON_FONT_SIZE, BLACK, 1.1, 1.075)
        # render_button(display, self.exit_button)

        if self.start_button is None:
            self.start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN_WIDTH * 0.72, SCREEN_HEIGHT * 0.86), (100, 50)),
                                                         text='Start',
                                                         manager=self.manager)

    def handle(self, event: pygame.event.Event):
        if event.ui_element == self.start_button:
            print("hello world")
