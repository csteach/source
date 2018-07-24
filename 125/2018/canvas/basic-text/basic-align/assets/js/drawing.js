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
// define text alignment - centre of text will drawn at defined coordinates
context.textAlign = "center";
// draw text on canvas - string, x, y
context.fillText("Welcome to the wonderful world of canvas...", canvas.width/2, canvas.height/2);
