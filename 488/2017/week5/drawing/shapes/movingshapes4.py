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
pygame.display.set_caption("moving shapes - 1")

# define game quit and program exit
def gameExit():
    pygame.quit()
    sys.exit()

# rect coords...start at the centre
rectX = 0
rectY = 300

# create game loop
while True:
    # 'processing' inputs (events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit()
    # 'updating' the game
    # check position of rectX
    if rectX > winWidth:
        rectX = 0.0
    # modify rect coordinates
    rectX += 10
    # 'rendering' to the window
    window.fill(WHITE)
    # draw rectangle
    pygame.draw.rect(window, GREEN, (rectX, rectY, 30, 20))

    # 'flip' display - always after drawing...
    pygame.display.flip()
