/**
 * drawing.js - basic logic for drawing onto the canvas element
 * draw bézier curves - cubic
 * MDN - https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Drawing_shapes
 */

// define canvas
var canvas = document.getElementById('drawing');
// define context for drawing
var context = canvas.getContext('2d');

/*
* drawing example - bézier curves - cubic
*/

// define fill style
context.fillStyle = 'SteelBlue';

// draw a cubic bézier curve
context.beginPath();
context.moveTo(75, 40);
context.bezierCurveTo(75, 37, 70, 25, 50, 25);
context.bezierCurveTo(20, 25, 20, 62.5, 20, 62.5);
context.bezierCurveTo(20, 80, 40, 102, 75, 120);
//context.bezierCurveTo(110, 102, 130, 80, 130, 62.5);
//context.bezierCurveTo(130, 62.5, 130, 25, 100, 25);
//context.bezierCurveTo(85, 25, 75, 37, 75, 40);
context.fill();

