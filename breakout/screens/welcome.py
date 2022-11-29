import pygame
from screens import BaseScreen
from components import TextBox
from ..components import Background,InputBox
from pygame.locals import *
from models.score import Score


class WelcomeScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sprites = pygame.sprite.Group()
        pygame.mixer.init()
        pygame.font.init()
        self.user = "unknown"

        # music:
        self.bc_music = pygame.mixer.Sound('./audio/music.mp3')
        self.bc_music.play()

        #title:
        self.image_title = pygame.image.load('./images/title.png')
        self.scaled_image_title = pygame.transform.scale(self.image_title, (550, 100))
        self.button_start = TextBox(
            (160, 60), "START", color=(0, 0, 0), bgcolor=(255, 255, 255)
        )
        self.button_score = TextBox(
            (160, 60), "SCORE", color=(0, 0, 0), bgcolor=(255,255,255)
        )
        self.font = pygame.font.Font('./font/LycheeSoda.ttf', 40)
        self.text_login = self.font.render(f"LOGIN :", True, (0,0,0))
        self.input_box = InputBox(500, 270, 200, 40, '')

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
        self.window.blit(self.text_login,((350,270)))
        self.input_box.draw(self.window)
        
    def update(self):
        self.input_box.update()

    def manage_event(self, event):
        print(event)

        if event.type == pygame.MOUSEBUTTONDOWN :
            mouse = event.pos
            if self.button_start.rect.collidepoint(mouse):
                print("you click start")
                self.next_screen = "prepare"
                self.bc_music.stop()
                # get user input
                self.user = self.input_box.get_text()
                if self.user == "":
                    self.scores["username"] = "unknown"
                else:
                    self.scores["username"] = self.user
                score = Score("user.json")
                score.add_user(self.user,[])
                score.save()
                self.running = False

        if event.type == pygame.MOUSEBUTTONDOWN :
            mouse = event.pos
            if self.button_score.rect.collidepoint(mouse):
                print("you click score")
                self.next_screen = "menuscore"
                self.bc_music.stop()
                self.running = False
        
        self.input_box.handle_event(event)


        
        
