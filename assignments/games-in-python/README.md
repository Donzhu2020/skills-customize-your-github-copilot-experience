
# 🎮 Assignment: Games in Python

## 🎯 Objective

Build the classic Hangman word-guessing game to practice Python strings, loops, conditionals, and random selection while creating an interactive game experience.

## 📝 Tasks

### 🛠️ Hangman Game Implementation

#### Description
Create a Hangman game where players guess letters to reveal a hidden word before running out of attempts.

#### Requirements
Completed program should:

- Randomly select words from a predefined list
- Accept letter guesses and show current progress in underscore format (e.g., `_ _ _`)
- Track the number of incorrect guesses remaining
- Display the player's guessed letters
- End the game when the word is guessed or attempts are exhausted
- Display win/lose messages with the final word revealed
- Allow players to play multiple rounds without restarting the program

#### Example Output
```
Welcome to Hangman!
Word: _ _ _ _ _
Incorrect guesses remaining: 6
Guessed letters: 

Guess a letter: e
Word: _ _ _ e _
Incorrect guesses remaining: 6
Guessed letters: e

Guess a letter: x
Incorrect guess!
Word: _ _ _ e _
Incorrect guesses remaining: 5
Guessed letters: e, x
```
