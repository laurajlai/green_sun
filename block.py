import pygame

# Block class
class Block(pygame.sprite.Sprite):
    def __init__(self, block_image):
        pygame.sprite.Sprite.__init__(self)

        # block image
        self.image = pygame.image.load(block_image).convert_alpha()
        self.size = self.image.get_size()
        self.actual = pygame.transform.scale(self.image, (int(self.size[0]*0.5), int(self.size[1]*0.5)))

        # block coordinates (for block1), rectangle
        self.x = 500
        self.y = 460
        self.rect = self.actual.get_rect(topleft = (self.x, self.y))
    
    # changes the coordinates of a Block object (needed because there are multiple blocks)
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y
        self.rect = self.actual.get_rect(topleft = (self.x, self.y))

    # function to see if the player collided with a block
    # if the player collided with a block, the game ends
    def block_collide(self, player):
        if self.rect.colliderect(player.rect):
            print("Skill issue")
            return True
        return False