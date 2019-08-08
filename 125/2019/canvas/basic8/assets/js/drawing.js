/**
 * drawing.js - basic logic for drawing onto the canvas element
 * draw arcs and circles
 */

// define canvas
var canvas = document.getElementById('drawing');
// define context for drawing
var context = canvas.getContext('2d');

/*
* drawing example - shape with fill path
*/

// define stroke style and width
context.strokeStyle = 'SteelBlue';
context.lineWidth = 3;

// draw a full circle
context.beginPath();
context.arc(50, 100, 25, 0, Math.PI * 2, false);
context.stroke();

// draw a semi-circle
context.beginPath();
context.arc(125, 100, 25, 0, Math.PI, false);
context.stroke();

// draw a quarter circle
context.beginPath();
context.arc(175, 100, 25, 0, Math.PI / 2, false);
context.stroke();
