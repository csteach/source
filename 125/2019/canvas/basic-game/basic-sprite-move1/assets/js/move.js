/**
 * animation.js - basic logic for animating a shape
 * add keyboard control to move a shape around the canvas
 * animate sprite
 */

// define canvas
var canvas = document.getElementById('drawing');
// define context for drawing
var context = canvas.getContext('2d');
// define canvas width and height
var cHeight = canvas.height;
var cWidth = canvas.width;

// define sprite draw function
function drawSprite(dx, dy) {
	// 1. define optional image size
  var img = new Image();

  // image source file
  img.src = './assets/images/player.png';

  img.onload = function() {
	  // context.drawImage(image, dx, dy, dw, dh)
    context.drawImage(img, dx-30, dy-40, 60, 40);
  }
}


/**
 * image sprite
 */

//  constructor - name capitalised to denote constructor
function Sprite() {
 this.x = cWidth/2;
 this.y = cHeight;
};

// 1. update prototype - method to draw sprite
Sprite.prototype.draw = function () {
  // draw image as sprite - specify start x and y coordinates
  drawSprite(this.x, this.y);
};

// 2. update prototype -method to move a sprite
Sprite.prototype.move = function () {
// update position of sprite based on speed
 this.x += this.xSpeed;
 this.y += this.ySpeed;
// check sprite relative to boundaries - canvas edge
  if (this.x < 0) {
	  this.x = cWidth;
  } else if (this.x > cWidth) {
	  this.x = 0;
  } else if (this.y < 0) {
	  this.y = cHeight;
  } else if (this.y > cHeight) {
    this.y = 0;
  }

 console.log(`x = ` + this.x + ', y = ' + this.y);
};

// 4. update prototype - user control
Sprite.prototype.userControl = function( key ) {
  /*
	* 37 = LEFT
	* 38 = UP
	* 39 = RIGHT
	* 40 = DOWN
	*/
  if (key === 37) {
		sprite.userMove(-15, 0);
  } else if (key === 38) {
		sprite.userMove(0, -15);
	} else if (key === 39) {
		sprite.userMove(15, 0);
	} else if (key === 40) {
		sprite.userMove(0, 15);
	}
};

// 5. update prototype - user movement of sprite
Sprite.prototype.userMove = function (xS, yS) {
	// clear canvas for animation
	context.clearRect(0, 0, cWidth, cHeight);
  // update x and y speed
	this.xSpeed = xS;
  this.ySpeed = yS;
	// draw sprite and move...
	sprite.move();
	sprite.draw();
}

/**
 * game play and control 
 */

// add event listener for keypress - e.g. up arrow key...
window.addEventListener('keydown', function (event) {
	// get code for key presses
  var key = event.keyCode;
  console.log("key pressed = " + key);
  sprite.userControl(key);
})

// instantiate a ball object using the Ball constructor
var sprite = new Sprite();
