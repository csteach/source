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
pygame.display.set_caption("basic animate - 2")

clock = pygame.time.Clock()
max_fps = 30

# define game quit and program exit
def gameExit():
    pygame.quit()
    sys.exit()

# rgb colours for rect
rectRed = random.randint(0, 255)
rectGreen = random.randint(0, 255)
rectBlue = random.randint(0, 255)

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
    #print(elapsedSecs)
    if rectRed >= 255:
        rectRed = random.randint(0, 255)
    else:
        rectRed +=1
    if rectGreen >= 255:
        rectGreen = random.randint(0, 255)
    else:
        rectGreen +=1
    if rectBlue >= 255:
        rectBlue = random.randint(0, 255)
    else:
        rectBlue +=1
    # draw
    # 'rendering' to the window
    window.fill(WHITE)
    pygame.draw.rect(window, (rectRed, rectGreen, rectBlue), (50, 50, winWidth / 2, winHeight / 2))

    # update the display window...
    pygame.display.update()
