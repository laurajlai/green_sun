import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # button image
        self.image = pygame.image.load('green_sun_button.png').convert_alpha()
        self.size = self.image.get_size()
        self.actual = pygame.transform.scale(self.image, (int(self.size[0]*0.6), int(self.size[1]*0.6)))

        # key coordinates, rectangle
        self.x = 300
        self.y = 515
        self.rect = self.actual.get_rect(topleft = (self.x, self.y))

        # other attributes
        self.off = False

    # changes the coordinates of a Button object
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y
        self.rect = self.actual.get_rect(topleft = (self.x, self.y))

    # function to see if the player collided with a button
    # if the player collides with a button, set button_off to true and 
    # gate_off to true
    def button_collide(self, player, gate):
        if self.rect.colliderect(player.rect):
            self.off = True
            gate.change_gate()
            return True
        return False