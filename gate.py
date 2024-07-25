import pygame

class Gate(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # gate image
        self.image = pygame.image.load('green_sun_gate.png').convert_alpha()
        self.size = self.image.get_size()
        self.actual = pygame.transform.scale(self.image, (int(self.size[0]*0.6), int(self.size[1]*0.6)))

        # key coordinates, rectangle
        self.x = 500
        self.y = 108
        self.rect = self.actual.get_rect(topleft = (self.x, self.y))

        # other attributes
        self.off = False

    # changes the coordinates of a Gate object
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y
        self.rect = self.actual.get_rect(topleft = (self.x, self.y))
    
    # function to change the gate from active to inactive/permeable
    def change_gate(self):
        # replace the gate image
        self.image = pygame.image.load('green_sun_gate_open.png').convert_alpha()
        self.actual = pygame.transform.scale(self.image, (int(self.size[0]*0.6), int(self.size[1]*0.6)))
        self.off = True

    # function to see if the player collided with the gate
    # if the player collides with the gate while the gate is not off, they
    # cannot move 
    # otherwise, the gate changes color
    def gate_collide(self, player, button):
        to_ret = False
        printed = False
        if self.rect.colliderect(player.rect):
            if (button.off == False):
                player.x = 181
                if (printed == False):
                    print("Oh no!! You ignored the instruction! Try activating the button first")
                    printed = True
                return True
            else:
                self.change_gate()
                to_ret = True
        return to_ret