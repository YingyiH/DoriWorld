import pygame
from screens import BaseScreen
from components import TextBox
from ..components import Background


class IntroScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sprites = pygame.sprite.Group()
        # buttons:
        self.button_skip = TextBox(
            (100, 45), "SKIP", color=(255, 255, 255), bgcolor=(0, 0, 0)
        )
        self.button_next = TextBox(
            (100, 45), "NEXT", color=(255, 255, 255), bgcolor=(0,0,0)
        )

        self.sprites.add(self.button_skip,self.button_next)
        self.background = Background("./images/background/game_background1.jpeg")

    # to set the position of the button:
    def draw(self):
        self.window.fill((255,255,255)) #background color
        self.window.blit(self.background.scaled_image,self.background.rect)
        self.button_skip.rect.x = 920
        self.button_skip.rect.y = 20
        self.button_next.rect.x = 920
        self.button_next.rect.y = 480
        self.sprites.draw(self.window)

    def update(self):
        pass

    def manage_event(self, event):
        print(event)

        if event.type == pygame.MOUSEBUTTONDOWN :
            mouse = event.pos
            if self.button_skip.rect.collidepoint(mouse):
                print("you click start")
                self.next_screen = "game"
                self.running = False

        if event.type == pygame.MOUSEBUTTONDOWN :
            mouse = event.pos
            if self.button_next.rect.collidepoint(mouse):
                print("you click score")
                self.next_screen = "game"
                self.running = False
