# import modules for pygame template
import pygame, random, sys, os
# import event
import pygame.event as EVENTS

# variables for pygame window
winWidth = 640
winHeight = 480
FPS = 30

# variables for commonly used colours
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# game assets
game_dir = os.path.dirname(__file__)
# relative path to assets dir
assets_dir = os.path.join(game_dir, "assets")
# relative path to image dir
img_dir = os.path.join(assets_dir, "images")

# initialise pygame settings and create game window
pygame.init()
#window = pygame.display.set_mode((winWidth, winHeight), pygame.FULLSCREEN)
#window = pygame.display.set_mode((winWidth, winHeight), pygame.RESIZABLE)
window = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("sprites - basic")
clock = pygame.time.Clock()

# create a default player sprite for the game
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_dir, "yellow-ball.png")).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect() #checks images and get rect...
        self.rect.center = (winWidth / 2, winHeight / 2)
        self.y_speed = 4

    def update(self):
        self.rect.x += 3
        self.rect.y += self.y_speed
        if self.rect.bottom > winHeight - 200:
            self.y_speed = -4
        if self.rect.top < 200:
            self.y_speed = 4
        if self.rect.left > winWidth:
            self.rect.right = 0

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
    window.fill(WHITE)
    game_sprites.draw(window)
    # update the display window...
    pygame.display.update()
