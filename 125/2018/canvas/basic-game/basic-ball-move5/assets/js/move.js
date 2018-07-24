/**
 * animation.js - basic logic for animating a shape
 * add keyboard control to move a shape around the canvas
 * check internal collision
 */

// define canvas
var canvas = document.getElementById('drawing');
// define context for drawing
var context = canvas.getContext('2d');
// define canvas width and height
var cHeight = canvas.height;
var cWidth = canvas.width;
// define game blocks
var blockDetails = [
  {
		x: 25,
		y: 25,
		width: 50,
    height: 10,
		color: 'blue'
	},
  {
		x: 150,
		y: 175,
		width: 50,
    height: 10,
		color: 'red'
	}
];

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

// draw block to canvas
function drawBlocks(blocks) {
	// iterate through blocks
  for (i = 0; i < blocks.length; i++) {
		context.fillStyle = blocks[i]['color'];
	  context.fillRect(blocks[i]['x'], blocks[i]['y'], blocks[i]['width'], blocks[i]['height']);
  }
}

/**
 * pin ball
 */

// ball constructor - name capitalised to denote constructor
function Ball() {
 this.x = cWidth/2;
 this.y = cHeight-10;
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

// 3. update prototype - check collision
Ball.prototype.checkCollision = function ( blocks ) {
  // iterate through blocks and check collision
	for (i = 0; i < blocks.length; i++) {
		// start start and end of block - x & y axis
		let blockStartX = blocks[i]['x'];
		let blockEndX = (blocks[i]['x'] + blocks[i]['width']);
		let blockStartY = blocks[i]['y'];
		let blockEndY = (blocks[i]['y'] + blocks[i]['height']);
		// check block collisions - allow for radius of ball
		if (this.x >= blockStartX-5 && this.x <= blockEndX+5 && this.y >= blockStartY-5 && this.y <= blockEndY+5) {
			console.log('collision at block = ' + this.x);
		}
  }
}

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
	// draw blocks to canvas
  drawBlocks(blockDetails);
  // update x and y speed
	this.xSpeed = xS;
  this.ySpeed = yS;
	// draw ball and move...
  ball.move();
	ball.draw();
  ball.checkCollision(blockDetails);
}

/**
 * game play and control 
 */

// add event listener for keypress - e.g. up arrow key...
window.addEventListener('keydown', function (event) {
	// get code for key presses
  var key = event.keyCode;
  console.log("key pressed = " + key);
  ball.userControl(key);
})

// instantiate a ball object using the Ball constructor
var ball = new Ball();