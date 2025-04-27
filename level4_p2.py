# level 4, part 2

#import pygame
import pygame

#import pygame.locals for keyboard controls
from pygame.locals import*

#import assets
import player
import bat
import door
import growshrink
import key

#initialize screen constants
WIDTH = 1395
HEIGHT = 677

pygame.init()

#create screen object
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#set background to the first Green Sun level 4 background
background = pygame.image.load('level_backdrops/green_sun_l4_p2.png')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

#declare instances of objects used in part 1
player = player.Player()
player.set_coordinates(player.x, player.y + 50)
grow_shrink = growshrink.GrowShrink('images/green_sun_grow.png', "grow")
grow_shrink.set_coordinates(grow_shrink.x - 1000, grow_shrink.y + 200)
bat1 = bat.Bat('images/green_sun_bat.png', 3)
bat2 = bat.Bat('images/green_sun_bat.png', 4)
bat3 = bat.Bat('images/green_sun_bat.png', 3)
bat2.set_coordinates(bat1.x + 210, bat1.y)
bat3.set_coordinates(bat1.x + 440, bat1.y)
door = door.Door('images/green_sun_door.png')
door.set_coordinates(door.x, door.y + 55)
key = key.Key('images/green_sun_key.png')
key.set_coordinates(key.x + 375, key.y)

#create variable to keep the game running
running = 1

# create a variable to keep track of whether or not victory message 
# has printed
has_printed = False

# game loop for part 1 of the game
while running == 1:
    #check game events
    for event in pygame.event.get():
        #check to see if the user decided to quit the game
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = 0
        elif event.type == QUIT:
            running = 0

    # if the player runs into a block, the game ends
    if(bat1.bat_collide(player) or bat2.bat_collide(player) or bat3.bat_collide(player)):
        running = 0

    # if the player runs into the shrink button, they shrink
    if(grow_shrink.growshrink_collide(player)):
        pass    

    # if the player runs into a key, well, uh, it keeps going    
    if(key.key_collide(player)):
        pass
    
    # if the player gets to the door and has the key, they win
    if(door.door_collide(player)):
        if(player.has_key):
            if(has_printed):
                print("You win!")
                has_printed = True
            running = 0
    
    # arrow key and space controls
    player.handle_keys()
    bat1.move()
    bat2.move()
    bat3.move()

    screen.blit(background,(0,0))
    screen.blit(player.actual, (player.x, player.y))
    screen.blit(bat1.actual, (bat1.x, bat1.y))
    screen.blit(bat2.actual, (bat2.x, bat2.y))
    screen.blit(bat3.actual, (bat3.x, bat3.y))
    screen.blit(door.actual, (door.x, door.y))

    # only blit the shrink module if the player has not used it
    if (not grow_shrink.used):
        screen.blit(grow_shrink.actual, (grow_shrink.x, grow_shrink.y))

    # only blit the key and flower if the player does not have it
    if(not player.has_key):
        screen.blit(key.actual, (key.x, key.y))

    pygame.display.flip()

