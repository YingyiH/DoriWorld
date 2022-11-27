import pygame
from screens import BaseScreen
from components import TextBox
from ..components import Background


class WelcomeScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sprites = pygame.sprite.Group()
        # buttons:
        self.button_start = TextBox(
            (160, 60), "START", color=(255, 255, 255), bgcolor=(255, 5, 255)
        )
        self.button_score = TextBox(
            (160, 60), "SCORE", color=(255, 255, 255), bgcolor=(255,0,255)
        )
        self.button_start.rect.x = 450
        self.button_start.rect.y = 200
        self.button_score.rect.x = 450
        self.button_score.rect.y = 300

        self.sprites.add(self.button_start,self.button_score)
        self.background = Background("./images/background/game_background4.jpeg")

    # to set the position of the button:
    def draw(self):
        self.window.fill((255,255,255)) #background color
        self.window.blit(self.background.scaled_image,self.background.rect)
        self.sprites.draw(self.window)

    def update(self):
        pass

    def manage_event(self, event):
        print(event)

        if event.type == pygame.MOUSEBUTTONDOWN :
            mouse = event.pos
            if self.button_start.rect.collidepoint(mouse):
                print("you click start")
                self.next_screen = "introduction"
                self.running = False

        if event.type == pygame.MOUSEBUTTONDOWN :
            mouse = event.pos
            if self.button_score.rect.collidepoint(mouse):
                print("you click score")
                self.next_screen = "introduction"
                self.running = False
        
