/**
 * drawing.js - basic logic for drawing onto the canvas element
 * draw bézier curves - quadratic
 * MDN - https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Drawing_shapes
 */

// define canvas
var canvas = document.getElementById('drawing');
// define context for drawing
var context = canvas.getContext('2d');

/*
* drawing example - bézier curves - quadratic
*/

// define fill style
context.fillStyle = 'SteelBlue';

// draw a quadratic bézier curve
context.beginPath();
context.moveTo(75, 25);
context.quadraticCurveTo(25, 25, 25, 62.5);
context.quadraticCurveTo(25, 100, 50, 100);
context.quadraticCurveTo(50, 120, 30, 125);
context.quadraticCurveTo(60, 120, 65, 100);
context.quadraticCurveTo(125, 100, 125, 62.5);
context.quadraticCurveTo(125, 25, 75, 25);
context.fill();

