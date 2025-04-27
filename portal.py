from asset import Asset
import subprocess
import sys

# Portal class
class Portal(Asset):
    def __init__(self, portal_image):
        super().__init__(portal_image, 1200, 300, 0.6)
        self.activated = False
    
    # function to see if the player collided with a portal
    # if the player collides with a portal, the portal is activated and the program
    # redirects to the new_screen parameter
    def portal_collide(self, player, new_screen):
        if self.generic_collide(player):
            self.activated = True
            subprocess.Popen(["python3", new_screen])
            sys.exit()
        return False