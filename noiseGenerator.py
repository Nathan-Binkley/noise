import pygame
import random
import os, sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import random
from pygame import gfxdraw
#Basic premise is to create "noise" More specifically Perlin noice using Pygame to visualize this noise

WHITE = (255,255,255)
BLACK = (0,0,0)
WIDTH = 500
HEIGHT = 500
BW = False #Set to true if you want just black and white noise

#pygame.gfxdraw.pixel(surface, x, y, color) -- PUTTING A COLOR AT A PIXEL

def createNoise():
    master_points = []
    for i in range(WIDTH):
        x_points = []
        for j in range(HEIGHT):
            x_points.append(random.randint(0,255))
        master_points.append(x_points)
    return master_points

def createPNoise(x = WIDTH, y = HEIGHT):
    master_points = []
    startPoint = 0
    for i in range(x):
        startPoint = random.randint(500,10000)
        rowPoints = []
        for i in range(y):
            choice = random.randint(0,2) #grow (2) or shrink (0) or stay equal (1)
            rowPoints.append(startPoint % 255) # all 3 RGB for this particular pixel
            if choice == 2:
                startPoint += random.randint(3,30)
            elif choice == 0:
                startPoint -= random.randint(3,30)
            else:
                pass
        master_points.append(rowPoints) # Creates a 2D array
    
    return master_points

def getMinMax2D(Array): #Helpful to get a normalized scale of the noise
    maximum = Array[0][0]
    minimum = Array[0][0]
    for i in Array:
        for j in i:
            if j > maximum: 
                maximum = j
            if j < minimum:
                minimum = j
    return [minimum, maximum]


def displayNoise(Noise):
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT)) 
    y = 0
    x = 0
    fpsClock = pygame.time.Clock()  
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for row in Noise:
            x = 0
            for pixel in row:
                if not BW:
                    window.set_at((x, y), (pixel,pixel,pixel))
                else:
                    if pixel > 255//2:
                        window.set_at((x, y), BLACK)
                    else:
                        window.set_at((x, y), WHITE)
                x += 1
            y += 1

        pygame.display.flip()
        fpsClock.tick(30)

global_min = []
global_max = []

x = createNoise()
minMax = getMinMax2D(x)
Loc_Min = minMax[0]
Loc_Max = minMax[1]
global_min.append(Loc_Min)
global_max.append(Loc_Max)
displayNoise(x)


#print(x)
#print("MIN: " + str(min(global_min)) + " MAX: " + str(max(global_max)))