from app.components.text import *

class MenuScreen:
    def __init__(self):
        self.header_text: PyGameText | None = None

    def render(self, display: pygame.display):
        display.fill(BG_COLOR)
        self.header_text = text(MENU_TXT, DEFAULT_FONT, MENU_FONT_SIZE, BLACK, 2, 20)
        render_text(display, self.header_text)
