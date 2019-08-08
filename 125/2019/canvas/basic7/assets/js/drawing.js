/**
 * drawing.js - basic logic for drawing onto the canvas element
 * draw a shape and fill path
 */

// define canvas
var canvas = document.getElementById('drawing');
// define context for drawing
var context = canvas.getContext('2d');

/*
* drawing example - shape with fill path
*/

// define fill style
context.fillStyle = 'DarkSeaGreen';

// start recording lines to draw...
context.beginPath();
// move to starting position for line - x & y
context.moveTo(50, 50);
// define line - x & y
context.lineTo(75, 25);
context.lineTo(100, 50);
context.lineTo(125, 75);
context.lineTo(100, 100);
context.lineTo(75, 125);
context.lineTo(50, 100);
context.lineTo(25, 75);
// draw all lines and fill
context.fill();


