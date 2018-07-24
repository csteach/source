# import modules for pygame template
import pygame, random, sys, os
# import event
import pygame.event as EVENTS

# variables for pygame window
winWidth = 640
winHeight = 840
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
# relative path to music and sound effects dir
snd_dir = os.path.join(assets_dir, "sounds")

# initialise pygame settings and create game window
pygame.init()
# add sound mixer to game
pygame.mixer.init()
window = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("music - basic - add sound effects and game music - 1")
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

# create a default player sprite for the game
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # load player object image & scale to fit game window...
        self.image = pygame.transform.scale(player_img, (49, 37))
        # set colorkey to remove black background for ship's rect
        self.image.set_colorkey(BLACK)
        #check images and get rect...
        self.rect = self.image.get_rect()
        # set radius for circle bounding
        self.radius = 20
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
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
				# play laser beam sound effect
        laser_effect.play()

# create a generic extra sprite for the game - standard name is *mob*
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # set pristine original image for sprite object - random choice from list
        self.image_original = random.choice(mob_imgs)
        # set colour key for original image
        self.image_original.set_colorkey(BLACK)
        # set copy image for sprite rendering
        self.image = self.image_original.copy()
        # specify bounding rect for sprite
        self.rect = self.image.get_rect()
        # set radius for circle bounding
        self.radius = int(self.rect.width * 0.9 / 2)
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        # specify random start posn & speed of enemies
        self.rect.x = random.randrange(winWidth - self.rect.width)
        self.rect.y = random.randrange(-100, -50)
        # random speed along the x-axis
        self.speed_x = random.randrange(-3, 3)
        # random speed along the y-axis
        self.speed_y = random.randrange(1, 7)
        # set up rotation for sprite image - default rotate value, rotate speed to add diff. directions,
        self.rotation = 0
        self.rotate_speed = random.randrange(-7, 7)
        # check timer for last update to rotate
        self.rotate_update = pygame.time.get_ticks()

    def rotate(self):
        # check time - get time now and check if ready to rotate sprite image
        time_now = pygame.time.get_ticks()
        # check if ready to update...in milliseconds
        if time_now - self.rotate_update > 70:
            self.last_update = time_now
            # check how far image has rotated & then loop back to the start
            self.rotation = (self.rotation + self.rotate_speed) % 360
            # new image for rotation
            rotate_image = pygame.transform.rotate(self.image_original, self.rotation)
            # check location of original centre of rect
            original_centre = self.rect.center
            # set image to rotate image
            self.image = rotate_image
            # create new rect for image
            self.rect = self.image.get_rect()
            self.rect.center = original_centre

    def update(self):
        # call rotate update
        self.rotate()
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        # check if extra sprite leaves the bottom of the game window - then randomise at the top...
        if self.rect.top > winHeight + 15 or self.rect.left < -15 or self.rect.right > winWidth + 15:
            # specify random start posn & speed
            self.rect.x = random.randrange(winWidth - self.rect.width)
            self.rect.y = random.randrange(-100, -50)
            self.speed_x = random.randrange(-3, 3)
            self.speed_y = random.randrange(1, 7)

# create a generic projectile sprite - for bullets, lasers &c.
class Projectile(pygame.sprite.Sprite):
    # x, y - add specific location for object relative to player sprite
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(projectile_img, (4, 18))
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

# load graphics/images for the game
bg_img = pygame.image.load(os.path.join(img_dir, "bg-lg.png")).convert()
# add rect for bg - helps locate background
bg_rect = bg_img.get_rect()
# player's object
player_img = pygame.image.load(os.path.join(img_dir, "player.png")).convert()
# player's projectile
projectile_img = pygame.image.load(os.path.join(img_dir, "projectile.png")).convert()
# mob - e.g. asteroid
mob_imgs = []
mob_list = ["mob-tiny.png", "mob-small.png", "mob-med.png"]

for img in mob_list:
    mob_imgs.append(pygame.image.load(os.path.join(img_dir, img)).convert())

# load music and sound effects for use in game window
# laser beam firing sound effect
laser_effect = pygame.mixer.Sound(os.path.join(snd_dir, 'laser-beam-med.wav'))
# explosion sound effect
explosion_effect = pygame.mixer.Sound(os.path.join(snd_dir, 'explosion-med.wav'))
# load music for background playback in game window
pygame.mixer.music.load(os.path.join(snd_dir, 'space-music-bg.wav'))
# set music volume - reduce default volume
pygame.mixer.music.set_volume(0.7)

# sprite groups - game, mob...
game_sprites = pygame.sprite.Group()
mob_sprites = pygame.sprite.Group()
projectiles = pygame.sprite.Group()
# create player object
player = Player()
# add sprite to game's sprite group
game_sprites.add(player)
# loop through extra sprite objects
for i in range(10):
    mob = Mob()
    # add to game_sprites group to get object updated
    game_sprites.add(mob)
    # add to mob_sprites group - use for collision detection &c.
    mob_sprites.add(mob)

# initialise game score - default to 0
game_score = 0

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
        # calculate points relative to size of mob object
        game_score += 40 - collision.radius
				# play explosion sound effect for collision
        explosion_effect.play()
        mob = Mob()
        game_sprites.add(mob)
        mob_sprites.add(mob)

    # add check for collision - enemy and player sprites (False = hit object is not deleted from game window)
    collisions = pygame.sprite.spritecollide(player, mob_sprites, False, pygame.sprite.collide_circle)
    # check collisions for game window
    if collisions:
        looping = False

    # draw
    # draw background image - specify image file and rect to load image
    window.blit(bg_img, bg_rect)
    # draw all sprites to the game window
    game_sprites.draw(window)
    # draw text to game window - game score
    textRender(window, str(game_score), 18, winWidth / 2, 10)
    # update the display window...
    pygame.display.update()
