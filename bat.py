from asset import Asset

# Bat class
class Bat(Asset):
    def __init__(self, bat_image, move_size):
        super().__init__(bat_image, 400, 300, 0.4)
        self.move_size = move_size
        self.max = 500
        self.min = 0
        self.moving_down = True
    
    # the bat moves up and down (observing the ground, of course)
    def move(self):
        # Move downward
        if self.moving_down:
            self.y += self.move_size
            if self.y >= self.max:  # If it reaches max, reverse direction
                self.y = self.max
                self.moving_down = False  
        
        # Move upward
        else:
            self.y -= self.move_size
            if self.y <= self.min:  # If it reaches min, reverse direction
                self.y = self.min
                self.moving_down = True  

        # Update rect after movement
        self.rect = self.actual.get_rect(topleft=(self.x, self.y))

    
    # if the player collides with a bat in normal size, the game ends
    # however, if the player collides with a bat in grown size, the bat just chips
    # their HP
    def bat_collide(self, player):
        if self.generic_collide(player) and player.has_grown is True:
            pass
        elif self.generic_collide(player) and player.has_grown is False:
            print("Skill issue")
            return True
        return False