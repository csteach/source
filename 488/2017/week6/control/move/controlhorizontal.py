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
pygame.display.set_caption("control - keyboard events - horizontal move")

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
leftDown = False
rightDown = False

# clock and fps
# clock = pygame.time.Clock()
# max_fps = 30

# define game quit and program exit
def gameExit():
    pygame.quit()
    sys.exit()

def move():
    global rectX

    # move left
    if leftDown:
        # check shape not exit window to left
        if rectX > 0.0:
            rectX -= rectSpeed
    # move right
    if rightDown:
        # check shape not exit window to right
        if rectX + rectSize < winWidth:
            rectX += rectSpeed

# create game loop
while True:
    # set clock
    #msElapsed = clock.tick(max_fps)
    #print(msElapsed)
    # 'processing' inputs (events)
    for event in EVENTS.get():
        # check keyboard events - keydown
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                leftDown = True
            if event.key == pygame.K_RIGHT:
                rightDown = True

        # check keyboard events - keyup
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                leftDown = False
            if event.key == pygame.K_RIGHT:
                rightDown = False

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
