# Py-Proj3-Hangman-Game
# Hangman Game

This is a simple implementation of the classic word-guessing game "Hangman" written in Python. The game provides a fun way to guess a secret word by suggesting letters one at a time while adhering to a limited number of lives

## Features
- **Error Handling**: Input validation ensures smooth gameplay. 
- **Improved User Experience**: ASCII visuals and messages make the game enjoyable.
- **Basic Programming Concepts**: Utilizes Python concepts like lists, loops, and conditional statements.

## How to Play

1. The program selects a secret word randomly.
2. **Guess the Word**: Input one letter per turn to guess the secret word.
3. **Feedback**: 
   - Correct guesses reveal the letter's position in the word blanks.
   - Incorrect guesses reduce lives and add to the hangman drawing.
4. **Win or Lose**:
   - **Win**: Successfully guess the entire word before lives run out.
   - **Lose**: Use up all lives and see the hangman fully drawn.

## Key Python Concepts Used

1. **Lists**: 
   - To store the secret words as a list of characters.
   - To track correctly guessed letters and display progress.

2. **Conditional Statements (`if`, `elif`, `else`)**:
   - To evaluate user input and determine game logic.

3. **Loops**:
   - For repeated guessing until the game ends.

4. **Error Handling**:
   - Ensures user input is valid (e.g., a single alphabetical character).
5. **ASCII Art**:
   - Visual representation of the hangman for added engagement.

## Installation and Execution

1. Clone or download this repository.
2. Make sure Python (version 3.6 or later) is installed on your system.
