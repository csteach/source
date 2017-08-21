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

# game assets
game_dir = os.path.dirname(__file__)
# relative path to assets dir
assets_dir = os.path.join(game_dir, "assets")
# relative path to image dir
img_dir = os.path.join(assets_dir, "images")

# initialise pygame settings and create game window
pygame.init()
window = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("shooter 0.4 - adding graphics")
clock = pygame.time.Clock()

# create a default player sprite for the game
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # load ship image & scale to fit game window...
        self.image = pygame.transform.scale(ship_img, (49, 37))
        # set colorkey to remove black background for ship's rect
        self.image.set_colorkey(BLACK)
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

    # fire projectile from top of player sprite object
    def fire(self):
        # set position of projectile relative to player's object rect for centerx and top
        projectile = Projectile(self.rect.centerx, self.rect.top)
        # add projectile to game sprites group
        game_sprites.add(projectile)
        # add each projectile to sprite group for all projectiles
        projectiles.add(projectile)

# create a generic enemy sprite for the game - standard name is *mob*
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = asteroid_img
        # set colorkey to remove black background for meteor's rect
        self.image.set_colorkey(BLACK)
        # specify bounding rect for sprite
        self.rect = self.image.get_rect()
        # specify random start posn & speed of enemies
        self.rect.x = random.randrange(winWidth - self.rect.width)
        self.rect.y = random.randrange(-100, -50)
        # random speed along the x-axis
        self.speed_x = random.randrange(-3, 3)
        # random speed along the y-axis
        self.speed_y = random.randrange(1, 7)

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        # check if enemy sprite leaves the bottom of the game window - then randomise at the top...
        if self.rect.top > winHeight + 15 or self.rect.left < -15 or self.rect.right > winWidth + 15:
            # specify random start posn & speed of enemies
            self.rect.x = random.randrange(winWidth - self.rect.width)
            self.rect.y = random.randrange(-100, -50)
            self.speed_x = random.randrange(-3, 3)
            self.speed_y = random.randrange(1, 7)

# create a generic projectile sprite - for bullets, lasers &c.
class Projectile(pygame.sprite.Sprite):
    # x, y - add specific location for object relative to player sprite
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = laser_img
        # set colorkey to remove black background for laser's rect
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        # weapon fired from front (top) of player sprite...
        self.rect.bottom = y
        self.rect.centerx = x
        # speed of projectile up the screen
        self.speed_y = -10

    def update(self):
        # update y relative to speed of projectile on y-axis
        self.rect.y += self.speed_y
        # remove from game window - if it goes beyond bounding for y-axis at top...
        if self.rect.bottom < 0:
            # kill() removes specified sprite from group...
            self.kill()



# define game quit and program exit
def gameExit():
    pygame.quit()
    sys.exit()

# load graphics
bg_img = pygame.image.load(os.path.join(img_dir, "bg-purple-lg.png")).convert()
# add rect for bg - helps locate background
bg_rect = bg_img.get_rect()
# player's ship
ship_img = pygame.image.load(os.path.join(img_dir, "ship-blue.png")).convert()
# ship's laser
laser_img = pygame.image.load(os.path.join(img_dir, "laser-blue.png")).convert()
# asteroid
asteroid_img = pygame.image.load(os.path.join(img_dir, "asteroid-med-grey.png")).convert()

# sprite groups - game, mob, projectiles...
game_sprites = pygame.sprite.Group()
mob_sprites = pygame.sprite.Group()
projectiles = pygame.sprite.Group()
# create player object
player = Player()
# add sprite to game's sprite group
game_sprites.add(player)
# loop through enemy objects
for i in range(10):
    mob = Mob()
    # add to game_sprites group to get object updated
    game_sprites.add(mob)
    # add to mob_sprites group - use for collision detection &c.
    mob_sprites.add(mob)

running = True
# create game loop
while running:
    # check loop is running at set speed
    clock.tick(FPS)
    # 'processing' inputs (events)
    for event in EVENTS.get():
        # check keyboard events - keydown
        if event.type == pygame.KEYDOWN:
            # check for ESCAPE key
            if event.key == pygame.K_ESCAPE:
                gameExit()
            elif event.key == pygame.K_SPACE:
                # fire laser beam...
                player.fire()

        # check click on window exit button
        if event.type == pygame.QUIT:
            gameExit()
    # 'updating' the game
    # update all game sprites
    game_sprites.update()

    # add check for sprite group collide with another sprite group - projectiles hitting enemy objects - use True to delete sprites from each group...
    collisions = pygame.sprite.groupcollide(mob_sprites, projectiles, True, True)
    # add more mobs for those hit and deleted by projectiles
    for collision in collisions:
        mob = Mob()
        game_sprites.add(mob)
        mob_sprites.add(mob)

    # add check for collision - enemy and player sprites (False = hit object is not deleted from game window)
    collisions = pygame.sprite.spritecollide(player, mob_sprites, False)
    # check collisions for game window
    if collisions:
        running = False

    # draw
    # draw background image - specify image file and rect to load image
    window.blit(bg_img, bg_rect)
    #window.fill(BLACK)
    game_sprites.draw(window)
    # update the display window...
    pygame.display.update()
