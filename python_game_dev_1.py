##CTRL + SHIFT + B <-- WHEN NO INPUT FROM USER
##OTHERWISE USE BELOW
##Select all CTRL + ENTER
##Or CRTL + ` and run from terminal
##ALT + SHIFT + T for new terminal
##Run from CMD
    ##cd C:\Users\amber\OneDrive\Desktop\Programming\pythonPractice
    ##name_of_file.py


import pygame

#initializing pygame package
pygame.init()

#giving a window with dimensions (w,h) <-- as a single parameter (tuple)
gameDisplay = pygame.display.set_mode((800,600))

#giving the game a title (at top of window)
pygame.display.set_caption('Racing Game')

#clock (times fps)
clock = pygame.time.Clock()

#game superloop
crashed = False

while not crashed:
    #pygame.event.get will get ANY event that happens (mouse click, key press...)
    for event in pygame.event.get():
        #if user x's out of the window
        if event.type == pygame.QUIT:
            crashed = True
        print(event)
    #update display (can put in parameters for specific updates)
    pygame.display.update()

    #dictating fps (can make things move faster)
    clock.tick(60)

#stops pygame from running
pygame.quit()
#stop python from running
quit()
