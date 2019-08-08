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
rectX = winWidth / 2
rectY = winHeight / 2

# create game loop
while True:
    # 'processing' inputs (events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit()
    # 'updating' the game
    # modify rectX by 4 pixels - higher creates impression of faster animation...
    rectX -= 4
    # 'rendering' to the window
    window.fill(WHITE)
    # draw rectangle
    pygame.draw.rect(window, GREEN, (rectX, rectY, 15, 10))

    # 'flip' display - always after drawing...
    pygame.display.flip()
