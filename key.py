from asset import Asset

# Key class
class Key(Asset):
    def __init__(self, key_image):
        super().__init__(key_image, 650, 420, 0.6)
    
    # function to see if the player collided with a key
    # if the player collides with a key, set the has_key attribute to True
    def key_collide(self, player):
        if self.generic_collide(player):
            player.has_key = True
            return True
        return False
