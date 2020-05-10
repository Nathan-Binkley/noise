import random
import os, sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # ONLY WORKS IF YOU IMPORT PYGAME *AFTER* YOU DO THIS -- Note to self
import pygame
import random
#Basic premise is to create "noise" More specifically Perlin noice using Pygame to visualize this noise

WHITE = (255,255,255)
BLACK = (0,0,0)
WIDTH = 500 # SET LARGER IF YOU WANT YOUR LAPTOP TO DIE -- or if running on more beefy PC
HEIGHT = 500 # 800-1000 is optimal stress test
RESOLUTION = 1
BW = False # Set to true if you want just black and white noise

noiseType = 0 #1 for regular Noise, non-1 for Perlin Noise


def createNoise(): # Creates matrix of 1s and 0s
    master_points = []
    for i in range(HEIGHT):
        x_points = []
        for j in range(WIDTH):
            x_points.append(random.randint(0,1))
        master_points.append(x_points)

    return master_points

def createPNoise(x = WIDTH, y = HEIGHT): # Creates ratios between 0 and 1
    
    master_points = []
    startPoint = 0
    above = 0
    addSub = 0

    for i in range(x):
        try:
            startAbove = master_points[i-1][0]
        except:
            startAbove = random.randint(500,1000)
        addSub = random.randint(0,2)
        if addSub == 0 and startAbove > 0: #subtract
            startPoint = startAbove - random.randint(3,30)
        elif addSub == 2: # add
            startPoint = startAbove + random.randint(3,30)
        else: #Do nothing if it's 1
            pass

        rowPoints = []

        for j in range(y):
            try:
                above = master_points[i-1][j] 
                # print("ABOVE CURRENT POINT: " + str(above))
                # print("CURRENT POINT: " + str(startPoint))
            except Exception as e:
                # print(e)
                above = 0

            choice = random.randint(0,2) #grow (2) or shrink (0) or stay equal (1)
            rowPoints.append(startPoint) # all 3 RGB for this particular pixel

            if choice == 2: #Add to

                startPoint += random.randint(3,30)
            
            elif choice == 0: #Subtract from

                startPoint -= random.randint(3,30)

            else:
                pass

        master_points.append(rowPoints) # Creates a 2D array

    # print(scalar)
    
    #Can probably do this somewhere in the main loop up there^^^, but idk a way for it to remain smooth really atm.

    for i in range(len(master_points)): #ROW #Ensuring no negative values
        for j in range(len(master_points[i])): #COL
            if master_points[i][j] < 0:
                master_points[i][j] *= -1
            
    scalar = getMinMax2D(master_points)
    minPoints = scalar[0]
    maxPoints = scalar[1]
    
    for i in range(len(master_points)): #ROW #SCALING
        for j in range(len(master_points[i])): #COL
            master_points[i][j] = master_points[i][j]/maxPoints

    # print(master_points)

    return master_points # returns scaled % values from pixel value/max

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
    window = pygame.display.set_mode((WIDTH * RESOLUTION , HEIGHT * RESOLUTION )) 
    fpsClock = pygame.time.Clock()  

    while True:
        y = 0
        x = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        for row in Noise:
            x = 0
            for pixel in row:
                # print(pixel)
                # print(int(pixel * 255))
                if not BW:
                    try:
                        pygame.draw.rect(window,(int(pixel*255), int(pixel*255), int(pixel*255)),(x, y, RESOLUTION, RESOLUTION))
                    except Exception as e:
                        print(e)
                        print(pixel*255)
                else:
                    if noiseType == 1:
                        pygame.draw.rect(window,(int(pixel*255), int(pixel*255), int(pixel*255)),(x, y, RESOLUTION, RESOLUTION))
                    else:
                        if int(pixel * 255) > 255//2:
                            pygame.draw.rect(window,BLACK,(x, y, RESOLUTION, RESOLUTION))
                        else:
                            pygame.draw.rect(window,WHITE,(x, y, RESOLUTION, RESOLUTION))
                x += RESOLUTION
            y += RESOLUTION
        
        pygame.display.flip()
        fpsClock.tick(30)

global_min = []
global_max = []

noise = 0
if noiseType == 1:
    noise = createNoise()
else:
    noise = createPNoise()

displayNoise(noise)