from app.facades.ui_facade import *
from lib.constants import *

# Initialize Pygame
pygame.init()

# Display Window
pygame.display.set_caption(CAPTION)
display: pygame.Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Background
background = pygame.Surface(display.get_size())
background.fill(WHITE)
display.blit(background, (0, 0))

# Component Manager
manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT), THEME_PATH)
clock = pygame.time.Clock()

# UI
ui = UIFacade(display, manager)


def main():
    while True:
        display.blit(background, (0, 0))
        time_delta = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            match event.type:
                case pygame_gui.UI_BUTTON_PRESSED:
                    ui.handle(event)

                case pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                    ui.select(event)

                case pygame.QUIT:
                    ui.quit()

            manager.process_events(event)

        manager.update(time_delta)
        manager.draw_ui(display)
        ui.render()
        pygame.display.update()


if __name__ == '__main__':
    main()
