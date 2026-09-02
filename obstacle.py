import pygame

class block(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((255, 0, 0))  # Red color for the block
        self.rect = self.image.get_rect(topleft=(x, y))   