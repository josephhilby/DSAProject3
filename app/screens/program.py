import re
import pygame
import pygame_gui

from pygame_gui.elements import UIButton, UIPanel, UILabel

from app.facades.algorithm_facade import AlgorithmFacade
from app.objects.graph import Graph
from lib.constants import *


class ProgramScreen:
    """
    Class to hold components and manage state of program screen
    """
    def __init__(self, manager: pygame_gui.UIManager):
        self.manager: pygame_gui.UIManager = manager
        self.alg_facade: AlgorithmFacade = AlgorithmFacade()
        self.solutions: list[{str: (int, int)}] = []
        self.selected_solution: int = 1
        self.alg_one: str | None = None
        self.alg_one_sum: int = 0
        self.alg_two: str | None = None
        self.alg_two_sum: int = 0
        self.maze_rect: pygame.Rect | None = None
        self.header_section: UILabel | None = None
        self.section_one: UIPanel | None = None
        self.section_two: UIPanel | None = None
        self.section_three: UIPanel | None = None
        self.run_button: UIButton | None = None
        self.reset_button: UIButton | None = None
        self.exit_button: UIButton | None = None

    def render(self, display: pygame.Surface):
        if self.header_section is None:
            self.header_section = pygame_gui.elements.UILabel(
                manager=self.manager,
                text=PROGRAM_TXT,
                relative_rect=pygame.Rect(
                    SCREEN_WIDTH * 0.00, SCREEN_HEIGHT * 0.00,
                    SCREEN_WIDTH * 1.00, SCREEN_HEIGHT * 0.05
                )
            )

        if self.alg_one is None:
            self.alg_one = self.alg_facade.names()[1]

        if self.alg_two is None:
            self.alg_two = self.alg_facade.names()[0]

        if self.run_button is None:
            self.run_button = pygame_gui.elements.UIButton(
                manager=self.manager,
                text='Run',
                relative_rect=pygame.Rect(
                    SCREEN_WIDTH * 0.59, SCREEN_HEIGHT * 0.90,
                    SCREEN_WIDTH * 0.08, SCREEN_HEIGHT * 0.08
                )
            )

        if self.reset_button is None:
            self.reset_button = pygame_gui.elements.UIButton(
                manager=self.manager,
                text='Reset',
                relative_rect=pygame.Rect(
                    SCREEN_WIDTH * 0.72, SCREEN_HEIGHT * 0.90,
                    SCREEN_WIDTH * 0.08, SCREEN_HEIGHT * 0.08
                )
            )

        if self.exit_button is None:
            self.exit_button = pygame_gui.elements.UIButton(
                manager=self.manager,
                text='Exit',
                relative_rect=pygame.Rect(
                    SCREEN_WIDTH * 0.85, SCREEN_HEIGHT * 0.90,
                    SCREEN_WIDTH * 0.08, SCREEN_HEIGHT * 0.08
                )
            )

        if self.section_one is None:
            self.section_one = pygame_gui.elements.UIPanel(
                manager=self.manager,
                relative_rect=pygame.Rect(
                    SCREEN_WIDTH * 0.02, SCREEN_HEIGHT * 0.05,
                    SCREEN_WIDTH * 0.40, SCREEN_HEIGHT * 0.50
                )
            )

            pygame_gui.elements.UILabel(
                manager=self.manager,
                container=self.section_one,
                text="Runs",
                relative_rect=pygame.Rect(
                    SCREEN_WIDTH * 0.00, SCREEN_HEIGHT * 0.00,
                    SCREEN_WIDTH * 0.40, 25
                )
            )

            pygame_gui.elements.UISelectionList(
                manager=self.manager,
                container=self.section_one,
                item_list=[f"Run {i}" for i in range(1, len(self.solutions) + 1)],
                relative_rect=pygame.Rect(
                    SCREEN_WIDTH * 0.00, 25,
                    SCREEN_WIDTH * 0.40 - 6, SCREEN_HEIGHT * 0.50 - 31
                )
            )

        if self.section_two is None:
            self.section_two = pygame_gui.elements.UIPanel(
                manager=self.manager,
                relative_rect=pygame.Rect(
                    SCREEN_WIDTH * 0.435, SCREEN_HEIGHT * 0.050,
                    SCREEN_WIDTH * 0.545, SCREEN_HEIGHT * 0.845
                )
            )

            pygame_gui.elements.UILabel(
                manager=self.manager,
                container=self.section_two,
                text=f"Maze for Run {self.selected_solution}",
                relative_rect=pygame.Rect(
                    SCREEN_WIDTH * 0.000, SCREEN_HEIGHT * 0.0,
                    SCREEN_WIDTH * 0.545, 25
                )
            )

        if self.section_three is None and len(self.solutions) > 0:
            self.section_three = pygame_gui.elements.UIPanel(
                manager=self.manager,
                relative_rect=pygame.Rect(
                    SCREEN_WIDTH * 0.02, SCREEN_HEIGHT * 0.55,
                    SCREEN_WIDTH * 0.40, SCREEN_HEIGHT * 0.43
                )
            )

            alg_one_steps = len(self.solutions[self.selected_solution-1][self.alg_one])
            alg_two_steps = len(self.solutions[self.selected_solution-1][self.alg_two])
            alg_one_avg = self.alg_one_sum/len(self.solutions)
            alg_two_avg = self.alg_two_sum/len(self.solutions)

            text = f"""
            <b>Run {self.selected_solution}</b>
            <p>{self.alg_one}: Steps {alg_one_steps}
            {self.alg_two}: Steps {alg_two_steps}
            {self.alg_one} was {alg_one_steps/alg_two_steps:.2f} times the speed of {self.alg_two}</p>
            <b>Expected Values</b>
            <p>{self.alg_one}: {alg_one_avg: .2f}
            {self.alg_two}: {alg_two_avg: .2f}
            {self.alg_one} averages {alg_one_avg/alg_two_avg:.2f} times the speed of {self.alg_two}</p>
            """

            pygame_gui.elements.UITextBox(
                manager=self.manager,
                container=self.section_three,
                html_text=text,
                relative_rect=pygame.Rect(
                    SCREEN_WIDTH * 0.00, SCREEN_HEIGHT * 0.00,
                    SCREEN_WIDTH * 0.40 - 6, SCREEN_HEIGHT * 0.43 - 6
                )
            )

        if self.maze_rect is None:
            self.maze_rect = pygame.Rect(
                SCREEN_WIDTH * 0.435 + 6, SCREEN_HEIGHT * 0.05 + 30,
                641, 641
            )

        pygame.draw.rect(display, WHITE, self.maze_rect)
        pygame.draw.rect(display, BLACK, self.maze_rect, width=1)

        if len(self.solutions) > 0:
            alg_one_solution = self.solutions[self.selected_solution-1][self.alg_one]
            alg_two_solution = self.solutions[self.selected_solution-1][self.alg_two]
            pygame.draw.lines(display, (255, 0, 0), False, alg_one_solution, 1)
            pygame.draw.lines(display, (0, 0, 255), False, alg_two_solution, 1)

    def rerender_maze(self):
        if self.section_two is not None:
            self.section_two.kill()
            self.section_two = None

    def rerender_results(self):
        if self.section_three is not None:
            self.section_three.kill()
            self.section_three = None

    def handle(self, event: pygame.event.Event) -> str:
        if event.ui_element == self.run_button:
            graph = Graph()
            graph.generate_maze()
            nodes = graph.nodes
            top = self.maze_rect.top
            left = self.maze_rect.left
            solution = {self.alg_one: self.alg_facade.plot(nodes, self.alg_one, 640, top, left),
                        self.alg_two: self.alg_facade.plot(nodes, self.alg_two, 640, top, left)}
            self.solutions.append(solution)
            self.alg_one_sum += len(self.solutions[-1][self.alg_one])
            self.alg_two_sum += len(self.solutions[-1][self.alg_two])
            self.section_one.kill()
            self.section_one = None
            self.rerender_results()

        elif event.ui_element == self.reset_button:
            self.solutions = []
            self.alg_one_sum = 0
            self.alg_two_sum = 0
            self.section_one.kill()
            self.section_one = None
            self.selected_solution = 1
            self.rerender_maze()
            self.rerender_results()

        elif event.ui_element == self.exit_button:
            self.clear()
            return "MENU"

        return "PROGRAM"

    def select_run(self, event: pygame.event.Event):
        run = re.search(r'Run (\d+)', event.text)

        if run:
            self.selected_solution = int(run.group(1))

        self.rerender_maze()
        self.rerender_results()

    def clear(self):
        self.header_section.kill()
        self.run_button.kill()
        self.reset_button.kill()
        self.exit_button.kill()
        self.section_one.kill()

        if self.section_two is not None:
            self.section_two.kill()

        if self.section_three is not None:
            self.section_three.kill()

        self.header_section = None
        self.run_button = None
        self.reset_button = None
        self.exit_button = None
        self.section_one = None
        self.section_two = None
        self.section_three = None
        self.alg_one = None
        self.alg_two = None
        self.maze_rect = None
        self.solutions = []
        self.selected_solution = 1
