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
# relative path to music and sound effects dir
snd_dir = os.path.join(assets_dir, "sounds")

# initialise pygame settings and create game window
pygame.init()
# add sound mixer to game
pygame.mixer.init()
window = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("music - basic - add sound effects and game music - 2")
clock = pygame.time.Clock()

# specify font name to find
font_match = pygame.font.match_font('arial')
# text output and render function - draw to game window
def textRender(surface, text, size, x, y):
    # specify font for text render - uses found font and size of text
    font = pygame.font.Font(font_match, size)
    # surface for text pixels - TRUE = anti-aliased
    text_surface = font.render(text, True, WHITE)
    # get rect for text surface rendering
    text_rect = text_surface.get_rect()
    # specify a relative location for text
    text_rect.midtop = (x, y)
    # add text surface to location of text rect
    surface.blit(text_surface, text_rect)

# define game quit and program exit
def gameExit():
    pygame.quit()
    sys.exit()

# initialise title for game window
welcome_title = "ancient asteroids - demo music..."

# load music and sound effects for use in game window
# load music for background playback in game window
pygame.mixer.music.load(os.path.join(snd_dir, 'space-music-bg.wav'))
# set music volume - reduce default volume
pygame.mixer.music.set_volume(0.7)

# play background music
pygame.mixer.music.play(loops=-1)

looping = True
# create game loop
while looping:
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

    # draw
    # draw game window and fill colour
    window.fill(BLUE)

    # draw text to game window - game score
    textRender(window, str(welcome_title), 18, winWidth / 2, 10)

    # update the display window...
    pygame.display.update()
