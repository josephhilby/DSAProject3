import sys
import pygame
import pygame_gui

from pygame_gui.elements import UIButton, UIDropDownMenu
from lib.constants import *
from app.facades.algorithm_facade import AlgorithmFacade


class MenuScreen:
    def __init__(self, manager: pygame_gui.UIManager):
        self.manager: pygame_gui.UIManager = manager
        self.exit_button: UIButton | None = None
        self.start_button: UIButton | None = None
        self.alg_one_dropdown: UIDropDownMenu | None = None
        self.alg_two_dropdown: UIDropDownMenu | None = None
        self.alg_names: [str] = AlgorithmFacade().names

    def render(self):
        if self.start_button is None:
            self.start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN_WIDTH * 0.72, SCREEN_HEIGHT * 0.86), (100, 50)),
                                                             text='Start',
                                                             manager=self.manager)
        if self.exit_button is None:
            self.exit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN_WIDTH * 0.85, SCREEN_HEIGHT * 0.86), (100, 50)),
                                                            text='Quit',
                                                            manager=self.manager)

        if self.alg_one_dropdown is None:
            self.alg_one_dropdown = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect(SCREEN_WIDTH * 0.55, SCREEN_HEIGHT * 0.5, 110, 25),
                                                                       options_list=self.alg_names(),
                                                                       starting_option=self.alg_names()[0],
                                                                       manager=self.manager)

        if self.alg_two_dropdown is None:
            self.alg_two_dropdown = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect(SCREEN_WIDTH * 0.35, SCREEN_HEIGHT * 0.5, 110, 25),
                                                                       options_list=self.alg_names(),
                                                                       starting_option=self.alg_names()[0],
                                                                       manager=self.manager)

    def handle(self, event: pygame.event.Event):
        if event.ui_element == self.start_button:
            self.clear()
            return "PROGRAM"

        elif event.ui_element == self.exit_button:
            pygame.quit()
            sys.exit()

        return "MENU"

    def clear(self):
        self.start_button.kill()
        self.exit_button.kill()
        self.alg_one_dropdown.kill()
        self.alg_two_dropdown.kill()
        self.start_button = None
        self.exit_button = None
        self.alg_one_dropdown = None
        self.alg_two_dropdown = None
