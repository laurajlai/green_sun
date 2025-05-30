from asset import Asset

# Grow/Shrink Class
class GrowShrink(Asset):
    def __init__(self, starting_image, mode):
        super().__init__(starting_image, 1200, 300, 0.6)
        self.mode = mode
        self.used = False
    
    # function to see if the player collided with a grow/shrink module
    # if in "grow" mode, the player grows. if in shrink mode, the player shrinks.
    def growshrink_collide(self, player):
        if self.generic_collide(player):
            if self.mode == "grow":
                player.grow()
                self.used = True
            else:
                player.shrink()
                self.used = True
            return True
        return False