/**
 * drawing.js - basic logic for drawing onto the canvas element
 * draw combined shapes - Egyptian Ankh
 * Wikipedia - https://en.wikipedia.org/wiki/Ankh
 */

// define canvas
var canvas = document.getElementById('drawing');
// define context for drawing
var context = canvas.getContext('2d');

/*
* drawing example - combined shapes - Ankh
* context.quadraticCurveTo(cp1x, cp1y, x, y);
*/

// define stroke style and width
context.strokeStyle = 'SteelBlue';
context.lineWidth = 10;

// draw an egyptian ankh
context.beginPath();
// define start point for drawing
context.moveTo(150, 100);
// PART 1 - top of ankh symbol
context.quadraticCurveTo(200, 50, 250, 100);
// right side of ankh symbol
context.quadraticCurveTo(300, 150, 200, 250);
// left side of ankh symbol
context.quadraticCurveTo(100, 150, 150, 100);

// PART 2 - horizontal bar in centre of ankh
// define start point for horizontal bar
context.moveTo(200, 260);
// draw left top line
context.lineTo(70, 255);
// draw left vertical line
context.lineTo(70, 285);
// draw left bottom line
context.lineTo(200, 280);
// draw right bottom line
context.lineTo(330, 285);
// draw right vertical line
context.lineTo(330, 255);
// draw right top line
context.lineTo(200, 260);

// PART 3 - vertical stem from horizontal bar down
// define start point for vertical stem
context.moveTo(210, 280)
// draw right side down - slight angle out
context.lineTo(215, 500);
// draw bottom of stem
context.lineTo(185, 500);
// draw left side up = slight angle in
context.lineTo(190, 280);

context.stroke();