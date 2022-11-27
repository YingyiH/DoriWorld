import pygame
from screens import BaseScreen
from components import TextBox
from ..components import Background


class LevelScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sprites = pygame.sprite.Group()
        # buttons:
        self.button_level1 = TextBox(
            (130, 100), "1", color=(0,0,0), bgcolor=(255, 255, 255,0)
        )
        self.button_level2 = TextBox(
            (100, 45), "2", color=(255, 255, 255), bgcolor=(0,0,0)
        )
        self.sprites.add(self.button_level1,self.button_level2)
        self.background = Background("./images/background/levels.jpeg")

    # to set the position of the button:
    def draw(self):
        self.window.fill((255,255,255)) #background color
        self.window.blit(self.background.scaled_image,self.background.rect)
        self.button_level1.rect.x = 260
        self.button_level1.rect.y = 150
        self.button_level2.rect.x = 920
        self.button_level2.rect.y = 480
        self.sprites.draw(self.window)

    def update(self):
        pass

    def manage_event(self, event):
        print(event)

        if event.type == pygame.MOUSEBUTTONDOWN :
            mouse = event.pos
            if self.button_level1.rect.collidepoint(mouse):
                print("you click start")
                self.next_screen = "prepare"
                self.running = False

        if event.type == pygame.MOUSEBUTTONDOWN :
            mouse = event.pos
            if self.button_level2.rect.collidepoint(mouse):
                print("you click score")
                self.next_screen = "prepare"
                self.running = False
