### Pygame - Game Notes - Game 1 - Shoot Em Up

A few notes on building a simple 'Shoot Em Up' type game with Pygame.

#### Contents
* Intro
* Different types
* Game versions
  * Game/Extras
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

##### Game/Extras
  * v1.1
    * add repetitive firing sequence for player's laser beam
      * move keypress check for space bar to player class
      * fire laser beam whilst space pressed down
      * set interval in ms for firing sequence
      * check time between now and last firing
  * v1.2
    * add some fun explosions
      * create sprite object for explosion
      * cycle through images to create explosion animation
      * add explosion for each collision
    * extra explosions
      * explode a player's ship for a collision
    * scale explosions
      * rescale and size explosions in game window

#### References
* [Shoot Em Up](https://en.wikipedia.org/wiki/Shoot_'em_up)
