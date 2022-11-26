import pygame


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location=[0, 0]):
        #[0,0] is location top left screen so it fills everything
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.image.load(image_file)
        self.scaled_image = pygame.transform.scale(self.image, (1050, 550))
        self.rect = self.scaled_image.get_rect()
        self.rect.left, self.rect.top = location