/**
 * drawing.js - basic logic for drawing onto the canvas element
 * draw text on canvas - fill text with colour
 */

// define canvas
var canvas = document.getElementById('drawing');
// define context for drawing
var context = canvas.getContext('2d');

/*
* drawing examples
*/

// define font for text
context.font = "25px Sans Serif";
// define fill colour
context.fillStyle = "green";
// draw text on canvas - string, x, y
context.fillText("Welcome to the wonderful world of canvas...", 50, 50);
