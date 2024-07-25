import pygame

# Door class
class Door(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # door image
        self.image = pygame.image.load('green_sun_door.png').convert_alpha()
        self.size = self.image.get_size()
        self.actual = pygame.transform.scale(self.image, (int(self.size[0]*0.5), int(self.size[1]*0.5)))

        # door coordinates, rectangle
        self.x = 1200
        self.y = 347
        self.rect = self.actual.get_rect(topleft = (self.x, self.y))

    # changes the coordinates of a Door
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y
        self.rect = self.actual.get_rect(topleft = (self.x, self.y))

    # function to see if the player collided with the door
    # if the player has a key, the player can access the door
    def door_collide(self, player, gate = None):
        to_ret = False
        # if a gate is not in the level, just need to check if player has hit the door with the key
        if gate is None:
            if (self.rect.colliderect(player.rect) and player.has_key):
                print("You win!")
                to_ret = True
        
        # if a gate is in the level, need to check that the player has hit the button too
        else:
            if (self.rect.colliderect(player.rect) and player.has_key and gate.off == True):
                print("You win!")
                to_ret = True
            if (self.rect.colliderect(player.rect) and player.has_key and gate.off == False):
                print("You do not win yet.")

        return to_ret