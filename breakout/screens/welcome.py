import pygame
from screens import BaseScreen
from components import TextBox
from ..components import Background
from pygame.locals import *


class WelcomeScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sprites = pygame.sprite.Group()
        pygame.mixer.init()
        # music:
        self.bc_music = pygame.mixer.Sound('./audio/music.mp3')
        self.bc_music.play()

        #title:
        self.image_title = pygame.image.load('./images/title.png')
        self.scaled_image_title = pygame.transform.scale(self.image_title, (550, 100))
        # self.rect_title = self.scaled_image_title.get_rect()
        # buttons:
        # self.button_title = TextBox(
        #     (160, 60), "DORI WORLD", color=(0, 0, 0), bgcolor=(179, 236, 255)
        # )
        self.button_start = TextBox(
            (160, 60), "START", color=(0, 0, 0), bgcolor=(255, 255, 255)
        )
        self.button_score = TextBox(
            (160, 60), "SCORE", color=(0, 0, 0), bgcolor=(255,255,255)
        )
        # self.button_title.rect.x = 450
        # self.button_title.rect.y = 150
        self.button_start.rect.x = 250
        self.button_start.rect.y = 400
        self.button_score.rect.x = 650
        self.button_score.rect.y = 400

        self.sprites.add(self.button_start,self.button_score)
        self.background = Background("./images/background/game_background4.jpeg")

    # to set the position of the button:
    def draw(self):
        self.window.fill((255,255,255)) #background color
        self.window.blit(self.background.scaled_image,self.background.rect)
        self.window.blit(self.scaled_image_title, ((255, 150)))
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
                self.bc_music.stop()
                self.running = False

        if event.type == pygame.MOUSEBUTTONDOWN :
            mouse = event.pos
            if self.button_score.rect.collidepoint(mouse):
                print("you click score")
                self.next_screen = "introduction"
                self.running = False
        
