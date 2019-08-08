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
	// output guess letter
	console.log('letter = ' + letter);
	document.getElementById('guessLetter').innerHTML = 'guess letter: ' + letter;
	// check letter against  game word
	if (gameWord.includes(letter) === true) {
		console.log('letter has been found...');

		for (i = 0; i < gameWord.length; i++) {
			// check letter against gameSplit array
		  if (gameWord[i] === letter) {
				console.log('letter = index ' + i);
				// update letter in answers array
				answers[i] = letter;
				// update game progress to player
        var lettersOutput = answers.join(" "); // create string from answers array
        document.getElementById('wordStatus').innerHTML = 'guess word: ' + lettersOutput;
			}
		}

	} else {
		// output update to player - no letter found...
		console.log('letter not found...');
		document.getElementById('guessLetter').innerHTML = 'letter not found - please try again...';
	}

}, false);
