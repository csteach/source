/**
 * animation.js - basic logic for animating a shape
 * draw shape and animate size
 */

// define canvas
var canvas = document.getElementById('drawing');
// define context for drawing
var context = canvas.getContext('2d');

/*
* drawing example - basic rect with animation
*/

// initial size for shape
var size = 0;

setInterval(function() {
  // clear rect - matches size of canvas
  //context.clearRect(0, 0, 400, 400);
  // define rect for shape
  context.fillRect(0, 0, size, size);

  // increment position value
  size++;
  // check position to stop shape leaving canvas
  if (size > 400) {
    size = 0; 
		context.clearRect(0, 0, 400, 400);
  }
}, 15);

