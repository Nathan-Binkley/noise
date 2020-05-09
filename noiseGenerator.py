import random
import os, sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # ONLY WORKS IF YOU IMPORT PYGAME *AFTER* YOU DO THIS -- Note to self
import pygame
import random
#Basic premise is to create "noise" More specifically Perlin noice using Pygame to visualize this noise

WHITE = (255,255,255)
BLACK = (0,0,0)
WIDTH = 50 # SET LARGER IF YOU WANT YOUR LAPTOP TO DIE -- or if running on more beefy PC
HEIGHT = 50 # 800-1000 is optimal stress test
RESOLUTION = 5
BW = False # Set to true if you want just black and white noise


def createNoise():
    master_points = []
    for i in range(HEIGHT):
        x_points = []
        for j in range(WIDTH):
            x_points.append(random.randint(0,255))
        master_points.append(x_points)
    return master_points

def createPNoise(x = WIDTH, y = HEIGHT):
    master_points = []
    startPoint = 0
    above = 0
    addSub = 0
    for i in range(x):
        try:
            startAbove = master_points[i-1][0]
        except:
            startAbove = random.randint(500,10000)
        addSub = random.randint(0,2)
        if addSub == 0: #subtract
            startPoint = startAbove - random.randint(3,30)
        elif addSub == 2: # add
            startPoint = startAbove + random.randint(3,30)
        else: #Do nothing if it's 1
            pass

        rowPoints = []

        for j in range(y):
            choice = random.randint(0,2) #grow (2) or shrink (0) or stay equal (1)
            rowPoints.append(startPoint % 255) # all 3 RGB for this particular pixel
            try:
                above = master_points[i-1][y] 
            except:
                above = 0
            if choice == 2: #ADD to
                startPoint += random.randint(3,30)
                
            elif choice == 0: #Subtract from
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
    window = pygame.display.set_mode((WIDTH * RESOLUTION, HEIGHT * RESOLUTION)) 

    y = 0
    x = 0

    fpsClock = pygame.time.Clock()  

    globalMin = getMinMax2D(Noise)[0]
    globalMax = getMinMax2D(Noise)[1]

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
                    pygame.draw.rect(window,(pixel,pixel,pixel),(x,y,RESOLUTION,RESOLUTION))
                else:
                    if pixel > 255//2:
                        pygame.draw.rect(window,BLACK,(x,y,RESOLUTION,RESOLUTION))
                    else:
                        pygame.draw.rect(window,WHITE,(x,y,RESOLUTION,RESOLUTION))
                x += RESOLUTION
            y += RESOLUTION
        y = 0
        pygame.display.flip()
        fpsClock.tick(30)

global_min = []
global_max = []

x = createPNoise()
minMax = getMinMax2D(x)
Loc_Min = minMax[0]
Loc_Max = minMax[1]
# global_min.append(Loc_Min)
# global_max.append(Loc_Max)
displayNoise(x)


#print(x)
#print("MIN: " + str(min(global_min)) + " MAX: " + str(max(global_max)))