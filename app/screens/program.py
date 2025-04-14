from email._header_value_parser import Section

import pygame
import pygame_gui

from pygame_gui.elements import UIButton, UIPanel, UILabel

from app.facades.algorithm_facade import AlgorithmFacade
from app.objects.graph import Graph
from lib.constants import *


class ProgramScreen:
    def __init__(self, manager: pygame_gui.UIManager):
        self.manager: pygame_gui.UIManager = manager
        self.header_section: UILabel | None = None
        self.run_button: UIButton | None = None
        self.reset_button: UIButton | None = None
        self.exit_button: UIButton | None = None
        self.alg_facade: AlgorithmFacade = AlgorithmFacade()
        self.graphs: [Graph] = []
        # self.solutions: [Solution]
        self.alg_one: str | None = None
        self.alg_two: str | None = None
        self.section_one: UIPanel | None = None
        self.section_two: UIPanel | None = None

    def render(self):
        if self.header_section is None:
            self.header_section = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((SCREEN_WIDTH * 0.0, SCREEN_HEIGHT * 0.0), (SCREEN_WIDTH * 1.0, SCREEN_HEIGHT * 0.065)),
                                                              text=PROGRAM_TXT,
                                                              manager=self.manager)

        if self.alg_one is None:
            self.alg_one = self.alg_facade.names()[0]

        if self.alg_two is None:
            self.alg_two = self.alg_facade.names()[0]

        if self.run_button is None:
            self.run_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN_WIDTH * 0.59, SCREEN_HEIGHT * 0.9), (SCREEN_WIDTH * 0.08, SCREEN_HEIGHT * 0.08)),
                                                           text='Run',
                                                           manager=self.manager)

        if self.reset_button is None:
            self.reset_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN_WIDTH * 0.72, SCREEN_HEIGHT * 0.9), (SCREEN_WIDTH * 0.08, SCREEN_HEIGHT * 0.08)),
                                                             text='Reset',
                                                             manager=self.manager)
        if self.exit_button is None:
            self.exit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN_WIDTH * 0.85, SCREEN_HEIGHT * 0.9), (SCREEN_WIDTH * 0.08, SCREEN_HEIGHT * 0.08)),
                                                            text='Exit',
                                                            manager=self.manager)
        if self.section_one is None:
            self.section_one = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((SCREEN_WIDTH * 0.02, SCREEN_HEIGHT * 0.08), (SCREEN_WIDTH * 0.25, SCREEN_HEIGHT * 0.8)),
                                                           manager=self.manager)

            pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 0), (SCREEN_WIDTH * 0.25, 25)),
                                        text="Runs",
                                        manager=self.manager,
                                        container=self.section_one)

        if self.section_two is None:
            self.section_two = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((SCREEN_WIDTH * 0.28, SCREEN_HEIGHT * 0.08), (SCREEN_WIDTH * 0.70, SCREEN_HEIGHT * 0.8)),
                                                           manager=self.manager)

            pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 0), (SCREEN_WIDTH * 0.70, 25)),
                                        text="Maze",
                                        manager=self.manager,
                                        container=self.section_two)

    def handle(self, event: pygame.event.Event):
        if event.ui_element == self.run_button:
            print(f"run: {self.alg_one}, {self.alg_two}")
        elif event.ui_element == self.reset_button:
            print("reset")
        elif event.ui_element == self.exit_button:
            self.clear()
            return "MENU"

        return "PROGRAM"

    def clear(self):
        self.header_section.kill()
        self.run_button.kill()
        self.reset_button.kill()
        self.exit_button.kill()
        self.section_one.kill()
        self.section_two.kill()
        self.header_section = None
        self.run_button = None
        self.reset_button = None
        self.exit_button = None
        self.section_one = None
        self.section_two = None
        self.alg_one = None
        self.alg_two = None
