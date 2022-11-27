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


        # buttons:
        self.button_start = TextBox(
            (160, 60), "START", color=(0, 0, 0), bgcolor=(255, 255, 255)
        )
        self.button_score = TextBox(
            (160, 60), "SCORE", color=(0, 0, 0), bgcolor=(255,255,255)
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
                self.bc_music.stop()
                self.running = False

        if event.type == pygame.MOUSEBUTTONDOWN :
            mouse = event.pos
            if self.button_score.rect.collidepoint(mouse):
                print("you click score")
                self.next_screen = "introduction"
                self.running = False
        
