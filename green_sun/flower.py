from asset import Asset

# Flower class
class Flower(Asset):
    def __init__(self, flower_image, align):
        super().__init__(flower_image, 446, 400, 1)
        self.taken = False
        self.move_size = 4
        self.max = 360
        self.min = 7
        self.moving_down = True
        self.align = align

        # the flower moves up and down (observing the ground, of course)
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

    # function to see if the player collided with a flower
    # if the player collides with a key, set the has_flower and can_double_jump attributes
    # to True
    def flower_collide(self, player):
        if self.generic_collide(player):
            player.has_flower = True
            self.taken = True
            if self.align == "vertical":
                player.can_high_jump = True
            else:
                player.can_wide_jump = True
            return True
        return False