from asset import Asset

# Lava class
class Lava(Asset):
    def __init__(self, lava_image):
        super().__init__(lava_image, 380, 570, 0.4)
        self.burned = False
    
    # if the player collides with lava, their HP slowly depletes
    def lava_collide(self, player):
        if self.generic_collide(player):
            print("hot! hot!")
            player.hp -= 1
            if player.hp <= 0:
                player.die()
            self.burned = True
            return True
        return False