import pygame
from components.text import render_text, center_text

COLOR_ACTIVE = pygame.Color((186,200,170))
COLOR_INACTIVE = pygame.Color('black')

class InputBox(pygame.sprite.Sprite):

    def __init__(self, x, y, w, h, text=''):
        super().__init__()
        self.rect = pygame.Rect(x, y, w, h)
        #START WITH TEXT BOX OFF COLOR
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = render_text(self.text, 30, (0, 0, 0))
        self.active = False
        self.entered = ''

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.entered = self.text
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = render_text(self.text, 24, (0, 0, 0))

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

        # what I add
        self.get_text()

    def draw(self, window):
        # Blit the text.
        window.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(window, self.color, self.rect, 2)
    
    def get_text(self):
        return self.text
