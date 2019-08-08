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

/*
* drawing example - move shape around the canvas
*/

// 1. a well-known mouse with variant colours
// left ear
circle(117, 100, 18, true, 'black');
// right ear
circle(183, 100, 18, true, 'black');
// head
circle(150, 130, 33, true, 'DarkRed');

