import math
import numpy as np


def whichGun(gunType):
    if gunType == 'R':
        gunHeight = int()
        gunWidth = int()
        gunLength = int()
        return gunHeight, gunWidth, gunLength
    elif gunType == 'D':
        gunHeight = int()
        gunWidth = int()
        gunLength = int()
        return gunHeight, gunWidth, gunLength
    elif gunType == 'E':
        gunHeight = int()
        gunWidth = int()
        gunLength = int()
        return gunHeight, gunWidth, gunLength
    elif gunType == 'F':
        gunHeight = int()
        gunWidth = int()
        gunLength = int()
        return gunHeight, gunWidth, gunLength


def filteringBlock(gunHeight, gunLength, gunWidth):
    # Start position can be in the top left corner. Set the top left corner of the block to be the top left corner of the baseplate.
    # Create Nx block
    status = True

    while status:
        collision = bool
        # Need to chekc for object collision with the maze walls.
        # NXOpen.Mechatronics.CollisionSensor
        collisionCheck = NXOpen.Mechatronics.CollisionSensorBuilder
        if collisionCheck == True:
            # mark the basearea red
            # Update to the next location - Updating the corner position of the block with the length of the block
        else:
            # mark the basearea green
            # Update to the next location - Updating the corner position of the block with the length of the block
            # when it reaches the end of the platform, jump back and move width of block down.
            # repeat
            # Need to check that the x and y values of the block is on the intervall of the baseplate.

    return
