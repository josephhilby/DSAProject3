from app.components.text import *
from app.components.button import *

class MenuScreen:
    def __init__(self):
        self.header_text: PyGameText | None = None
        self.start_button: PyGameButton | None = None

    def render(self, display: pygame.display):
        display.fill(BG_COLOR)
        self.header_text = text(MENU_TXT, DEFAULT_FONT, MENU_FONT_SIZE, BLACK, 2, 20)
        render_text(display, self.header_text)

        self.start_button = button("Start", DEFAULT_FONT, BUTTON_FONT_SIZE, BLACK, 1.3, 1.075)
        render_button(display, self.start_button)

        self.exit_button = button("Exit", DEFAULT_FONT, BUTTON_FONT_SIZE, BLACK, 1.1, 1.075)
        render_button(display, self.exit_button)