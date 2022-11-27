import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, side):
        super().__init__()
        self.side = side
        # load the image:
        self.image = pygame.image.load('./images/projectile/mushroom.png')
        self.scaled_image = pygame.transform.scale(self.image, (1,1))
        self.rect = self.scaled_image.get_rect()
        self.rect.x = x + 10
        self.rect.y = y + 30
 

    # def draw(self,win):
    #     pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)

    def update(self):
        self.rect.x += 10 * self.side