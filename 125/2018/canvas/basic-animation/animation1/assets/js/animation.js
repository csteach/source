/**
 * animation.js - basic logic for animating a shape
 * draw shape and animate
 */

// define canvas
var canvas = document.getElementById('drawing');
// define context for drawing
var context = canvas.getContext('2d');

/*
* drawing example - basic rect with animation
*/

// initial start position X for shape
var pos = 0;

setInterval(function() {
  // clear rect - matches size of canvas
  context.clearRect(0, 0, 800, 800);
  // define rect for shape
  context.fillRect(pos, 0, 40, 40);

  // increment position value
  pos++;
  // check position to stop shape leaving canvas
  if (pos > 400) {
    pos = 0; 
  }
}, 15);

