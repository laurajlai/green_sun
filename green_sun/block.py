from asset import Asset

# Block class
class Block(Asset):
    def __init__(self, block_image):
        super().__init__(block_image, 500, 460, 0.5)

    # function to see if the player collided with a block
    # if the player collided with a block, the game ends
    def block_collide(self, player):
        if self.generic_collide(player):
            player.die()
            print("Oops!")
            return True
        return False