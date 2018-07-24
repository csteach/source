/**
 * drawing.js - basic logic for drawing onto the canvas element
 * change the colour
 * colour reference - https://css-tricks.com/snippets/css/named-colors-and-hex-equivalents/
 */

// define canvas
var canvas = document.getElementById('drawing');
// define context for drawing
var context = canvas.getContext('2d');

// define colours
var colours = ["YellowGreen", "DarkSeaGreen", "MediumSeaGreen", "LightSeaGreen", "Turquoise"];

/*
* drawing examples
*/

// 4. draw with a different colour
context.fillStyle = colours[0];
context.fillRect(0,0,200, 50);

// 5. draw many shapes with different colours
for (i = 1; i < 6; i++) {
  var width = 30;
	var height = i * 25;
	var x = 30 * i;
	var y = 75;
	context.fillStyle = colours[i-1];
	context.fillRect(x, y, width, height);
}
