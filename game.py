# Jared Dutt, jad7qt

# Planning to make a game with different a room progression system
# The character has to get a key / reach the door / beat a boss to go to the next room
# Game will allow restart with button
# Character will have health bar
# rooms will be set in advance, not random.

import gamebox
import pygame
import random

frameCounter = 0
jumpingFrame = 104
width = 800
height = 600
camera = gamebox.Camera(width, height)
died = False
health = 100
player_right = True
notJumping = True
jumpHeight = -15
player_inventory = []
current_level = 1
milsecs = 0
endSkelWalk = 120
skelWalkRight = True
time_walk = 200
facingRight = True
attacking = False

# Floor gamebox
plat_width = 70
plat_thick = 15
plat_height = 60
plat_distance = 150
plat_color = 'black'
floors = [gamebox.from_color(camera.x, height, plat_color, width, 20),  # First floor
          gamebox.from_color(camera.x + width, height, plat_color, width, 20),  # Second floor
          gamebox.from_color(camera.x + (2 * width), height, plat_color, width, 20),  # Third floor
          gamebox.from_color(4 * width - (width/4) + 150, height, plat_color, (width/2) - 100, 20),  # Fourth floor part 2
          gamebox.from_color(3 * width + (width/4) - 150, height, plat_color, (width/2) - 60, 20),  # Fourth floor part 1
          gamebox.from_color(5 * width - 25, height, plat_color, 50, 20),  # Fifth Floor
          gamebox.from_color(5.5 * width, height, "gold", width, 20),  # Sixth Floor
          gamebox.from_color(6.5 * width, height, "gold", width, 20),  # Sixth Floor
          gamebox.from_color(camera.x - plat_distance, height - plat_height, plat_color, plat_width, plat_thick),  # Stage 1
          gamebox.from_color(camera.x, height - 2 * plat_height, plat_color, plat_width, plat_thick),  # Stage 1
          gamebox.from_color(camera.x + plat_distance, height - 3 * plat_height, plat_color, plat_width, plat_thick),  # Stage 1
          gamebox.from_color(camera.x, height - 4 * plat_height, plat_color, plat_width, plat_thick),  # Stage 1
          gamebox.from_color(camera.x - plat_distance, height - 5 * plat_height, plat_color, plat_width, plat_thick),  # Stage 1
          gamebox.from_color(camera.x, height - 6 * plat_height, plat_color, plat_width, plat_thick),  # Stage 1
          gamebox.from_color(camera.x + plat_distance, height - 7 * plat_height, plat_color, plat_width, plat_thick),  # Stage 1
          gamebox.from_color(width + 100, height - (plat_width / 2), plat_color, plat_thick, plat_width),  # Stage 2 first wall
          gamebox.from_color(2 * width - 100, height - (plat_width / 2), plat_color, plat_thick, plat_width),  # Stage 2 second wall
          gamebox.from_color(3 * width - 75, height - 30, plat_color, plat_thick, 40),  # Stage 3 second wall
          gamebox.from_color(2.5 * width - plat_distance, height - plat_height, plat_color, plat_width/2, plat_thick),  # Stage 3 plat
          gamebox.from_color(2.5 * width, height - 2 * plat_height, plat_color, plat_width / 2, plat_thick),  # Stage 3 plat
          gamebox.from_color(2.5 * width + plat_distance, height - 3 * plat_height, plat_color, plat_width / 2, plat_thick),  # Stage 3 plat
          gamebox.from_color(2.5 * width + 2 * plat_distance, height - 4 * plat_height, plat_color, plat_width / 2, plat_thick),  # Stage 3 plat
          gamebox.from_color(2.5 * width + plat_distance, height - 5 * plat_height, plat_color, plat_width / 2, plat_thick),  # Stage 3 plat
          gamebox.from_color(2.5 * width, height - 6 * plat_height, plat_color, plat_width / 2, plat_thick),  # Stage 3 plat
          gamebox.from_color(2.5 * width - plat_distance, height - 7 * plat_height, plat_color, plat_width / 2, plat_thick),  # Stage 3 plat
          gamebox.from_color(2 * width + (plat_width / 2), height - 8 * plat_height, plat_color, plat_width, plat_thick),  # Stage 3 final plat
          gamebox.from_color(3.5 * width + 40, height - plat_height * 1.5, plat_color, plat_width * 3, plat_thick),  # Stage 4 skeleton plat
          gamebox.from_color(3.5 * width + 40 + (plat_width * 3)/2 - (plat_thick/2), height - plat_height * 1.5 - 5, plat_color, plat_thick, 20),  # Stage 4 skeleton plat wall 1
          gamebox.from_color(3.5 * width + 40 - (plat_width * 3)/2 + (plat_thick/2), height - plat_height * 1.5 - 5 , plat_color, plat_thick, 20),  # Stage 4 skeleton plat wall 2
          gamebox.from_color(3.5 * width + plat_distance, height - 3 * plat_height, plat_color, plat_width, plat_thick),  # Stage 4
          gamebox.from_color(3.5 * width, height - 4.5 * plat_height, plat_color, plat_width, plat_thick),  # Stage 4
          gamebox.from_color(3.5 * width - plat_distance, height - 6 * plat_height, plat_color, plat_width, plat_thick),  # Stage 4
          gamebox.from_color(3.5 * width, height - 7.5 * plat_height, plat_color, plat_width, plat_thick),  # Stage 4
          gamebox.from_color(3.5 * width + plat_distance * 1.5, height - 7.5 * plat_height, plat_color, plat_width, plat_thick),  # Stage 4
          gamebox.from_color(3.5 * width + plat_distance * 2 - 10, height - 7.5 * plat_height, plat_color, plat_width, plat_thick),  # Stage 4
          gamebox.from_color(4 * width + plat_distance, height - 1.5* plat_height, plat_color, plat_width/2,plat_thick),  # Stage 5
          gamebox.from_color(4 * width + plat_distance * 2, height - 2.5 * plat_height, plat_color, plat_width/2,plat_thick),  # Stage 5
          gamebox.from_color(4 * width + plat_distance, height - 3.5 * plat_height, plat_color, plat_width/2,plat_thick),  # Stage 5
          gamebox.from_color(4 * width + plat_distance * 2, height - 4.5 * plat_height, plat_color, plat_width/2,plat_thick),  # Stage 5
          gamebox.from_color(4 * width + plat_distance * 3, height - 5.5 * plat_height, plat_color, plat_width/2,plat_thick),  # Stage 5
          gamebox.from_color(4 * width + plat_distance * 4, height - 4.5 * plat_height, plat_color, plat_width/2, plat_thick),  # Stage 5
          gamebox.from_color(4 * width + plat_distance * 2, height - 6.5 * plat_height, plat_color, plat_width / 2, plat_thick),  # Stage 5
          gamebox.from_color(4 * width + plat_distance, height - 7.5 * plat_height, plat_color, plat_width / 2, plat_thick)  # Stage 5
          ]

# Spawn Plate gameboxes
spawnPlates = [
    gamebox.from_color(20, height - 15, 'light grey', 30, 10),  # Plate 1
    gamebox.from_color(width + 20, height - 15, 'light grey', 30, 10),  # Plate 2
    gamebox.from_color(2 * width + 20, height - 15, 'light grey', 30, 10),  # Plate 3
    gamebox.from_color(3 * width + 20, height - 15, 'light grey', 30, 10),  # Plate 4
    gamebox.from_color(4 * width + 20, height - 15, 'light grey', 30, 10),  # Plate 5
    gamebox.from_color(5 * width + 20, height - 15, 'light grey', 30, 10),  # Plate 6
    gamebox.from_color(6 * width + 20, height - 15, 'light grey', 30, 10)  # Final Plate
]
# Next Level plate gameboxes
nextLevelPlates = [
    gamebox.from_color(width - 20, height - 15, 'pink', 30, 10),  # Plate 1
    gamebox.from_color(2 * width - 20, height - 15, 'pink', 30, 10),  # Plate 2
    gamebox.from_color(3 * width - 20, height - 15, 'pink', 30, 10),  # Plate 3
    gamebox.from_color(4 * width - 20, height - 15, 'pink', 30, 10),  # Plate 4
    gamebox.from_color(5 * width - 20, height - 15, 'pink', 30, 10),  # Plate 5
    gamebox.from_color(6 * width - 30, height - 15, 'pink', 30, 10)  # Plate 6
]

# Self created door image
doors = [
    gamebox.from_image(width - 26, height - 40, "pixel_art.png"),  # First Door
    gamebox.from_image(2 * width - 26, height - 40, "pixel_art.png"),  # Second Door
    gamebox.from_image(3 * width - 26, height - 40, "pixel_art.png"),  # Third Door
    gamebox.from_image(4 * width - 26, height - 40, "pixel_art.png"),  # Fourth Door
    gamebox.from_image(5 * width - 26, height - 40, "pixel_art.png"),  # Fifth Door
    gamebox.from_image(6 * width - 50, height - 75, "pixel_art.png")  # Sixth Door
]
# Scale the doors to correct size
for door in doors:
    door.scale_by(0.25)
doors[5].scale_by(2)

# Key image from Dinopixel.com by mnjackson5
key_image = gamebox.load_sprite_sheet("https://dinopixel.com/preload/0520/pixel-key.png", 1, 1)
key1 = gamebox.from_image(camera.x + plat_distance, height - (7 * plat_height) - 20, key_image[0])
key1.scale_by(0.05)
key2 = gamebox.from_image(camera.x + width, height - 20, key_image[0])
key2.scale_by(0.05)
key3 = gamebox.from_image(2 * width + (plat_width/2), height - 8 * plat_height - 23, key_image[0])
key3.scale_by(0.05)
key4 = gamebox.from_image(3.5 * width + (plat_distance * 2), height - 7.5 * plat_height - 23, key_image[0])
key4.scale_by(0.05)
key5 = gamebox.from_image(4 * width + plat_distance, height - 7.5 * plat_height - 23, key_image[0])
key5.scale_by(0.05)
key6 = gamebox.from_image(5.5 * width, height - 80, key_image[0])
key6.scale_by(0.2)


# Sprite pictures from www.seanmacdonnell.com
player_images = gamebox.load_sprite_sheet('https://seanmacdonnell.com/wp-content/uploads/2014/11/New-Running.png', 14,
                                          13)
player = gamebox.from_image(spawnPlates[0].x, spawnPlates[0].y, player_images[142])
player.scale_by(2)
current_frame = 142

# Skeleton sprite pictures from www.opengameart.org
skel_images = gamebox.load_sprite_sheet('https://opengameart.org/sites/default/files/skeleton_3.png', 21, 13)
skel = gamebox.from_image(width + (width / 2), (height / 2), skel_images[26])
skel_frame = 143

def updateSkels():
    global skel_frame, skel, floors, player, player_inventory, endSkelWalk, skelWalkRight, time_walk, facingRight, attacking
    for floor in floors:  # Move skeleton to not pass through floor
        if skel.touches(floor):
            skel.move_to_stop_overlapping(floor)
    if (milsecs - endSkelWalk) < time_walk:
        if skelWalkRight and not skel.touches(player):
            skel.x += 2
        elif not skel.touches(player):
            skel.x -= 2
    else:
        endSkelWalk = milsecs
        skelWalkRight = not skelWalkRight
        time_walk = random.randint(1*ticks_per_second,5*ticks_per_second)
    if skel.touches(player):
        endSkelWalk += 1
        if not attacking:
            skel.flip()
        if not attacking:  # runs if the skeleton has first touched the player
            skel_frame = 221
            attacking = True
        skel.image = skel_images[int(skel_frame)]
        skel_frame += 0.6
        if skel_frame > 232:
            skel_frame = 221
    elif skelWalkRight:  # For walking RIGHT, changes skel sprite
        if attacking:
            skel.flip()
        attacking = False
        if not facingRight:
            skel.flip()
            facingRight = True
        skel_frame += 0.35
        if skel_frame > 151:
            skel_frame = 143
        skel.image = skel_images[int(skel_frame)]
    else:  # For walking LEFT, changes skel sprite
        if attacking:
            skel.flip()
        attacking = False
        if facingRight:
            skel.flip()
            facingRight = False
        skel_frame += 0.35
        if skel_frame > 151:
            skel_frame = 143
        skel.image = skel_images[int(skel_frame)]

def updatePlayer(keys):
    global current_frame, player_right, floors, notJumping, jumpingFrame, player_inventory
    player_run = False
    '''Takes in keys pressed by user as parameter and moves the character left or right if left or right arrow keys 
    pressed. Also cycles sprite image '''
    if pygame.K_LEFT in keys:
        if player_right:
            player.flip()
            player_right = False
        player.x -= 5
        player_run = True
    if pygame.K_RIGHT in keys:
        if not player_right:
            player.flip()
            player_right = True
        player.x += 5
        player_run = True

    # Loops through sprite sheet for running animation or jumping
    if player_run and notJumping:  # Running Animation
        current_frame += 0.2
        if current_frame > 9:
            current_frame = 0
        player.image = player_images[int(current_frame)]
    elif not notJumping:  # Jumping animation
        player.image = player_images[int(jumpingFrame)]
        jumpingFrame += 0.3
        if 107 < jumpingFrame < 108.3:  # If Jumping frame is passed first row of animation
            jumpingFrame = 117
        if 120 < jumpingFrame < 122.3:  # If Jumping frame is passed second row of animation
            jumpingFrame = 143
        if jumpingFrame > 145.3:  # If Jumping frame is passed third row of animation
            jumpingFrame = 104
    else:
        player.image = player_images[142]
        jumpingFrame = 104


def update_keys():
    global player, key1
    if player.touches(key1):
        player_inventory.append(key1)
    if key1 not in player_inventory:
        camera.draw(key1)
    if player.touches(key2):
        player_inventory.append(key2)
    if key2 not in player_inventory:
        camera.draw(key2)
    if player.touches(key3):
        player_inventory.append(key3)
    if key3 not in player_inventory:
        camera.draw(key3)
    if player.touches(key4):
        player_inventory.append(key4)
    if key4 not in player_inventory:
        camera.draw(key4)
    if player.touches(key5):
        player_inventory.append(key5)
    if key5 not in player_inventory:
        camera.draw(key5)
    if player.touches(key6):
        player_inventory.append(key6)
    if key6 not in player_inventory:
        camera.draw(key6)


def new_level_check():
    global current_level, player, player_inventory, nextLevelPlates
    if current_level == 1 and player.touches(nextLevelPlates[0]) and key1 in player_inventory:
        player.x = spawnPlates[1].x
        player.y = spawnPlates[1].y
        camera.x += width
        current_level = 2
    if current_level == 2 and player.touches(nextLevelPlates[1]) and key2 in player_inventory:
        player.x = spawnPlates[2].x
        player.y = spawnPlates[2].y
        camera.x += width
        current_level = 3
        skel.x = 2.6 * width
    if current_level == 3 and player.touches(nextLevelPlates[2]) and key3 in player_inventory:
        player.x = spawnPlates[3].x
        player.x = spawnPlates[3].y
        camera.x += width
        current_level = 4
        skel.x = 3.5 * width
        skel.y = height - plat_height * 1.5 - 30
        skel.scale_by(0.5)
    if current_level == 4 and player.touches(nextLevelPlates[3]) and key4 in player_inventory:
        player.x = spawnPlates[4].x
        player.x = spawnPlates[4].y
        camera.x += width
        current_level = 5
        skel.x = 1.5 * width
        skel.scale_by(2)
    if current_level == 5 and player.touches(nextLevelPlates[4]) and key5 in player_inventory:
        player.x = spawnPlates[5].x
        player.x = spawnPlates[5].y
        camera.x += width
        current_level = 6
    if current_level == 6 and player.touches(nextLevelPlates[5]) and key6 in player_inventory:
        player.x = spawnPlates[6].x
        player.x = spawnPlates[6].y
        camera.x += width
        current_level = 7


def update_health():
    global health, died
    if player.touches(skel):  # if player touches anything that hurts him, remove health at some increment
        health -= 1
    camera.draw(gamebox.from_text(camera.x - (width/2) + 33, 45, "Health", 20, 'red'))
    camera.draw(gamebox.from_color( (camera.x - (width/2)+63 - (0.5 * (100 - health))), 65, 'red', health, 20))

    if player.y > (height + 100):
        health = 0

    if health == 0:
        camera.draw(gamebox.from_text(camera.x, camera.y - 30, "DEAD", 70, "red"))
        camera.draw(gamebox.from_text(camera.x, camera.y + 20, "Press r to restart", 30, "red"))
        camera.display()
        died = True


def tick(keys):
    global frameCounter, height, died, camera, health, notJumping, spawnPlates, milsecs, player_inventory,\
        current_level, facingRight, skelWalkRight, skel_frame, endSkelWalk, time_walk
    if not died:
        milsecs +=1

        # clear background
        camera.clear("grey")

        # Draw background and spawn plates
        for plate in nextLevelPlates:
            camera.draw(plate)
        for i in doors:
            camera.draw(i)

        # gravity
        player.speedy += 1
        skel.speedy += 1
        player.y += player.speedy
        skel.y += skel.speedy

        # Skeletons
        updateSkels()

        # Game over condition
        update_health()

        # Next level check
        new_level_check()

        # update player
        updatePlayer(keys)

        # Updates and Draw keys
        update_keys()

        # Draw spawn plates
        for plate in spawnPlates:
            camera.draw(plate)

        # Collision with floor
        notJumping = False  # Default set to jumping, will turn True if player does not touch any floor in floors
        for floor in floors:
            camera.draw(floor)
            if player.bottom_touches(floor) and pygame.K_SPACE in keys:
                player.speedy = jumpHeight
            if player.touches(floor):
                player.move_to_stop_overlapping(floor)
            if player.bottom_touches(floor):
                notJumping = True  # player is touching floor, not jumping

        # Prevents player from running out of camera view
        if player.x > camera.x + (width / 2) - 10:  # Right side
            player.x = camera.x + (width / 2) - 10
        if player.x < camera.x - (width / 2) + 10:  # Left Side
            player.x = camera.x - (width / 2) + 10

        # increments frame Counter
        frameCounter += 1

        # drawing gameboxes
        camera.draw(skel)
        if current_level != 7:  # Only shows current level if not finished
            camera.draw(gamebox.from_text(camera.x - (width / 2) + 60, 20, "Current Level " + str(current_level), 20, "red"))
        if current_level == 7:  # Only runs when game finished
            camera.draw(gamebox.from_text(camera.x, camera.y, "You Win!!!", 65, "gold"))
            camera.draw(gamebox.from_text(camera.x, camera.y + 50, "Press R to Play Again", 40 , "gold"))
            if pygame.K_r in keys:
                health = 100
                died = False
                frameCounter = 0
                player.speedy = 0
                camera.x = width / 2
                player_inventory = []
                milsecs = 0
                current_level = 1
                endSkelWalk = 120
                time_walk = 200
                player.x = spawnPlates[0].x
                player.y = spawnPlates[0].y
                skel.x = 1.5 * width
                skel.y = (height /2) + 150
        camera.draw(gamebox.from_text(camera.x + (width / 2) - 90, camera.y - (height / 2) + 20, "Inventory :", 20, 'red'))
        if key1 in player_inventory:
            camera.draw(gamebox.from_text(camera.x + (width / 2) - 60, camera.y - (height / 2) + 40, "First Key", 20, 'red'))
        if key2 in player_inventory:
            camera.draw(gamebox.from_text(camera.x + (width / 2) - 60, camera.y - (height / 2) + 55, "Second Key", 20, 'red'))
        if key3 in player_inventory:
            camera.draw(gamebox.from_text(camera.x + (width / 2) - 60, camera.y - (height / 2) + 70, "Third Key", 20, 'red'))
        if key4 in player_inventory:
            camera.draw(gamebox.from_text(camera.x + (width / 2) - 60, camera.y - (height / 2) + 85, "Fourth Key", 20, 'red'))
        if key5 in player_inventory:
            camera.draw(gamebox.from_text(camera.x + (width / 2) - 60, camera.y - (height / 2) + 100, "Fifth Key", 20, 'red'))
        if key6 in player_inventory:
            camera.draw(gamebox.from_text(camera.x + (width / 2) - 60, camera.y - (height / 2) + 115, "Sixth Key", 20, 'red'))
        camera.draw(player)
        camera.display()
    else:
        if pygame.K_r in keys:
            health = 100
            died = False
            frameCounter = 0
            player.speedy = 0
            camera.x = width/2
            player_inventory = []
            milsecs = 0
            if current_level == 4:
                skel.scale_by(2)
            current_level = 1
            endSkelWalk = 120
            time_walk = 200
            player.x = spawnPlates[0].x
            player.y = spawnPlates[0].y
            skel.x = 1.5 * width
            skel.y = (height / 2) + 150

ticks_per_second = 60
gamebox.timer_loop(ticks_per_second, tick)