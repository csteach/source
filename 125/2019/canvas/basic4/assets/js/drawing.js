/**
 * drawing.js - basic logic for drawing onto the canvas element
 * stroke/line rectangle examples
 */

// define canvas
var canvas = document.getElementById('drawing');
// define context for drawing
var context = canvas.getContext('2d');

/*
* drawing examples
*/

// 6. draw rectangle outline with stroke/line - no fill
context.strokeRect(5, 5, 150, 50);

// 7. draw rectangle outline with colour
context.strokeStyle = "DarkSeaGreen";
context.lineWidth = 3;
context.strokeRect(5, 75, 300, 50);