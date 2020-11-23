import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class cube(object):
    rows = 20
    w = 500
    def __init__(self,start,dirnx=1,dirny=0,color=(255,0,0)):
        pass

    def move(self, dirnx, dirny):
        pass

    def draw(self, surface, eyes=False):
        pass


class snake(object):
    def __init__(self, color, pos):
        pass

    def move(self):
        pass

    def reset(self, pos):
        pass

    def addCube(self):
        pass

    def draw(self, surface):
        pass


def drawGrid(w, rows, surface):
    sizeBtwn = w // rows # Gives the distance between the lines

    x = 0 # Keps track of the current x
    y = # Keeps track of the current y
    for l in range(rows): # Draw on vertical and one horizontal lin each loop
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255,255,255), (x,0),(x,w))
        pygame.draw.line(surface, (255,255,255), (0,y),(w,y))

def redrawWindow(surface):
    surface.fill((0,0,0)) # Fills the screen with black
    drawGrid(surface) # Will draw our grid lines
    pygame.display.update() # Updates the screen

def randomSnack(rows, item):
    pass

def message_box(subject, content):
    pass

def main():
    global width, rows, s
    width = 500 # Width of my screen
    height = 500 # Height of my screen
    rows = 20 # Amount of rows

    win = pygame.display.set_mode((width, height))  # Creates my screen object

    s = snake((255,0,0), (10,10)) # Creates a sanke object which well code later

    clock = pygame.time.Clock() # creating a clock object

    flag = True
    # STARTING MAIN LOOP

    while flag:
        pygame.time.delay(50) # This will delay the game so it doesn't run too quickly
        clock.tick(10) # Will ensure our game runs at 10 fps
        redrawWindow(win) # This will refresh our screen

main()