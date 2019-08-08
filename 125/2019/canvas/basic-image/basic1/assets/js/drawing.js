/**
 * drawing.js - basic logic for drawing onto the canvas element
 * add a static image
 */

// define canvas
var canvas = document.getElementById('drawing');
// define context for drawing
var context = canvas.getContext('2d');

/*
* drawing examples - draw a static image
*/

// 1. define optional image size
var img = new Image();

// image source file
img.src = './assets/images/philae1.jpg';

img.onload = function() {
	// context.drawImage(image, dx, dy)
  context.drawImage(img, 0, 0);
}