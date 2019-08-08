/**
 * drawing.js - basic logic for drawing onto the canvas element
 * stepped pyramid
 */

// define canvas
var canvas = document.getElementById('drawing');
// define context for drawing
var context = canvas.getContext('2d');

/*
* drawing examples
*/

// 3. pattern with rectangles - stepped pyramid - x,y,width,height
for (i = 1; i < 7; i++) {
	var start = 100;
  var width = i * 30;
  var x = (start - (width / 2))
	context.fillRect(x, i * 20, width, 20);
}
