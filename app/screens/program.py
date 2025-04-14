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
        self.solutions: [{str: (int, int)}] = []
        self.maze_rect: pygame.Rect | None = None
        self.alg_one: str | None = None
        self.alg_two: str | None = None
        self.section_one: UIPanel | None = None
        self.section_two: UIPanel | None = None

    def render(self, display: pygame.Surface):
        if self.header_section is None:
            self.header_section = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((SCREEN_WIDTH * 0.0, SCREEN_HEIGHT * 0.0), (SCREEN_WIDTH * 1.0, SCREEN_HEIGHT * 0.05)),
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
            self.section_one = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((SCREEN_WIDTH * 0.02, SCREEN_HEIGHT * 0.05), (SCREEN_WIDTH * 0.40, SCREEN_HEIGHT * 0.845)),
                                                           manager=self.manager)

            pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 0), (SCREEN_WIDTH * 0.40, 25)),
                                        text="Runs",
                                        manager=self.manager,
                                        container=self.section_one)

        if self.section_two is None:
            self.section_two = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((SCREEN_WIDTH * 0.435, SCREEN_HEIGHT * 0.05), (SCREEN_WIDTH * 0.545, SCREEN_HEIGHT * 0.845)),
                                                           manager=self.manager)

            pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 0), (SCREEN_WIDTH * 0.545, 25)),
                                        text="Maze",
                                        manager=self.manager,
                                        container=self.section_two)

        if self.maze_rect is None:
            self.maze_rect = pygame.Rect((SCREEN_WIDTH * 0.435 + 7, SCREEN_HEIGHT * 0.05 + 30), (641, 641))

        pygame.draw.rect(display, WHITE, self.maze_rect)
        pygame.draw.rect(display, BLACK, self.maze_rect, width=1)
        if self.solutions:
            pygame.draw.lines(display, (0, 255, 0), False, self.solutions[0][self.alg_one], 2)
            pygame.draw.lines(display, (0, 0, 255), False, self.solutions[0][self.alg_two], 2)


    def handle(self, event: pygame.event.Event):
        if event.ui_element == self.run_button:
            graph = Graph()
            graph.generate_maze()
            nodes = graph.nodes
            top = self.maze_rect.top
            left = self.maze_rect.left
            solution = {self.alg_one: self.alg_facade.plot(nodes, self.alg_one, 640, top, left),
                        self.alg_two: self.alg_facade.plot(nodes, self.alg_two, 640, top, left)}
            self.solutions.append(solution)
        elif event.ui_element == self.reset_button:
            self.solutions = []
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
        self.maze_rect = None
        self.solutions = []
