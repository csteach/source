/**
 * drawing.js - basic logic for drawing onto the canvas element
 * draw a stick man
 */

// define canvas
var canvas = document.getElementById('drawing');
// define context for drawing
var context = canvas.getContext('2d');

/*
* drawing example - stick man
*/

// define stroke style &c.
context.strokeStyle = 'LightSeaGreen';
context.lineWidth = 3;

// HEAD - draw rectangle outline with stroke/line - no fill
context.strokeRect(80, 5, 40, 40);

// TORSO: draw lines with paths
// start recording lines to draw...
context.beginPath();
// move to starting position for line - x & y
context.moveTo(100, 45);
// define line - x & y
context.lineTo(100, 125);

// LEFT ARM:  
context.moveTo(100, 75);
context.lineTo(65, 65);

// RIGHT ARM:  
context.moveTo(100, 75);
context.lineTo(135, 65);

// LEFT LEG:  
context.moveTo(100, 125);
context.lineTo(75, 185);

// RIGHT LEG:  
context.moveTo(100, 125);
context.lineTo(125, 185);

// draw all lines
context.stroke();


