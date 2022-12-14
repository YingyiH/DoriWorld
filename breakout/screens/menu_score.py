import pygame
from screens import BaseScreen
from components import TextBox
from ..components import Background
from pygame.locals import *
from models.score import Score


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
        score = Score("user.json")
        self.userinfo_text = score.load_from_json()
        if self.userinfo_text["users"] == []:
            self.text_scores = TextBox(
            (800, 230), "Empty", color=(0,0,0), bgcolor=(252,206,172)
        )
        else:
            self.space = 130
            self.history_list = []
            # self.score = self.scores["scores"]
            for item in self.userinfo_text["users"]:
                index = self.userinfo_text["users"].index(item)
                username = item["username"]
                grades = item["grades"]
                self.history_list.append(
                    TextBox(
                        (700, 50), f"{username} ------------------------------------------------------------ {grades}", color=(0,0,0), bgcolor=(252,206,172)
                    ) 
                )
                self.space += 10
                self.history_list[index].rect.x = 100
                self.history_list[index].rect.y = self.space
                self.sprites.add(self.history_list[index])
                self.space += 20
        
        #background:
        self.sprites.add(self.button_menu)
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
        
