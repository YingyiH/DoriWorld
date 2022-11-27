import random
import pygame
from screens import BaseScreen
from ..components import Background,Character

from components import TextBox


class GameScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.background = Background("./images/background/game_background1.jpeg")
        #Doris character
        self.character = Character()

    def update(self):
        self.character.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.character.rect.left = max(self.character.rect.left - 10, 0)
            self.image = pygame.image.load('./images/character/3.png')
        elif keys[pygame.K_RIGHT]:
            self.character.rect.right = min(self.character.rect.right + 10, 1150)
            self.image = pygame.image.load('./images/character/1.png')

        if self.character.rect.right > 1100:
            self.running = False
            self.next_screen = "next_game"

    def draw(self):
        self.window.fill((255, 255, 255))
        self.window.blit(self.background.scaled_image, self.background.rect )
        self.window.blit(self.character.scaled_image, self.character.rect)
        # self.sprites.draw(self.window)
        # self.tiles.draw(self.window)

    def manage_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.running = False
            self.next_screen = "welcome"

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if self.character.rect.bottom < 300:
                    pass
                else:
                    self.character.jump()

        
