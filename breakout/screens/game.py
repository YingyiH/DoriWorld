import random
import pygame
from screens import BaseScreen
from ..components import Background,Character, Projectile, Enemy, Score

from components import TextBox


class GameScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.background = Background("./images/background/game_background2.jpeg")
        self.character = Character()
        self.projectiles = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.sprites = pygame.sprite.Group()
        self.score = Score()

    def update(self):

        self.character.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.character.rect.left = max(self.character.rect.left - 10, 0)
        elif keys[pygame.K_RIGHT]:
            self.character.rect.right = min(self.character.rect.right + 10, 1150)

        if self.character.rect.right > 1100:
            self.running = False
            self.next_screen = "prepare"

        self.projectiles.update()
        self.enemies.update()
        self.manage_enemies()
        self.text_score = TextBox(
            (130, 45), f"SCORE: {self.score.score}", color=(0,0,0), bgcolor=(255,255,255)
        )
        self.sprites.add(self.text_score)

    def draw(self):
        self.window.fill((255, 255, 255))
        self.window.blit(self.background.scaled_image, self.background.rect )
        self.window.blit(self.character.scaled_image, self.character.rect)
        self.text_score.rect.x = 900
        self.text_score.rect.y = 20
        self.sprites.draw(self.window)

        self.projectiles.draw(self.window)
        self.enemies.draw(self.window)

    def manage_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.running = False
            self.next_screen = "welcome"

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.character.jump()
            elif event.key == pygame.K_q:
                projectile = Projectile(self.character.rect.x, self.character.rect.y, -1)
                self.projectiles.add(projectile)
            elif event.key == pygame.K_e:
                projectile = Projectile(self.character.rect.x, self.character.rect.y, 1)
                self.projectiles.add(projectile)

    def manage_enemies(self):
        if random.randrange(0, 100) < 1:
            enemy = Enemy(random.randint(10, 1200), random.randint(-1, 1))
            self.enemies.add(enemy)

        for i in self.projectiles:
            if pygame.sprite.spritecollide(i, self.enemies, dokill=True):
                i.kill()
                self.score.add_score()
