# HangMan Game

## Introduction

Welcome to Hangman, a classic word-guessing game where you try to uncover a hidden word letter by letter. 
This console-based Hangman game is a simple yet entertaining way to challenge your vocabulary.

## How to play:
1. Run the script in a Python environment.
2. Enter your name to start the game.
3. Guess letters to uncover the hidden word.
4. Be mindful of incorrect guesses, represented by the hangman's progression.
5. Win by guessing the entire word or lose if the hangman is fully drawn.


![Am I Responsive](images/Hangman%20responsive.png)

## Features

- **Interactive Gameplay:**     Guess letters to reveal the hidden word.
- **Random Word Selection:**    Each game features a randomly selected word from a predefined list.
- **Hangman ASCII Art:**        Enjoy visual representations of the hangman's progress based on incorrect guesses.
- **Player-Friendly:**          User prompts and feedback make the game easy to understand and play.
- **Play Again Option:**        Decide whether to start a new game or exit after completing a round.
- **Input Validation:**         Ensure that player inputs meet the game's requirements.

### Existing Features

Start Screen

- When the console is launched, the Hangman ASCII art appears along with the game rules. The player is prompted to choose between starting a new game or quitting to exit the game.

![Start Screen](images/StartScreen.png)

Input Name

- The game welcomes the player with a prompt to enter their name, adding a personalized touch to the gaming experience. This step ensures a unique and engaging connection with the player before diving into the challenges of Hangman. The input requires a minimum of two letters for validation. 

![Name Screen](images/Name_screen.png)

Letter Input

- In this interactive phase, the player is prompted to guess a letter for the Hangman game. The console awaits the player's input, creating an immersive experience as they strategically select a letter they believe is part of the hidden word. This step is crucial for progressing through the game and adds an element of suspense and strategy to the overall gameplay.

![Letter Input](images/Enter_First_Letter_Screen.png)

Correct Choice of Letter

- In this victorious moment, the player has successfully guessed a letter that is part of the secret word. The console responds with a positive acknowledgment, updating the display to reveal the correct placement of the guessed letter(s) within the word. This progress brings the player closer to unraveling the complete word and adds a sense of accomplishment to the gaming experience.

![Correct Guess](images/Correct_Guess.png)

Wrong Choice of Letter

- Uh-oh! The player has made an incorrect guess, and the consequences are unfolding. The console responds by updating the Hangman display, illustrating a part of the Hangman figure. Additionally, a list of incorrect guesses is presented, urging the player to strategize and make more accurate choices in subsequent attempts. The challenge intensifies, adding suspense to the game.

![Wrong Guess](images/Wrong_Guess.png)