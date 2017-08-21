# import modules for pygame template
import pygame, sys, random

# variables for pygame
winWidth = 800
winHeight = 600

# variables for commonly used colours
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
GREEN = (0, 255, 0)

# initialise pygame settings and create game window
pygame.init()
window = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("basic animate - 3")

clock = pygame.time.Clock()
max_fps = 30

# define game quit and program exit
def gameExit():
    pygame.quit()
    sys.exit()

# rect coords...start at the centre
rectX = winWidth / 2
rectY = winHeight / 2
# rect speed and direction change
rectWidth = 30
rectHeight = 30

# create game loop
while True:
    # set clock
    msElapsed = clock.tick(max_fps)
    #print(msElapsed)
    # 'processing' inputs (events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit()
    # 'updating' the game
    elapsedSecs = msElapsed/1000
    # animate left to right
    # check position of rectX
    if rectX > winWidth:
        rectX = 0
    else:
        rectX +=4

    # draw
    # 'rendering' to the window
    window.fill(WHITE)
    pygame.draw.rect(window, BLUE, (rectX-rectWidth / 2, rectY-rectHeight / 2, rectWidth, rectHeight))

    # update the display window...
    pygame.display.update()
