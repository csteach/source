### Readme - Pygame - Sprites - Basic

A few examples of basic sprites with Pygame.

#### Contents
* basicsprites1.py
    * create a sprite object, add to sprite group, and update and render sprites to game window...
* basicsprites2.py
    * import assets directory from local filesystem
        * set relative directories for assets, images...
    * set image for sprite
    * animate with bouncing on y-axis, and across the screen on the x-axis...
        * loop from side to side on x-axis
* basicsprites3.py
    * add sprite to game window
    * control sprite with keyboard controls on x-axis
    * add bounding check and constraint to x-axis
* basicsprites4.py
    * add more sprite objects to the game window
    * sprites move down the screen along a randomised path for the x-axis and y-axis
    * speed of each sprite is also randomised
    * sprites will reappear in a randomised position at the top of the screen
        * x-axis and y-axis detection is in place...
* basicsprites5.py
    * release a sprite object from another sprite object
    * listen for a keypress, e.g. the spacebar
    * release new sprite object for each keypress...spacebar &c.
    * new sprite released relative to player object...
* basicsprites6.py
    * add collision detection
        * collision - mob hits player & ends game
        * collision - player hits mob and kills mob
    * update `while` loop boolean to check for state of game
        * looping or not
