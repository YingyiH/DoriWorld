import pygame
from screens import BaseScreen
from components import TextBox
from ..components import Background
from pygame.locals import *


class GameOverScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sprites = pygame.sprite.Group()
        pygame.mixer.init()
        pygame.font.init()

        self.score = self.scores["scores"]

        # music:
        self.bc_music = pygame.mixer.Sound('./audio/music.mp3')
        self.bc_music.play()


        # title:
        self.image_title = pygame.image.load('./images/title.png')
        self.scaled_image_title = pygame.transform.scale(self.image_title, (250, 50))
        # score:
        self.font = pygame.font.Font('./font/LycheeSoda.ttf', 64)
        self.text_score = self.font.render(f"Score:  {self.score}", True, (0,0,0))
        # buttons:
        self.button_start = TextBox(
            (160, 60), "Again", color=(0, 0, 0), bgcolor=(255, 255, 255)
        )
        self.button_menu = TextBox(
            (160, 60), "MENU", color=(0, 0, 0), bgcolor=(255,255,255)
        )
        self.button_start.rect.x = 250
        self.button_start.rect.y = 400
        self.button_menu.rect.x = 650
        self.button_menu.rect.y = 400
        #background:
        self.sprites.add(self.button_start,self.button_menu)
        self.background = Background("./images/background/score_background.jpeg")

    # to set the position of the button:
    def draw(self):
        self.window.fill((255,255,255)) #background color
        self.window.blit(self.background.scaled_image,self.background.rect)
        self.window.blit(self.scaled_image_title, ((255, 150)))
        self.sprites.draw(self.window)
        self.window.blit(self.text_score,((270,260)))

    def update(self):
        pass

    def manage_event(self, event):
        print(event)

        if event.type == pygame.MOUSEBUTTONDOWN :
            mouse = event.pos
            if self.button_start.rect.collidepoint(mouse):
                print("you click start")
                self.next_screen = "game"
                self.bc_music.stop()
                self.running = False

        if event.type == pygame.MOUSEBUTTONDOWN :
            mouse = event.pos
            if self.button_menu.rect.collidepoint(mouse):
                print("you click score")
                self.next_screen = "welcome"
                self.bc_music.stop()
                self.running = False
        
