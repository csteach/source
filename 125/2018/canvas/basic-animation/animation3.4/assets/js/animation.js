/**
 * animation.js - basic logic for animating a shape
 * add collision detection to shape's animation - pin ball
 */

/**
 * animation.js - basic logic for animating a shape
 * draw shape and randomly move
 */

// define canvas
var canvas = document.getElementById('drawing');
// define context for drawing
var context = canvas.getContext('2d');


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
 this.x = 100;
 this.y = 100;
 this.xSpeed = -2;
 this.ySpeed = 3;
};

// 1. update prototype - method to draw ball
Ball.prototype.draw = function () {
 circle(this.x, this.y, 10, true, 'green');
};

// 2. update prototype -method to move a ball
Ball.prototype.move = function () {
 this.x += this.xSpeed;
 this.y += this.ySpeed;
 console.log(`x = ` + this.x + ', y = ' + this.y);
};

// 3. update prototype - check a collision
Ball.prototype.checkCollision = function () {
if (this.x < 0 || this.x > 400) {
 this.xSpeed = -this.xSpeed;
 }
if (this.y < 0 || this.y > 400) {
 this.ySpeed = -this.ySpeed;
 }
};


/*
* drawing example - pin ball with collision...
*/

// instantiate a ball object using the Ball constructor
var ball = new Ball();

// run the timer for the animation...
setInterval(function () {
 context.clearRect(0, 0, 400, 400);
 ball.draw();
 ball.move();
 ball.checkCollision();
}, 30);