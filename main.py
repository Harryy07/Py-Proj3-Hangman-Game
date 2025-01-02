import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

lives = 6 #initialising number of lives left.
#creating the same number of blanks as chosen word.
placeholder = "_"
for blank in chosen_word:
    print(placeholder, end='' )

correct_guess = []
game_over = False
while not game_over:
    guess = input("\nGuess a letter: ").lower() #The reason for storing the user input in lower case is just because the user might put input in all upper case or just the first letter.
    display = ""

#checking if the user guessed the right letter or not and if guessed correctly replace the blank with guessed word and rest leave it as same.
    for letter in chosen_word:
        if guess == letter:
            display += letter
            correct_guess.append(guess) #appending the correct guess into the list
        elif letter in correct_guess:
            display += letter #keeping the previous correct guess
        else:
            display += "_"


    if not "_" in display:
        game_over = True
        print("You won! ")
    if not guess in chosen_word:
            lives -= 1
    if lives == 0:
        game_over = True
        print("You Lose, Game Over!")

    print(display)
    print(f"Number of lives left: {lives}")
    print(stages[lives])