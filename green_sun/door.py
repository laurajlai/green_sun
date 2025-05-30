from asset import Asset

# Door class
class Door(Asset):
    def __init__(self, door_image):
        super().__init__(door_image, 1200, 347, 0.5)

    # function to see if the player collided with the door
    # if the player has a key, the player can access the door
    def door_collide(self, player, gate = None):
        to_ret = False
        # if a gate is not in the level, just need to check if player has hit the door with the key
        if gate is None:
            if self.generic_collide(player) and player.has_key:
                print("You win!")
                to_ret = True
        
        # if a gate is in the level, need to check that the player has hit the button too
        else:
            if self.generic_collide(player) and player.has_key and gate.off == True:
                print("You win!")
                to_ret = True
            if self.generic_collide(player) and player.has_key and gate.off == False:
                print("You do not win yet.")

        return to_ret