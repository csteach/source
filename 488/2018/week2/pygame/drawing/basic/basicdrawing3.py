# import modules for pygame template
import pygame, sys

# variables for pygame
winWidth = 800
winHeight = 600

# variables for commonly used colours
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# initialise pygame settings and create game window
pygame.init()
window = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("basic drawing - 3")

# define game quit and program exit
def gameExit():
    pygame.quit()
    sys.exit()

# create game loop
while True:
    # 'processing' inputs (events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit()
    # 'updating' the game

    # 'rendering' to the window
    window.fill(BLUE)
    # draw a single line
    pygame.draw.line(window, WHITE, (0, 300), (800, 300), 1)

    # draw a triangle - three lines
    pygame.draw.lines(window, YELLOW, True, ((325, 275), (350, 300), (300, 300), 2))
    # draw a triangle 2 - three lines
    pygame.draw.lines(window, YELLOW, True, ((475, 200), (575, 300), (375, 300), 2))
    #draw a triangle 3 - three lines
    pygame.draw.lines(window, YELLOW, True, ((650, 250), (700, 300), (600, 300), 2))

    # draw a circle
    pygame.draw.circle(window, WHITE, (700, 75), 30 , 1)

    # draw an ellipse
    pygame.draw.ellipse(window, RED, (120, 30, 80, 90))

    # draw a couple of lines
    pygame.draw.line(window, WHITE, (150, 115), (150, 140), 1)
    pygame.draw.line(window, WHITE, (170, 115), (170, 140), 1)

    # draw a rectangle
    pygame.draw.rect(window, GREEN, (140, 140, 40, 30))

    # 'flip' display - always after drawing...
    pygame.display.flip()
