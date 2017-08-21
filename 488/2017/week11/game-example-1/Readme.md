### Pygame - Game Notes - Game 1 - Shoot Em Up

A few notes on building a simple 'Shoot Em Up' type game with Pygame.

#### Contents
* Intro
* Different types
* Game versions
  * sprites/animating
  * drawing/text
  * music/basic
  * player/health - part 1
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

##### Sprites/Animating
  * v0.7 - shooter0.7.py
    * set random image for mob sprite object image
      * random image from selection of image options
      * rotate and animate each random mob sprite image

##### Drawing/Text
  * v0.8 - shooter0.8.py
    * draw text to the game window & keep a game score
    * keep a running score for collisions with a projectile
        * player shoots and destroys an asteroid
        * score is calculated relative to size of mob object - radius...
    * score is rendered to top of game window
        * update for each successful hit

##### Music/Basic
  * v0.9 - shooter0.9.py
    * add music and sound effects to the game window
      * add pygame mixer
      * load sounds directory in assets
      * load required sounds and sound effects
      * call `play()` for each required sound effect and game music...

##### Player/Health - part 1
  * v1.0 - shooter1.0.py
    * check player's health
        * set default health to 100%
        * decrement health per collision
          * quit game when health reaches 0
        * draw status bar to game window
          * green colour for good health
          * change to red colour below 40%

#### References
* [Shoot Em Up](https://en.wikipedia.org/wiki/Shoot_'em_up)
