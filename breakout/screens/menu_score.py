import pygame
from screens import BaseScreen
from components import TextBox
from ..components import Background
from pygame.locals import *


class MenuScoreScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sprites = pygame.sprite.Group()
        pygame.font.init()
        self.score = 0

        # title:
        self.image_title = pygame.image.load('./images/title.png')
        self.scaled_image_title = pygame.transform.scale(self.image_title, (250, 50))
        # buttons:
        self.button_menu = TextBox(
            (120, 50), "MENU", color=(0, 0, 0), bgcolor=(255,255,255)
        )
        self.button_menu.rect.x = 900
        self.button_menu.rect.y = 460

        # score text:
        if self.scores == {}:
            self.text_scores = TextBox(
            (800, 230), "Empty", color=(0,0,0), bgcolor=(252,206,172)
        )
        else:
            
            self.score = self.scores["scores"]
            self.text_scores = TextBox(
                (700, 50), f"score: --------------------------------------------------- {self.score}", color=(0,0,0), bgcolor=(252,206,172)
            )
        self.text_scores.rect.x = 100
        self.text_scores.rect.y = 130
        
        #background:
        self.sprites.add(self.button_menu,self.text_scores)
        self.background = Background("./images/background/game_background5.jpeg")

    def update(self):
        pass

    # to set the position of the button:
    def draw(self):
        self.window.fill((255,255,255)) #background color
        self.window.blit(self.background.scaled_image,self.background.rect)
        self.window.blit(self.scaled_image_title, ((60, 60)))
        self.sprites.draw(self.window)

    def manage_event(self, event):
        print(event)

        if event.type == pygame.MOUSEBUTTONDOWN :
            mouse = event.pos
            if self.button_menu.rect.collidepoint(mouse):
                print("you click score")
                self.next_screen = "welcome"
                self.running = False
        
