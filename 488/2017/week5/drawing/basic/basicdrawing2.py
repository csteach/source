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

# initialise pygame settings and create game window
pygame.init()
window = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("basic drawing - 2")

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
    pygame.draw.lines(window, WHITE, True, ((400, 350), (450, 400), (350, 400), 1))

    #draw a pentagon - multiple lines
    pygame.draw.lines(window, YELLOW, True, ((50, 50), (75, 75), (63, 100), (38, 100), (25, 75)), 2)

    # 'flip' display - always after drawing...
    pygame.display.flip()
