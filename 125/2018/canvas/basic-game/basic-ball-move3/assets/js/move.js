/**
 * animation.js - basic logic for animating a shape
 * add keyboard control to move a shape around the canvas
 */

// define canvas
var canvas = document.getElementById('drawing');
// define context for drawing
var context = canvas.getContext('2d');
// define canvas width and height
var cHeight = canvas.height;
var cWidth = canvas.width;

// define circle function
function circle(x, y, radius, fillCircle, color) {
	// start recording
  context.beginPath();
	// define arc - x, y, radius, start posn, end posn, anticlockwise...
	context.arc(x, y, radius, 0, Math.PI * 2, false);
	// check fill or stroke
	if (fillCircle) {
		// colour for fill
	  context.fillStyle = color;
		context.fill();
	} else {
		// set line width & line colour
		context.lineWidth = 2;
    context.strokeStyle = color;
		context.stroke();
	}
}


/**
 * pin ball
 */

// ball constructor - name capitalised to denote constructor
function Ball() {
 this.x = cWidth/2;
 this.y = cHeight-10;
 /*this.xSpeed = -2;
 this.ySpeed = 3;*/
};

// 1. update prototype - method to draw ball
Ball.prototype.draw = function () {
 circle(this.x, this.y, 10, true, 'green');
};

// 2. update prototype -method to move a ball
Ball.prototype.move = function () {
// update position of ball based on speed
 this.x += this.xSpeed;
 this.y += this.ySpeed;
// check ball relative to boundaries - canvas edge
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
Ball.prototype.userControl = function( key ) {
  /*
	* 37 = LEFT
	* 38 = UP
	* 39 = RIGHT
	* 40 = DOWN
	*/
  if (key === 37) {
		ball.userMove(-15, 0);
  } else if (key === 38) {
		ball.userMove(0, -15);
	} else if (key === 39) {
		ball.userMove(15, 0);
	} else if (key === 40) {
		ball.userMove(0, 15);
	}
};

// 5. update prototype - user movement of ball
Ball.prototype.userMove = function (xS, yS) {
	// clear canvas for animation
	context.clearRect(0, 0, cWidth, cHeight);
  // update x and y speed
	this.xSpeed = xS;
  this.ySpeed = yS;
	// draw ball and move...
  ball.move();
	ball.draw();
}

// add event listener for keypress - e.g. up arrow key...
window.addEventListener('keydown', function (event) {
	// get code for key presses
  var key = event.keyCode;
  console.log("key pressed = " + key);
  ball.userControl(key);
})

// instantiate a ball object using the Ball constructor
var ball = new Ball();
