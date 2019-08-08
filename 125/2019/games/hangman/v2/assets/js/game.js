/**
* game.js - logic for game - hangman
*/

// define random words for game - initial fixed examples...
var gameWords = [
	"dragon",
	"wizard",
	"eagle",
  "hobbit",
	"earth",
	"planets",
	"geography"
];

// pick a random word for a new game
var gameWord = gameWords[Math.floor(Math.random() * gameWords.length)];

// set value for letters to guess from random word
var lettersToGuess = gameWord.length;

// check random word in console & letters left to guess
console.log('game word = ' + gameWord + ' & letters left = ' + lettersToGuess);

// define empty array for characters in random word
var answers = [];

// loop through answers array - add underscore for each letter in gameWord
for (var i = 0; i < gameWord.length; i++) {
	answers[i] = "_";
}

// output game progress to player
var lettersOutput = answers.join(" "); // create string from answers array
document.getElementById('wordStatus').innerHTML = 'guess word: ' + lettersOutput;

/*
* add event listeners for user interaction
*/

// select guess button in document
var guessBtn = document.getElementById('guessBtn');

// listen for user click on `guess` button
guessBtn.addEventListener('click', function() {
	// get letter value from input field
	var letter = document.getElementById('guess').value;
	// reset input field
	document.getElementById('guess').value = '';
	// reset focus on input field
  document.getElementById('guess').focus();
	// output guess letter
	console.log('letter = ' + letter);
	document.getElementById('guessLetter').innerHTML = 'guess letter: ' + letter;

	// check letter against game word & not in answers - check for duplicate letter guess
	if (gameWord.includes(letter) === true && answers.includes(letter) === false) {
		console.log('letter has been found...' + gameWord.includes(letter));
      // loop through gameWord
		  for (i = 0; i < gameWord.length; i++) {
				// check letter against each value in gameWord
		    if (gameWord[i] === letter) {
				  console.log('letter = index ' + i);
					// add letter to answers array at matching index position
				  answers[i] = letter;
					// decrement remaining letters to guess to win game...
					lettersToGuess--;
					console.log('letters left to find = ' + lettersToGuess);
				  // update game progress to player
          var lettersOutput = answers.join(" "); // create string from answers array
          document.getElementById('wordStatus').innerHTML = 'guess word: ' + lettersOutput;
			  }
		  }

			// check if gameWord has been guessed correctly
			if (lettersToGuess === 0) {
				console.log('game over...player won');
				document.getElementById('guessLetter').innerHTML = 'GAME OVER: word guessed correctly';
				// exit game and reset...need to add
			}

	} else {
		console.log('letter not found...');
		document.getElementById('guessLetter').innerHTML = 'letter not found - please try again...';
		// draw output to hangman...need to add
	}

}, false);
