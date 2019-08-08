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

# initialise pygame settings and create game window
pygame.init()
window = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("basic drawing - 1")

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
    # draw some rectangles
    pygame.draw.rect(window, WHITE, (200, 200, 100, 50))
    pygame.draw.rect(window, CYAN, (300, 150, 100, 100))
    pygame.draw.rect(window, MAGENTA, (400, 100, 100, 150))
    # draw a circle
    pygame.draw.circle(window, WHITE, (150, 100), 30 , 2)
    # draw an ellipse & containing rectangle - extra 2 is for width of rect border
    pygame.draw.ellipse(window, GREEN, (200, 50, 100, 30))
    pygame.draw.rect(window, GREEN, (200, 50, 100, 30), 2)

    # 'flip' display - always after drawing...
    pygame.display.flip()
