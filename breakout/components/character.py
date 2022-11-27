import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./images/character/0.png')
        self.scaled_image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.scaled_image.get_rect()
        self.rect.x = 200
        self.rect.y = 400
        self.gravity = 0.02
            
    def update(self):
        if self.rect.y < 400:
            self.rect.y += self.rect.y * self.gravity

    def jump(self):
        self.rect.y -= 100