/*
* travel notes JS
* - plain JS example usage...
*/

function travelNotes() {
  "use strict";

  // get a reference to `.note_output` in the DOM
  let noteOutput = document.querySelector('.note-output');
  // add note button
  let addNoteBtn = document.getElementById('add-note');
  // input field for add note
  let inputNote = document.getElementById('input-note');

  // add event listener to add note button
  addNoteBtn.addEventListener('click', () => {
      createNote(inputNote, noteOutput);
  });

  // add event listener for keypress in note input field
  inputNote.addEventListener('keypress', (e) => {
    // check key pressed by code - 13 - return
    if (e.keyCode === 13) {
      createNote(inputNote, noteOutput);
    }
  });

}

// create a note
// - input = value from input field
// - output = DOM node for output of new note
function createNote(input, output) {
    // create p node
    let p = document.createElement('p');
    // get value from input field for note
    let inputVal = input.value;
    // check input value
    if (inputVal !== '') {
      // create text node
      let noteText = document.createTextNode(inputVal);
      // append text to paragraph
      p.appendChild(noteText);
      // append new paragraph and text to existing note output
      output.appendChild(p);
      // call custom animation for fade in...
      fadeIn(p);
      // clear input text field
      input.value = '';
    }
}

// custom fade-in animation...
function fadeIn(node) {
  node.style.opacity = 0;

  let last = +new Date();
  let tick = () => {
    node.style.opacity = +node.style.opacity + (new Date() - last) / 2000;
    last = +new Date();

    if (+node.style.opacity < 1) {
      (window.requestAnimationFrame && requestAnimationFrame(tick)) || setTimeout(tick, 16);
    }
  };

  tick();
}

// load app
travelNotes();
