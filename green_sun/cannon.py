from asset import Asset

# Cannon class
class Cannon(Asset):
    def __init__(self, cannon_image):
        super().__init__(cannon_image, 380, 480, 0.17)
        self.move_size = 2.5
        self.moving_left = True
    
    # moves left and right.
    def move(self, min, max):
        # Move left
        if self.moving_left:
            self.x += self.move_size
            if self.x >= max:  # If it reaches max, reverse direction
                self.x = max
                self.moving_left = False  
        
        # Move right
        else:
            self.x -= self.move_size
            if self.x <= min:  # If it reaches min, reverse direction
                self.x = min
                self.moving_left = True  

        # Update rect after movement
        self.rect = self.actual.get_rect(topleft=(self.x, self.y))
    
    # colliding with a cannon kills you 
    def cannon_collide(self, player):
        if self.generic_collide(player):
            player.die()
            print("Oops!")
            return True
        return False