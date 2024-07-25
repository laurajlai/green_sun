import pygame
import subprocess
import sys

# Portal class
class Portal(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # portal image 
        self.image = pygame.image.load('green_sun_portal.png').convert_alpha()
        self.size = self.image.get_size()
        self.actual = pygame.transform.scale(self.image, (int(self.size[0]*0.6), int(self.size[1]*0.6)))

        # portal activation
        self.activated = False

        # portal coordinates, rectangle
        self.x = 1200
        self.y = 300
        self.rect = self.actual.get_rect(topleft = (self.x, self.y))
    
    # changes the coordinates of a Portal object
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y
        self.rect = self.actual.get_rect(topleft = (self.x, self.y))
    
    # function to see if the player collided with a portal
    # if the player collides with a portal, the portal is activated and the program
    # redirects to the new_screen parameter
    def portal_collide(self, player, new_screen):
        if self.rect.colliderect(player.rect):
            self.activated = True
            subprocess.Popen(["python3", new_screen])
            pygame.quit()
            sys.exit()
            return True
        return False