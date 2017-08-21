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
pygame.display.set_caption("control - keyboard events - jump")

# variables for commonly used colours
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
GREEN = (0, 255, 0)

# rectangle variables
shapeSize = 20
shapeX = (winWidth / 2) - (shapeSize / 2)
shapeY = winHeight - shapeSize
shapeJY = 0.0
jumpHeight = 30.0

# event variables - keyboard
shapeJump = False

# clock and fps
# clock = pygame.time.Clock()
# max_fps = 30

# define game quit and program exit
def gameExit():
    pygame.quit()
    sys.exit()

def jump():
    global shapeY, shapeJY, shapeJump

    # check if shape in air - use gravity to descend
    if shapeJump == True:
        shapeY -= shapeJY
        print("in the air %8.2f" % (shapeJY))
        shapeJump = False


# create game loop
while True:
    # set clock
    #msElapsed = clock.tick(max_fps)
    #print(msElapsed)
    # 'processing' inputs (events)
    for event in EVENTS.get():
        # check keyboard events - keydown
        if event.type == pygame.KEYDOWN:
            # check for directional UP key
            if event.key == pygame.K_UP:
                if not shapeJump:
                    shapeJump = True
                    shapeJY += jumpHeight
            # check for ESCAPE key
            if event.key == pygame.K_ESCAPE:
                gameExit()

        # check click on window exit button
        if event.type == pygame.QUIT:
            gameExit()
    # 'updating' the game
    #elapsedSecs = msElapsed/1000
    #print(elapsedSecs)
    jump()
    # draw
    # 'rendering' to the window
    window.fill(WHITE)
    pygame.draw.rect(window, GREEN, (shapeX, shapeY, shapeSize, shapeSize))
    # update the display window...
    pygame.display.update()
