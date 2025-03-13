import pygame
from lib.constants import *

PyGameButton = tuple[pygame.Surface, pygame.Rect]


def button(txt: str,
           font: str,
           font_size: int,
           font_color: tuple[[int, int, int]],
           x: float,
           y: float,
           x_padding: int = 0,
           y_padding: int = 0
           ) -> PyGameButton:

    font = pygame.font.SysFont(font, font_size)
    font_surface = font.render(txt, True, font_color)
    font_surface_size = font_surface.get_rect().inflate(x_padding, y_padding).size

    font_rect = font_surface.get_rect(center=(font_surface_size[0] / 2, font_surface_size[1] / 2))

    button_surface = pygame.Surface(font_surface_size)
    button_surface.fill(WHITE)
    button_surface.blit(font_surface, font_rect)

    button_rect = button_surface.get_rect(center=(SCREEN_WIDTH // x, SCREEN_HEIGHT // y))
    return button_surface, button_rect


def render_button(display: pygame.display, button: PyGameButton):
    display.blit(button[0], button[1])
