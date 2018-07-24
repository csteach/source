/**
 * drawing.js - basic logic for drawing onto the canvas element
 * draw lines to create shapes
 */

// define canvas
var canvas = document.getElementById('drawing');
// define context for drawing
var context = canvas.getContext('2d');

/*
* drawing examples
*/

// 8. draw lines with paths
context.strokeStyle = 'LightSeaGreen';
context.lineWidth = 3;
// start recording lines to draw...
context.beginPath();
// move to starting position for line - x & y
context.moveTo(50, 10);
// define line - x & y
context.lineTo(100, 70);
// draw all linkes
context.stroke();

// 9. draw a pyramid
context.strokeStyle = 'GoldenRod';
context.lineWidth = 3;
// start recording lines to draw...
context.beginPath();
// move to starting position for line - x & y
context.moveTo(100, 100);
// define line - x & y
context.lineTo(50, 170);
// define line - x & y
context.lineTo(150, 170);
// define line - x & y
context.lineTo(100, 100);
// draw all linkes
context.stroke();