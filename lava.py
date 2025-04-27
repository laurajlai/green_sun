from asset import Asset

# Lava class
class Lava(Asset):
    def __init__(self, lava_image):
        super().__init__(lava_image, 211, 490, 0.56)
        self.burned = False
    
    # if the player collides with lava without a fireproof sigil, they die
    # otherwise, they can pass through and the sigil is removed.
    def lava_collide(self, player):
        if self.generic_collide(player) and player.has_sigil is True:
            pass
        elif self.generic_collide(player) and player.has_sigil is False:
            print("hot! hot!")
            self.burned = True
            return True
        return False