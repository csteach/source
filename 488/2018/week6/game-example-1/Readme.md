### Pygame - Game Notes - Game 1 - Shoot Em Up

A few notes on building a simple 'Shoot Em Up' type game with Pygame.

#### Contents
* Intro
* Different types
* Game versions
  * Sprites/Collisions
  * Sprites/Animating
* References

#### Intro
A **Shoot Em Up**, or **STG** in Japan, style game simply allows a player to fire bullets and other weapons at an enemy, whilst trying to avoid their attack.

The classic example, of course, is **Space Invaders**, which largely popularised this genre of game.

However, there are many different examples of this style of game.

#### Different types
Whilst the general gameplay is the same for each type of STG, there are a few notable variants. For example, we may consider viewpoint and movement as an easy way of differentiating various different examples. These may include,

  * fixed shooters
  * rail shooters
  * scrolling shooters
  * ...

#### Game versions
The following versions are available:

##### Sprites/Collisions
  * v0.5 - shooter0.5.py
    * better collisions and detection
        * change bounding box for player and mob sprite objects
        * change bounding box to circle, and modify radius to fit sprite objects

##### Sprites/Animating
  * v0.6 - shooter0.6.py
    * animating sprite images
      * rotate mob images down the screen
      * create pristine image for rotation
      * update rect bounding box to ensure it rotates correctly
  * v0.7 - shooter0.7.py
    * set random image for mob sprite object image
      * random image from selection of image options
      * rotate and animate each random mob sprite image

#### References
* [Shoot Em Up](https://en.wikipedia.org/wiki/Shoot_'em_up)
