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

// define function to draw mouse - x & y = centre of head, radius = head size, color1 = head colour
function mouse(x, y, radius, fill, color1, color2) {
  //draw left ear 
  circle(Math.floor(x/1.28), Math.floor(y/1.3), Math.floor(radius/1.8), fill, color2);
	//draw right ear
	circle(Math.floor(x*1.22), Math.floor(y/1.3), Math.floor(radius/1.8), fill, color2);
	//draw head
  circle(x, y, radius, fill, color1);
}

//draw required mouse shapes

// 1. base small size for mouse
mouse(150, 130, 34, true, 'DarkRed', `black`);
// 2. scale by 2 - x, y & radius
mouse(300, 260, 68, true, 'DarkBlue', `green`);
// animate our well known mouse
