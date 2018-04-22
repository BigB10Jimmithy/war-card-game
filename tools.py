from random import randint
import pygame
from pygame.locals import *
import time
import math

######################constants###############################

white = (255,255,255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0,255, 0) #might not needed
black = (0,0,0)
grey = (125,125,125)
brown = (128,30,30)
yellow = (255,255,0)
purple = (255,0,255)
clearblue = (0,255,255)
allColors = {1:red,2:blue,3:green,4:black,5:yellow,6:purple}

############################################################

cardWidth = 60
cardHeight = 80
btnWidth = 200
btnHeight = 100
btnpx = 300
btnpy = 600

#find out what this is
r2 = 5.0/math.sqrt(2.0)

#might not need this
actionTime = 0.1

#############################################################

class atHolder(object):

    def __init__(self, y, x):
        self.inside = None
        self.placed = False
        self.beaten = False
        self.x = x
        self.y = y
        #sorts out played cards positional information
        self.px = 145 + x*(cardWidth + 10)
        self.py = 103 + y*(cardHeight + 10)

    def add(self, cards):
        if not (self.placed or self.beaten):
            self.placed = True
            cards.x = self.x
            cards.y = self.y
            cards.px = self.px
            cards.py = self.py
            cards.clickedCard = False #I think this is cardClicked double check
            self.inside = cards

    def defeated(self):
        if not self.beaten:
            self.beaten = True

##########################################################

def txtObjects(text, font):
    disTxt = font.render(text, True, black)
    return disTxt, disTxt.get_rect()

def btn(MapGrid, message, x, y, w, h, icolour, acolour, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(MapGrid, acolour, (x, y, w, h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(MapGrid, icolour, (x, y, w, h))

    Stxt = pygame.font.SysFont("comicsansms", 20)
    disTxt, txtRect = txtObjects(message, Stxt)
    txtRect.center = ( (x+(w/2)), (y+(h/2)) )
    MapGrid.blit(disTxt, txtRect)

#retryBtn creates the button the reload the game once it's finished
def retryBtn(message, MapGrid):
    #change this name check if you refered to a changed version anywhere else
    hasClickedOnButton = False
    label = pygame.font.SysFont("monospace", 20).render(message, 10, black)
    MapGrid.blit(label, (btnpx + 25, btnpy + 50))
    pygame.draw.rect(MapGrid, red, pygame.Rect(btnpx, btnpy, btnWidth, btnHeight), 2)
    pygame.display.flip()
    
    #while condition for when the user clicks on the retry button
    while not hasClickedOnButton:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                click_x = event.pos[0]
                click_y = event.pos[1]
                if click_x >= btnpx and click_x <= btnpx + btnWidth and click_y >= btnpy and click_y <= btnpy + btnHeight:
                    hasClickedOnButton = True

def Point():
    # Really not sure I need this, don't even know what it does
    return bool(randint(0,1))

def getX(number,x):
    if number == 0:
        return x-1
    elif number == 1 :
        return x
    elif number == 2:
        return x+1
    elif number == 3:
        return x+1
    elif number == 4:
        return x+1
    elif number == 5:
        return x
    elif number == 6:
        return x-1
    elif number == 7:
        return x-1


def getY(number,y):
    if number == 0:
        return y-1
    elif number == 1:
        return y-1
    elif number == 2:
        return y-1
    elif number == 3:
        return y
    elif number == 4:
        return y+1
    elif number == 5:
        return y+1
    elif number == 6:
        return y+1
    elif number == 7:
        return y


    
