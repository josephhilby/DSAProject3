from lib.constraints import *
from app.facades.ui_facade import *

# Display Window
pygame.init()
pygame.display.set_caption(CAPTION)
display: pygame.Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# UI
ui = UIFacade(display)

# State
menu = "MENU"

def main():
    while True:
        ui.render(menu)
        pygame.display.update()

        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    ui.quit()


if __name__ == '__main__':
    main()
