import sys
import re
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

    def render(self, display: pygame.Surface):
        if self.state == 'MENU':
            self.menu_screen.render()
        elif self.state == 'PROGRAM':
            self.program_screen.render(display)

    def handle(self, event: pygame.event.Event):
        if self.state == 'MENU':
            self.state = self.menu_screen.handle(event)
        elif self.state == 'PROGRAM':
            self.state = self.program_screen.handle(event)

    def select_alg(self, event: pygame.event.Event):
        if event.ui_element == self.menu_screen.alg_one_dropdown:
            self.program_screen.alg_one = event.text
        elif event.ui_element == self.menu_screen.alg_two_dropdown:
            self.program_screen.alg_two = event.text

    def select_run(self, event: pygame.event.Event):
        if event.ui_object_id == 'panel.drop_down_menu.#drop_down_options_list':
            return
        run = re.search(r'Run (\d+)', event.text)
        if (run):
            self.program_screen.selected_solution = int(run.group(1))
        self.program_screen.rerender_maze()
        self.program_screen.rerender_results()

    @staticmethod
    def quit():
        pygame.quit()
        sys.exit()
