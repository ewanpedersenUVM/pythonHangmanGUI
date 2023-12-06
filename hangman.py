"""
Shamus Murphy
Final Project
"""

import random

def hangman(word):

  guess_letters = []
  incorrect_guesses = 0

  # Start the game loop.
  while incorrect_guesses < 6:

    # Display the game state.
    print(f"Number of letters: {len(word)}")
    print("Incorrect guesses: ", incorrect_guesses)

    # User's guess.
    guess = input("Guess a letter: ")
    
    # Check if the guess is correct.
    if guess in guess_letters :
       print("Letter already guessed please try again")
    else:
        try:
            index = word.index(guess)
            print(f"{guess} is located at the number {index + 1} spot in the word.")
            guess_letters.append(guess)
            print(f"Correct Letters: {guess_letters}")
        except ValueError:
            print(f"{guess} is not in the word.")
            incorrect_guesses += 1
    final_guess = input("Would you like to guess the word (yes/no)? ")
    final_guess = final_guess.upper()
    if (final_guess == "YES"):
      final = input("What is the word?")
      if final == word:
        print(f"You Win! and you had only {incorrect_guesses} incorrect guesses!")
        break
      else:
         print(f"Incorrect. You have {incorrect_guesses} incorrect guesses.")
    else:
       continue

    # Check if the game is over.
    if incorrect_guesses == 6:
      print("You lost!")
      break

  # Return the number of incorrect guesses.
  return incorrect_guesses

if __name__ == "__main__":
  word = input("Enter a word: ")
  number_of_incorrect_guesses = hangman(word)
  if number_of_incorrect_guesses == 6:
    print("You lost!")
  else:
    print("You won!")