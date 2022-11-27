import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./images/character/0.png')
        self.scaled_image = pygame.transform.scale(self.image, (30, 45))
        self.rect = self.scaled_image.get_rect()
        self.rect.x = 100
        self.rect.y = 450
        self.gravity = 0.02
            
    def update(self):
        if self.rect.y < 400:
            self.rect.y += self.rect.y * self.gravity

    def jump(self):
        if self.rect.y < 400:
            pass
        else:
            self.rect.y -= 100