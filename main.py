import random
import hangman_art
import hangman_words

word_list = hangman_words.word_list
stages = hangman_art.stages
logo = hangman_art.logo
print(logo)
chosen_word = random.choice(word_list)

lives = 6 #initialising number of lives left.
#creating the same number of blanks as chosen word.
placeholder = ""
word_length = len(chosen_word)
for blank in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

correct_guess = []
game_over = False
while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()                   #The reason for storing the user input in lower case is just because the user might put input in all upper case or just the first letter.
    display = ""
    if guess in correct_guess:                                   #If the user has entered a letter they've already guessed, print the letter and let them know.
        print(f"You've already guessed {guess}")
#checking if the user guessed the right letter or not and if guessed correctly replace the blank with guessed word and rest leave it as same.
    for letter in chosen_word:
        if guess == letter:
            display += letter
            correct_guess.append(guess)                           #appending the correct guess into the list
        elif letter in correct_guess:
            display += letter                                     #keeping the previous correct guess
        else:
            display += "_"
    print("Word to guess: " + display)

    if not guess in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life. ")
        lives -= 1
    if lives == 0:
        game_over = True
        print(f"***********************YOU LOSE!!**********************")
        print(f"The correct word was: {chosen_word}!")

    if not "_" in display:
        game_over = True
        print("***************************YOU WIN****************************")

    print(stages[lives])