import pygame

# Flower class
class Flower(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # flower image
        self.image = pygame.image.load('green_sun_flower.png').convert_alpha()
        self.size = self.image.get_size()
        self.actual = pygame.transform.scale(self.image, (int(self.size[0]), int(self.size[1])))

        # flower coordinates, rectangle
        self.x = 446
        self.y = 400
        self.rect = self.actual.get_rect(topleft = (self.x, self.y))

        # other attributes
        self.taken = False

    # changes the coordinates of a flower
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y
        self.rect = self.actual.get_rect(topleft = (self.x, self.y))

    # function to see if the player collided with a flower
    # if the player collides with a key, set the has_flower and can_double_jump attributes
    # to True
    def flower_collide(self, player):
        if self.rect.colliderect(player.rect):
            player.has_flower = True
            player.can_double_jump = True
            self.taken = True
            return True
        return False