import pygame

# Key class
class Key(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # key image
        self.image = pygame.image.load('green_sun_key.png').convert_alpha()
        self.size = self.image.get_size()
        self.actual = pygame.transform.scale(self.image, (int(self.size[0]*0.6), int(self.size[1]*0.6)))

        # key coordinates, rectangle
        self.x = 650
        self.y = 420
        self.rect = self.actual.get_rect(topleft = (self.x, self.y))
    
    # changes the coordinates of a Key object (needed because there are multiple blocks)
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y
        self.rect = self.actual.get_rect(topleft = (self.x, self.y))
    
    # function to see if the player collided with a key
    # if the player collides with a key, set the has_key attribute to True
    def key_collide(self, player):
        if self.rect.colliderect(player.rect):
            player.has_key = True
            return True
        return False
