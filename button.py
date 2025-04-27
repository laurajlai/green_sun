from asset import Asset

class Button(Asset):
    def __init__(self, button_image):
        super().__init__(button_image, 300, 515, 0.6)
        self.off = False

    # function to see if the player collided with a button
    # if the player collides with a button, set button_off to true and 
    # gate_off to true
    def button_collide(self, player, gate):
        if self.generic_collide(player):
            self.off = True
            gate.change_gate()
            return True
        return False