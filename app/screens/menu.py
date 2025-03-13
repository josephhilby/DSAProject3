from app.components.text import *

class MenuScreen:
    def __init__(self):
        self.header_text: PyGameText | None = None

    def render(self, display: pygame.display):
        display.fill(BG_COLOR)
