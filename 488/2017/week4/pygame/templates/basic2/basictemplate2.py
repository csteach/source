# import modules for pygame template
import pygame

# variables for pygame
winWidth = 800
winHeight = 600
FPS = 30

# variables for commonly used colours
BLUE = (0, 0, 255)

# initialise pygame settings and create game window
pygame.init()
pygame.mixer.init()
window = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("game template")
clock = pygame.time.Clock()

# create the game loop
active = True
# check game loop is active
while active:
    # monitor fps and keep game running at set speed
    clock.tick(FPS)
    # 'processing' inputs (events)
    for event in pygame.event.get():
        # check for window close click
        if event.type == pygame.QUIT:
            # update boolean for running
            active = False
    # 'updating' the game

    # 'rendering' to the window
    window.fill(BLUE)
    # 'flip' display - always after drawing...
    pygame.display.flip()

# quit the Pygame window, exiting the game
pygame.quit()
