/**
 * drawing.js - basic logic for drawing onto the canvas element
 * draw text on canvas - stroke style
 */

// define canvas
var canvas = document.getElementById('drawing');
// define context for drawing
var context = canvas.getContext('2d');

/*
* drawing examples
*/

// define font for text
context.font = "30px Comic Sans MS";

// draw text on canvas with stroke - string, x, y
context.strokeText("Welcome to the wonderful world of canvas...", 10, 50);
