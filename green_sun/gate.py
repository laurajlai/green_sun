from asset import Asset
import pygame

class Gate(Asset):
    def __init__(self, gate_image):
        super().__init__(gate_image, 500, 108, 0.6)
        self.off = False
    
    # function to change the gate from active to inactive/permeable
    def change_gate(self):
        # replace the gate image
        self.image = pygame.image.load('images/green_sun_gate_open.png').convert_alpha()
        self.actual = pygame.transform.scale(self.image, (int(self.size[0]*0.6), int(self.size[1]*0.6)))
        self.off = True

    # function to see if the player collided with the gate
    # if the player collides with the gate while the gate is not off, they
    # are sent back to the beginning
    # otherwise, the gate changes color
    def gate_collide(self, player, button):
        to_ret = False
        printed = False
        if self.generic_collide(player):
            if (button.off == False):
                while player.x > 0:
                    player.x -=10
                if (printed == False):
                    print("Oh no!! You ignored the instruction! Try activating the button first")
                    printed = True
                return True
            else:
                self.change_gate()
                to_ret = True
        return to_ret