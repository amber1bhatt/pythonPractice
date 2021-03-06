##CTRL + SHIFT + B <-- WHEN NO INPUT FROM USER
##OTHERWISE USE BELOW
##Select all CTRL + ENTER
##Or CRTL + ` and run from terminal
##ALT + SHIFT + T for new terminal
##Run from CMD
    ##cd C:\Users\amber\OneDrive\Desktop\Programming\pythonPractice
    ##name_of_file.py


import pygame
import time
import random

#initializing pygame package
pygame.init()

#variables for width and height for the window
display_width = 800
display_height = 600

#defining colors with rgb
black = (0,0,0)
white = (255,255,255)
car_width = 84

#giving a window with dimensions (w,h) <-- as a single parameter (tuple)
gameDisplay = pygame.display.set_mode((display_width,display_height))

#giving the game a title (at top of window)
pygame.display.set_caption('Racing Game')

#clock (times fps)
clock = pygame.time.Clock()

# load in car image
carImg = pygame.image.load('top-view-car-vehicle.png')

# blocks function
def things(thingx,thingy,thingw,thingh,color):
    #drawing a box to the screen (gameDisplay,color,[x,y,w,h])
    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])


# car function
def car(x,y):
    # pasting the car image onto the screen
    gameDisplay.blit(carImg,(x,y))

# text object function
def text_objects(text,font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

# display message function
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text,largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)

    pygame.display.update()

    # displays for 2 seconds
    time.sleep(2)

    #restart the game if you crash (and this message pops up)
    game_loop()


# crash function
def crash():
    message_display('You Crashed!!')


def game_loop():

    # x and y positions
    x = (display_width*0.45)
    y = (display_height*0.8)

    #change in position
    x_change = 0

    #starting location for block
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600

    #speed of the blocks
    thing_speed = 7

    #dimensions of blocks
    thing_width = 100
    thing_height = 100



    gameExit = False
    #game superloop
    while not gameExit:
        #pygame.event.get will get ANY event that happens (mouse click, key press...)
        for event in pygame.event.get():
            #if user x's out of the window quit the program
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # moving the car left and right
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

            # makes it so that you don't have to continuously press left and right to move
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        # make background white
        gameDisplay.fill(white)

        # drawing the blocks
        things(thing_startx,thing_starty,thing_width,thing_height,black)

        # making the block move down the screen
        thing_starty+=thing_speed

        # shows the car
        car(x,y)

        # car crashes if it hits a wall
        if x > display_width - car_width or x < 0:
            crash()

        # block is recreated after it passes the car (goes all the way to bottom of the screen)
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)

        # checks if the horizontal of the block (from bot left vertici to bot right vertici) is crossing over the car
        if y < thing_starty + thing_height:
            print("y crossover")

            #vertical collision detection
            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                print("x crossover")
                crash()

        #update display (can put in parameters for specific updates)
        pygame.display.update()

        #dictating fps (can make things move faster)
        clock.tick(90)

#run game loop
game_loop()

#stops pygame from running
pygame.quit()
#stop python from running
quit()
