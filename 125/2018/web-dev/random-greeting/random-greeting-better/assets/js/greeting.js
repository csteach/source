/**
* greeting.js - logic for random greeting generator
* using abstraction...
*/

// FN: greetings generator
function generateGreeting(name) {
	// define random greetings - initial fixed examples...
	let greetings = [
		`Hello ${name}, how are you?`,
		`Bonjour ${name}, ça va? `,
		`Guten tag ${name}, wie geht es ihnen?`,
		`Χαίρετε ${name}, Πώς είσαι;`,
		`Salve ${name}, quid agis?`,
		`Ciao ${name}, come va?`,
		`こんにちは ${name}, お元気ですか?`
	];
	// pick a random greeting message
  let greeting = greetings[Math.floor(Math.random() * greetings.length)];
	// return greeting message
	return greeting;
}

/*
* add event listeners for user interaction
*/

// SELECT: guess button in document
var greetingBtn = document.getElementById('greetingBtn');

// LISTEN: for user click on `greeting` button
greetingBtn.addEventListener('click', function() {
  // get name value from input field
	let name = document.getElementById('name').value;
	// output name
	console.log('name = ' + name);
	// get greeting message - pass input name...
	let greetingMessage = generateGreeting(name);
	
  // reset input field
	document.getElementById('name').value = '';
	// reset focus on input field
  document.getElementById('name').focus();
	// output greeting message to user
	document.getElementById('greeting').innerHTML = 'random greeting: ' + greetingMessage;

}, false);