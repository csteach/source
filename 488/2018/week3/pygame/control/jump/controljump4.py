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
pygame.display.set_caption("control - keyboard events - jump and fall - gravity")

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
gravity = 1.0

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
    global shapeY, shapeJY, shapeJump, gravity

    # check upward speed > 1.0
    if shapeJY > 1.0:
        # gradually decrease upward speed to less than 1.0
        shapeJY = shapeJY * 0.9
    else:
        # less than 1.0, reset to 0.0 to allow shape to fall
        shapeJY = 0.0
        # stop jump
        shapeJump = False

    # check if shape in air - use gravity to descend
    if shapeY < winHeight - shapeSize:
        shapeY += gravity
        gravity = gravity * 1.1
    else:
        shapeY = winHeight - shapeSize
        gravity = 1.0

    shapeY -= shapeJY

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
