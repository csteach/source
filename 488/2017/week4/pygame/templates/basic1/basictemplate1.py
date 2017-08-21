""" basic pygame window... """

# import modules
import sys
import pygame

# define start game
def start_game():
    """ start the game window... """
    pygame.init()
    window = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Basic Window")

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()

start_game()
