import pygame
from lib.constraints import *

PyGameText = tuple[pygame.Surface, pygame.Rect]


def text(txt: str,
         font: str,
         font_size: int,
         font_color: tuple[[int, int, int]],
         x: float,
         y: float,
         x_padding: int = 0,
         y_padding: int = 0
         ) -> PyGameText:

    font = pygame.font.SysFont(font, font_size)
    font_surface = font.render(txt, True, font_color)
    font_surface_size = font_surface.get_rect().inflate(x_padding, y_padding).size

    font_rect = font_surface.get_rect(center=(font_surface_size[0] / 2, font_surface_size[1] / 2))

    button_surface = pygame.Surface(font_surface_size)
    button_surface.fill(BG_COLOR)
    button_surface.blit(font_surface, font_rect)

    button_rect = button_surface.get_rect(center=(SCREEN_WIDTH // x, SCREEN_HEIGHT // y))
    return button_surface, button_rect


def render_text(display: pygame.display, text: PyGameText):
    display.blit(text[0], text[1])
