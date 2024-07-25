import pygame

#initialize screen constants
WIDTH = 1395
HEIGHT = 677

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        #player image
        self.image = pygame.image.load('green_sun_player.png').convert_alpha()
        self.size = self.image.get_size()
        self.actual = pygame.transform.scale(self.image, (int(self.size[0]*0.25), int(self.size[1]*0.25)))

        #player coordinates, movement speed, jump modifiers, and rectangle
        self.x = 100
        self.y = 383
        self.rect = self.actual.get_rect(topleft = ((self.x, self.y)))
        self.is_in_jump = False
        self.jumpcount = 10
        self.move_size = 5
        self.can_double_jump = False

        #other attributes
        self.has_key = False
        self.has_flower = False
    
    # changes the coordinates of a Block object (needed because there are multiple blocks)
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y
        self.rect = self.actual.get_rect(topleft = (self.x, self.y))
    
    # key handler for the player character
    def handle_keys(self):
        key = pygame.key.get_pressed()
        # move left
        if key[pygame.K_LEFT] and self.x > self.move_size: 
            self.x -= self.move_size 
            self.rect = self.actual.get_rect(topleft = ((self.x, self.y)))

        # move right
        if key[pygame.K_RIGHT] and self.x < WIDTH - 0.25*self.size[0] - self.move_size: 
            self.x += self.move_size 
            self.rect = self.actual.get_rect(topleft = ((self.x, self.y)))

        """# if not currently in a jump, you can jump (this is to prevent double jumping)
        if not(self.is_in_jump): 
            if key[pygame.K_UP] and self.y > self.move_size: # up key
                #self.y -= self.move_size
                self.is_in_jump = True
            if key[pygame.K_DOWN] and self.y < HEIGHT - 155 - 0.25*self.size[1] - self.move_size: # down key
                self.y += self.move_size
                self.rect = self.actual.get_rect(topleft = ((self.x, self.y)))
        else:
            if self.jumpcount >= -10:
                is_negative = 1
                if self.jumpcount < 0:
                    is_negative = -1
                # this makes the jump larger, otherwise you're just jumping up in place
                self.y -= (self.jumpcount ** 2) * 0.5 * is_negative 
                self.x += 2*self.move_size
                self.rect = self.actual.get_rect(topleft = ((self.x, self.y)))

                self.jumpcount -= 1
            else: 
                self.jumpcount = 10
                self.is_in_jump = False   """
        if not self.is_in_jump:
            if key[pygame.K_UP] and self.y > self.move_size: # up key
                self.is_in_jump = True
                self.jump_count = 10
                if self.can_double_jump:
                    self.jump_height_multiplier = 1.5  # Increase jump height if player has double jump item
                else:
                    self.jump_height_multiplier = 1.0

            if key[pygame.K_DOWN] and self.y < HEIGHT - 155 - 0.25 * self.size[1] - self.move_size: # down key
                self.y += self.move_size
                self.rect = self.actual.get_rect(topleft=(self.x, self.y))

        else:
            if self.jump_count >= -10:
                is_negative = 1
                if self.jump_count < 0:
                    is_negative = -1

                # this makes the jump larger, otherwise you're just jumping in place
                # add jump_height_multiplier if necessary
                self.y -= (self.jump_count ** 2) * 0.5 * is_negative * self.jump_height_multiplier
                self.x += 2 * self.move_size
                self.rect = self.actual.get_rect(topleft=(self.x, self.y))
                self.can_double_jump = False

                self.jump_count -= 1
            else:
                self.is_in_jump = False
                self.jump_count = 10

