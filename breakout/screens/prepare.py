import random
import pygame
from screens import BaseScreen
from ..components import Background,Character, Projectile, IntroText

from components import TextBox


class PrepareScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.background = Background("./images/background/game_background1.jpeg")
        self.character = Character()
        self.projectiles = pygame.sprite.Group()
        self.sprites = pygame.sprite.Group()
        self.text = IntroText()

        #Sign for game.py
        self.image_sign = pygame.image.load('./images/DoNotCross.png')
        self.scaled_image_sign = pygame.transform.scale(self.image_sign, (70, 100))

        # Music:
        pygame.mixer.init()
        self.bc_music = pygame.mixer.Sound('./audio/success.wav')

    def update(self):
        self.character.update()
        self.projectiles.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.character.rect.left = max(self.character.rect.left - 10, 0)
        elif keys[pygame.K_RIGHT]:
            self.character.rect.right = min(self.character.rect.right + 10, 1150)

        if self.character.rect.right > 1100:
            self.running = False
            self.next_screen = "game"

        # text hints:
        self.font = pygame.font.Font('./font/LycheeSoda.ttf', 32)
        self.text_hint = self.font.render(self.text.hint, True, (0,0,0))
        self.text_jump = self.font.render(self.text.jump, True, (255,255,255))
        self.text_move = self.font.render(self.text.move, True, (255,255,255))
        self.text_shoot = self.font.render(self.text.shoot, True, (255,255,255))

    def draw(self):
        self.window.fill((255, 255, 255))
        self.window.blit(self.background.scaled_image, self.background.rect )
        self.window.blit(self.scaled_image_sign, (900, 350))
        self.window.blit(self.character.scaled_image, self.character.rect)
        self.projectiles.draw(self.window)
        self.window.blit(self.text_hint,((760,300)))
        self.window.blit(self.text_move,((150,50)))
        self.window.blit(self.text_jump,((150,100)))
        self.window.blit(self.text_shoot,((150,150)))

    def manage_event(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if self.character.rect.bottom < 300:
                    pass
                else:
                    self.character.jump()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                self.running = False
                self.next_screen = "welcome"

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.character.jump()
            elif event.key == pygame.K_q:
                self.bc_music.play()
                projectile = Projectile(self.character.rect.x, self.character.rect.y, -1)
                self.projectiles.add(projectile)
            elif event.key == pygame.K_e:
                self.bc_music.play()
                projectile = Projectile(self.character.rect.x, self.character.rect.y, 1)
                self.projectiles.add(projectile)

        

        
