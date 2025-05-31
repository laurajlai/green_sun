# level 5, part 2

# import assets
from level_setup import *
import player
import block as block
import key
import button
from cannon import Cannon
import gate
import door

screen, clock = setup_pygame()

#set background to the Green Sun level 5 background
background = setup_background('level_backdrops/green_sun_l5_p2.png')

# declare instances of objects
player = player.Player()
player.set_coordinates(player.x-80, player.y + 60)
key1 = key.Key('images/green_sun_key.png')
key1.set_coordinates(key1.x +350, key1.y)
cannon = Cannon('images/green_sun_cannon.png')
cannon1 = Cannon('images/green_sun_cannon.png')
cannon1.set_coordinates(cannon.x+200, cannon.y)
door = door.Door('images/green_sun_door.png')
door.set_coordinates(door.x, door.y+60)
button = button.Button('images/green_sun_button.png')
button.set_coordinates(button.x+500, button.y+50)
gate = gate.Gate('images/green_sun_gate.png')
gate.set_coordinates(gate.x+430, gate.y+50)

# create variable to keep the game running
running = 1

# create a variable to keep track of whether or not victory message 
# has printed
has_printed = False

while running:
    # check game events
    for event in pygame.event.get():
        # check to see if the user decided to quit the game or restart
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = 0
            elif event.key == pygame.K_r:
                main()
        elif event.type == QUIT:
            running = 0
    
    cannon.move(100, 370)
    cannon1.move(400, 700)

    # colliding with a cannon is fatal
    if(cannon.cannon_collide(player) or cannon1.cannon_collide(player)):
        running = 0
        death_logic(screen, clock, player, 'level5_p2.py')

    # if the player runs into a gate while the button is not on, you
    # cannot move
    if(gate.gate_collide(player, button)):
        if(button.off):
            pass
    
    # if the player runs into a button, well, uh, it keeps going
    if(button.button_collide(player, gate)):
        pass

    # if the player runs into a key, well, uh, it keeps going    
    if(key1.key_collide(player)):
        pass

    # if the player gets to the door and has the key, they win
    if(door.door_collide(player)):
        if(player.has_key):
            if(has_printed is False):
                print("You win! thank you for playing green sun!")
                has_printed = True
            running = 0

    # arrow key and space controls
    player.handle_keys()

    # draw objects
    screen.blit(background,(0,0))
    screen.blit(player.actual, (player.x, player.y))

    # only blit the button and gate if the player has stepped on it
    if (not button.off):
        screen.blit(button.actual, (button.x, button.y))
    
    screen.blit(gate.actual, (gate.x, gate.y))
    screen.blit(cannon.actual, (cannon.x, cannon.y))
    screen.blit(cannon1.actual, (cannon1.x, cannon1.y))

    # only blit the key if the player does not have it
    if(not player.has_key):
        screen.blit(key1.actual, (key1.x, key1.y))
    screen.blit(door.actual, (door.x, door.y))
    pygame.display.flip()