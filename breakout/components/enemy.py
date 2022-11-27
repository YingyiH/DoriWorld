import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, side):
        super().__init__()
        self.side = side
        # load the image:
        self.image = pygame.image.load('./images/character/merchant.png')
        self.scaled_image = pygame.transform.scale(self.image, (30,45))
        self.rect = self.scaled_image.get_rect()
        self.rect.x = x
        self.rect.y = 5
 

    # def draw(self,win):
    #     pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)

    def update(self):
        # self.rect.y += self.rect.y * 0.1
        self.rect.y += 5

        if self.rect.y > 420:
            self.rect.y = 420
        if self.rect.y == 420:
            self.rect.x += 2 * self.side
        if self.rect.x <= 0:
            self.side *= -1
        if self.rect.x >= 950:
            self.rect.x *= -1