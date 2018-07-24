# import modules for pygame template
import pygame, sys
# import event
import pygame.event as EVENTS

# variables for pygame window
winWidth = 640
winHeight = 480

# initialise pygame settings and create game window
pygame.init()
#window = pygame.display.set_mode((winWidth, winHeight), pygame.FULLSCREEN)
#window = pygame.display.set_mode((winWidth, winHeight), pygame.RESIZABLE)
window = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("control - keyboard events - vertical move")

# variables for commonly used colours
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
GREEN = (0, 255, 0)

# rectangle variables
rectSize = 20
rectX = winWidth / 2
rectY = winHeight / 2
rectSpeed = 4.0

# event variables - keyboard
upDown = False
downDown = False

# clock and fps
# clock = pygame.time.Clock()
# max_fps = 30

# define game quit and program exit
def gameExit():
    pygame.quit()
    sys.exit()

def move():
    global rectY

    # move up
    if upDown:
        # check shape not exit window at top
        if rectY > 0.0:
            rectY -= rectSpeed
    # move down
    if downDown:
        # check shape not exit window at bottom
        if rectY + rectSize < winHeight:
            rectY += rectSpeed

# create game loop
while True:
    # set clock
    #msElapsed = clock.tick(max_fps)
    #print(msElapsed)
    # 'processing' inputs (events)
    for event in EVENTS.get():
        # check keyboard events - keydown
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                upDown = True
            if event.key == pygame.K_DOWN:
                downDown = True

        # check keyboard events - keyup
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                upDown = False
            if event.key == pygame.K_DOWN:
                downDown = False

        # check click on window exit button
        if event.type == pygame.QUIT:
            gameExit()
    # 'updating' the game
    #elapsedSecs = msElapsed/1000
    #print(elapsedSecs)
    move()
    # draw
    # 'rendering' to the window
    window.fill(BLACK)
    pygame.draw.rect(window, WHITE, (rectX, rectY, rectSize, rectSize))
    # update the display window...
    pygame.display.update()
