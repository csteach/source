# import modules for pygame template
import pygame, random, sys, os
# import event
import pygame.event as EVENTS

# variables for pygame window - space invaders vertical screen style
winWidth = 480
winHeight = 640
FPS = 60

# variables for commonly used colours
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# initialise pygame settings and create game window
pygame.init()
window = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("shooter 0.1 - move & control")
clock = pygame.time.Clock()

# create a default player sprite for the game
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect() #checks images and get rect...
        self.rect.centerx = winWidth / 2
        self.rect.bottom = winHeight - 20
        self.speed_x = 0

    # update per loop iteration
    def update(self):
        self.speed_x = 0
        key_state = pygame.key.get_pressed()
        if key_state[pygame.K_LEFT]:
            self.speed_x = -5
        if key_state[pygame.K_RIGHT]:
            self.speed_x = 5
        self.rect.x += self.speed_x
        if self.rect.right > winWidth:
            self.rect.right = winWidth
        if self.rect.left < 0:
            self.rect.left = 0

# define game quit and program exit
def gameExit():
    pygame.quit()
    sys.exit()

# game sprite group
game_sprites = pygame.sprite.Group()
# create player object
player = Player()
# add sprite to game's sprite group
game_sprites.add(player)

# create game loop
while True:
    # check loop is running at set speed
    clock.tick(FPS)
    # 'processing' inputs (events)
    for event in EVENTS.get():
        # check keyboard events - keydown
        if event.type == pygame.KEYDOWN:

            # check for ESCAPE key
            if event.key == pygame.K_ESCAPE:
                gameExit()

        # check click on window exit button
        if event.type == pygame.QUIT:
            gameExit()
    # 'updating' the game
    # update all game sprites
    game_sprites.update()
    # draw
    # 'rendering' to the window
    window.fill(BLACK)
    game_sprites.draw(window)
    # update the display window...
    pygame.display.update()
