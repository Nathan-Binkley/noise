import pygame
import random
import noise
#Basic premise is to create "noise" More specifically Perlin noice using Pygame to visualize this noise

def createNoise(x = 50, y = 50):
    master_points = []
    startPoint = 0
    for i in range(x):
        startPoint = random.randint(0,10000)
        rowPoints = []
        for i in range(y):
            choice = random.randint(0,2) #grow (2) or shrink (0) or stay equal (1)
            rowPoints.append(startPoint) # all 3 RGB for this particular pixel
            if choice == 2:
                startPoint += random.randint(0,30)
            elif choice == 0:
                startPoint -= random.randint(0,30)
            else:
                pass
        master_points.append(rowPoints) # Creates a 2D array
    return master_points

def getMaxMin2D(Array): #Helpful to get a normalized scale of the noise
    maximum = Array[0][0]
    minimum = Array[0][0]
    for i in Array:
        for j in i:
            if j > maximum: 
                maximum = j
            if j < minimum:
                minimum = j
    return [minimum, maximum]


def displayNoise():

    pass

print(createNoise())
