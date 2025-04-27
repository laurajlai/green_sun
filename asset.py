import pygame

# this is the superclass for all game objects. 
class Asset(pygame.sprite.Sprite):
    def __init__(self, pic, og_x, og_y, scale):
        pygame.sprite.Sprite.__init__(self)

        # initialize image, size, & coordinates
        self.image = pygame.image.load(pic).convert_alpha()
        self.size = self.image.get_size()
        self.x = og_x
        self.y = og_y
        self.actual = pygame.transform.scale(self.image, (int(self.size[0]*scale), int(self.size[1]*scale)))
        self.rect = self.actual.get_rect(topleft = (self.x, self.y))

    # changes the coordinates of an Asset
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y
        self.rect = self.actual.get_rect(topleft = (self.x, self.y))

    # checks if 2 Assets have collided (if Player is an Asset, this includes player, huh)
    def generic_collide(self, asset2):
        if self.rect.colliderect(asset2.rect):
            return True
        else:
            return False