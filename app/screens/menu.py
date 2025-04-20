import sys
import pygame
import pygame_gui

from pygame_gui.elements import UIButton, UIDropDownMenu, UILabel, UIPanel
from app.facades.algorithm_facade import AlgorithmFacade
from lib.constants import *


class MenuScreen:
    """
    Class to hold components and manage state of main menu screen
    """
    def __init__(self, manager: pygame_gui.UIManager):
        self.manager: pygame_gui.UIManager = manager
        self.header_section: UILabel | None = None
        self.footer_section: UIPanel | None = None
        self.dropdown_section: UIPanel | None = None
        self.alg_one_dropdown: UIDropDownMenu | None = None
        self.alg_two_dropdown: UIDropDownMenu | None = None
        self.exit_button: UIButton | None = None
        self.start_button: UIButton | None = None
        self.alg_names: [str] = AlgorithmFacade().names

    def render(self):
        if self.header_section is None:
            self.header_section = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(SCREEN_WIDTH * 0.0,
                                                                                        SCREEN_HEIGHT * 0.0,
                                                                                        SCREEN_WIDTH * 1.0,
                                                                                        SCREEN_HEIGHT * 0.05),
                                                              text=MENU_TXT,
                                                              manager=self.manager)

        if self.dropdown_section is None:
            self.dropdown_section = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect(SCREEN_WIDTH * 0.0,
                                                                                          SCREEN_HEIGHT * 0.05,
                                                                                          SCREEN_WIDTH * 1.0,
                                                                                          SCREEN_HEIGHT * 0.83),
                                                                manager=self.manager)

            self.alg_one_dropdown = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect(SCREEN_WIDTH * 0.35,
                                                                                                 SCREEN_HEIGHT * 0.42,
                                                                                                 110,
                                                                                                 25),
                                                                       options_list=self.alg_names(),
                                                                       starting_option=self.alg_names()[0],
                                                                       manager=self.manager,
                                                                       container=self.dropdown_section)

            self.alg_two_dropdown = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect(SCREEN_WIDTH * 0.55,
                                                                                                 SCREEN_HEIGHT * 0.42,
                                                                                                 110,
                                                                                                 25),
                                                                       options_list=self.alg_names(),
                                                                       starting_option=self.alg_names()[0],
                                                                       manager=self.manager,
                                                                       container=self.dropdown_section)

        if self.start_button is None:
            self.start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(SCREEN_WIDTH * 0.72,
                                                                                       SCREEN_HEIGHT * 0.9,
                                                                                       SCREEN_WIDTH * 0.08,
                                                                                       SCREEN_HEIGHT * 0.08),
                                                             text='Start',
                                                             manager=self.manager)

        if self.exit_button is None:
            self.exit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(SCREEN_WIDTH * 0.85,
                                                                                      SCREEN_HEIGHT * 0.9,
                                                                                      SCREEN_WIDTH * 0.08,
                                                                                      SCREEN_HEIGHT * 0.08),
                                                            text='Quit',
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
        self.header_section.kill()
        self.start_button.kill()
        self.exit_button.kill()
        self.dropdown_section.kill()
        self.header_section = None
        self.start_button = None
        self.exit_button = None
        self.dropdown_section = None
