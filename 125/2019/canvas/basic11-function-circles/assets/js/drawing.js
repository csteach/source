/**
 * drawing.js - basic logic for drawing onto the canvas element
 * draw circles with a custom function
 */

// define canvas
var canvas = document.getElementById('drawing');
// define context for drawing
var context = canvas.getContext('2d');

/*
* drawing example - custom function to draw circles
*/

// define custom function to draw circle
function circle(x, y, radius, fillCircle) {
	// start recording
  context.beginPath();
	// define arc - x, y, radius, start posn, end posn, anticlockwise...
	context.arc(x, y, radius, 0, Math.PI * 2, false);
	// check fill or stroke
	if (fillCircle) {
		context.fill();
	} else {
		context.stroke();
	}
}

// draw a series of circles
//context.lineWidth = 2;
//context.strokeStyle = 'DarkRed';
context.fillStyle = 'DarkRed';

// !. smiley face
// left eye
circle(100, 110, 20, false);
// right eye
circle(200, 110, 20, false);
// outer circle for head
circle(150, 150, 100, false);

// arc for mouth
context.beginPath();
context.arc(150, 170, 60, Math.PI, 0, true);;
context.stroke();

// 2. a certain well-known mouse
// left ear
circle(400, 100, 35, true);
// right ear
circle(500, 100, 35, true);
// head
circle(450, 160, 57, true);