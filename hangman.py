def hangman(word, decision, input, incorrect_guesses):

  guess_letters = []

  while incorrect_guesses < 6:
    if decision == 'letter':
      try:
          index = word.index(input)
          guess_letters.append(input)
      except ValueError:
            incorrect_guesses += 1
    elif decision == 'word':
      try:
          index = word.index(input)
      except ValueError:
            incorrect_guesses += 1
    elif input in guess_letters :
       print("Letter already guessed please try again")
    elif incorrect_guesses == 6:
      break
  return incorrect_guesses