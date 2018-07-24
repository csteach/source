/**
 * animation.js - basic logic for animating a shape
 * draw shape and randomly move
 */

/**
 * animation.js - basic logic for animating a shape
 * draw shape and randomly move
 */

// define canvas
var canvas = document.getElementById('drawing');
// define context for drawing
var context = canvas.getContext('2d');

var x = 150;
var y = 130;

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

/*
* drawing example - move shape around the canvas
*/

// update the x and y coordinates for shape animation
function update(coord) {
	var offset = Math.random()*5-2;
	coord += offset;

	if (coord > 400) {
		coord = 0;
	}
	if (coord < 0) {
		coord = 0;
	}

	return coord;
}

// animate our well known mouse
setInterval(function() {
	context.clearRect(0, 0, 800, 800);

  // 1. base small size for mouse
  circle(x, y, 40, true, 'green');
	x = update(x);
	y = update(y);
	
}, 20);