import random
import pygame
from screens import BaseScreen
from ..components import Background,Character, Projectile, Enemy, InputBox
from models.score import Score
import requests

from components import TextBox


class GameScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.background = Background("./images/background/game_background2.jpeg")
        self.character = Character()
        self.projectiles = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.sprites = pygame.sprite.Group()
        self.time = 60
        self.score = 0
        self.user = "unknown"
        pygame.mixer.init()
        
        

    def update(self):

        self.character.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.character.rect.left = max(self.character.rect.left - 5, 0)
        elif keys[pygame.K_RIGHT]:
            self.character.rect.right = min(self.character.rect.right + 5, 1000)

        self.projectiles.update()
        self.enemies.update()
        self.manage_enemies()
        self.time -= 1/60
        # self.time = 60 - int(pygame.time.get_ticks()/1000)
 
        self.text_score = TextBox(
            (130, 45), f"SCORE: {self.score}", color=(0,0,0), bgcolor=(255,255,255)
        )
        self.text_time = TextBox(
            (130, 45), f"TIME: {int(self.time)}", color=(0,0,0), bgcolor=(255,255,255)
        )
        self.sprites.add(self.text_score,self.text_time)

    def draw(self):
        self.window.fill((255, 255, 255))
        self.window.blit(self.background.scaled_image, self.background.rect )
        self.window.blit(self.character.scaled_image, self.character.rect)
        self.text_score.rect.x = 900
        self.text_score.rect.y = 20
        self.text_time.rect.x = 900
        self.text_time.rect.y = 80
        self.sprites.draw(self.window)

        self.projectiles.draw(self.window)
        self.enemies.draw(self.window)

        # if self.time <= 0:
        #     self.running = False
        #     self.next_screen = "gameover"

    def manage_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                self.running = False
                self.next_screen = "welcome"

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.character.jump()
                pygame.mixer.music.load('./audio/axe.mp3')
                pygame.mixer.music.play(1)
            elif event.key == pygame.K_q:
                pygame.mixer.music.load('./audio/success.wav')
                pygame.mixer.music.play(1)
                projectile = Projectile(self.character.rect.x, self.character.rect.y, -1)
                self.projectiles.add(projectile)
            elif event.key == pygame.K_e:
                pygame.mixer.music.load('./audio/success.wav')
                pygame.mixer.music.play(1)
                projectile = Projectile(self.character.rect.x, self.character.rect.y, 1)
                self.projectiles.add(projectile)

    def manage_enemies(self):
        if random.randrange(0, 13) < 1:
            enemy = Enemy(random.randint(10, 900), random.randint(-1, 1))
            self.enemies.add(enemy)

        for item in self.projectiles:
            if pygame.sprite.spritecollide(item, self.enemies, dokill=True):
                item.kill()
                self.score += 1
        
        if pygame.sprite.spritecollide(self.character, self.enemies, dokill=False):
            self.character.kill()
            self.scores["scores"] = self.score
            self.user = self.scores["username"]
            # post request:
            Flask_url = "http://127.0.0.1:5000/user/add"
            data = {
                "username": self.user,
                "grades": self.score
            }
            requests.post(Flask_url,json=data)
            print("uploaded")
                
            self.running = False
            self.next_screen = "gameover"

        elif self.time <= 0:
            self.scores["scores"] = self.score
            self.user = self.scores["username"]
            # post request:
            Flask_url = "http://127.0.0.1:5000/user/add"
            data = {
                "username": self.user,
                "grades": self.score
            }
            requests.post(Flask_url,json=data)
            print("uploaded")
                
            self.running = False
            self.next_screen = "gameover"