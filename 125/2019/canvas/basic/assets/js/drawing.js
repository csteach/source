/**
 * drawing.js - basic logic for drawing onto the canvas element
 * rectangle & staircase
 */

// define canvas
var canvas = document.getElementById('drawing');
// define context for drawing
var context = canvas.getContext('2d');

/*
* drawing examples
*/

// 1. rectangle
//context.fillRect(0, 0, 50, 25);

// 2. pattern with rectangles - staircase
for (i = 1; i < 7; i++) {
	var x = 100;
	context.fillRect(i / x, i * 20, i * 20, 20);
}

// 3. pattern with rectangles - stepped pyramid
