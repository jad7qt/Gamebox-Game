#Jared Dutt, jad7qt

import gamebox
import pygame
import random

frameCounter = 0
width = 600
height = 400
camera_speed = 1.75
camera = gamebox.Camera(width, height)
died = False
score = 0

# Platform Values
plat_height = 20

# Creating Player
player_dimension = 15
player = gamebox.from_color(width/2, 100, 'green', player_dimension, player_dimension)

platforms = [gamebox.from_color(width+20, 300, 'white', width, plat_height),
        gamebox.from_color(-20, 300, 'white', width, plat_height),
        gamebox.from_color(width+20, 390, 'white', width, plat_height),
        gamebox.from_color(-20, 390, 'white', width, plat_height)
             ]

def updatePlayer(keys):
    '''Takes in keys pressed by user as parameter and moves the character left or right if left or right arrow keys pressed'''
    if pygame.K_LEFT in keys:
        player.x -= 5
    if pygame.K_RIGHT in keys:
        player.x += 5

def generatePlat():
    '''Generates platforms with holes centered at random places within the screen width. Generates 2 gameboxes for each level.
    Also deletes platforms that are out of the camera view above the character'''
    global frameCounter
    global width
    if frameCounter% 55== 1:
        holeCenter = random.random() * width  # fix to make sure hole isn't too far over
        leftPlatCenter = holeCenter - (width + 10)
        rightPlatCenter = holeCenter + (width + 10)
        new_left = gamebox.from_color(leftPlatCenter, camera.y+300, 'white', width*2-20, plat_height)
        new_right = gamebox.from_color(rightPlatCenter, camera.y+300, 'white', width*2-20, plat_height)
        platforms.append(new_left)
        platforms.append(new_right)
    for plat in platforms:  # Deletes platforms above camera view
        if plat.y < camera.y-(height):
            platforms.remove(plat)


def tick(keys):
    '''Takes all keys pressed as parameter, and runs every second as many times as ticks_per_second is set to.
    Contains main game components. Freezes everything if died is set to True, but can be restarted when r is pressed'''
    global frameCounter
    global height
    global died
    global platforms
    global camera
    global player
    global score

    if not died:
        # clear background
        camera.clear("black")

        # gravity
        player.speedy += 1
        player.y += player.speedy

        # move camera down
        camera.y += camera_speed

        # jump statement
        for platformAny in platforms:
            camera.draw(platformAny)  # drawing walls
            if player.bottom_touches(platformAny) and pygame.K_SPACE in keys:
                player.speedy = -15  # jumps up
            if player.touches(platformAny):  # Moves to stop overlapping platforms
                player.move_to_stop_overlapping(platformAny)

        # Moves character if hitting bottom of camera
        if player.y+(player_dimension/2) >= camera.y + (height/2):
            player.y = camera.y + (height/2)-(player_dimension/2)

        # Moves character if hitting either side of camera
        if player.x+(player_dimension/2) >= camera.x + (width/2):  # Right side
            player.x = camera.x + (width/2) -(player_dimension/2)
        if player.x-(player_dimension/2) <= camera.x - (width/2):  # Left side
            player.x = camera.x - (width/2) + (player_dimension/2)

        # Game over condition
        if player.y < camera.y-(height/2):
            camera.draw(gamebox.from_text(camera.x, camera.y - 30, "DEAD", 70, "red"))
            camera.draw(gamebox.from_text(camera.x, camera.y + 20, "Press r to restart", 30, "red"))
            camera.display()
            died = True


        # update player
        updatePlayer(keys)

        # increments frame Counter, keeps score
        frameCounter += 1
        if frameCounter%ticks_per_second == 0:
            score += 1

        # Creating platforms
        generatePlat()

        # drawing gameboxes
        camera.draw(player)
        camera.draw(gamebox.from_text(camera.x+(width/2)-30, camera.y - (height/2)+30, str(score), 30, "red"))
        camera.display()


    else:
        if pygame.K_r in keys:
            died = False
            frameCounter = 0
            score = 0
            camera.x = width/2
            camera.y = height/2
            player = gamebox.from_color(width / 2, 100, 'green', 15, 15)
            player.speedy = 0
            platforms = [gamebox.from_color(width + 20, 300, 'white', width, plat_height),
                         gamebox.from_color(-20, 300, 'white', width, plat_height),
                         gamebox.from_color(width + 20, 390, 'white', width, plat_height),
                         gamebox.from_color(-20, 390, 'white', width, plat_height)
                         ]

ticks_per_second = 40
gamebox.timer_loop(ticks_per_second, tick)
