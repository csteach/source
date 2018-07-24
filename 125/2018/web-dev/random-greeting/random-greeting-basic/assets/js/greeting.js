/**
* greeting.js - logic for random greeting generator
*/

// define random greetings - initial fixed examples...
var greetings = [
	"Hello ",
	"Bonjour ",
	"Guten Tag ",
  "Χαίρετε ",
	"Salve ",
	"Ciao ",
	"こんにちは "
];

/*
* add event listeners for user interaction
*/

// select guess button in document
var greetingBtn = document.getElementById('greetingBtn');

// listen for user click on `greeting` button
greetingBtn.addEventListener('click', function() {
	// pick a random greeting message
  var greeting = greetings[Math.floor(Math.random() * greetings.length)];
	// check random greeting in console
  console.log('random greeting = ' + greeting);
	// get name value from input field
	var name = document.getElementById('name').value;
	// output name
	console.log('name = ' + name);
	// create greeting message
	var greetingMessage = greeting + name;
	// reset input field
	document.getElementById('name').value = '';
	// reset focus on input field
  document.getElementById('name').focus();
	// output greeting message to user
	document.getElementById('greeting').innerHTML = 'random greeting: ' + greetingMessage;

}, false);
