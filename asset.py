import pygame

class Asset(pygame.sprite.Sprite):
    def __init__(self, pic, og_x, og_y):
        super().__init__()

        # initialize image, size, & coordinates
        self.image = pygame.image.load(pic).convert_alpha()
        self.size = self.image.get_size()
        self.x = og_x
        self.y = og_y

        self.rect = self.actual.get_rect(topleft = (self.x, self.y))

    # changes the coordinates of an Asset
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y
        self.rect = self.actual.get_rect(topleft = (self.x, self.y))