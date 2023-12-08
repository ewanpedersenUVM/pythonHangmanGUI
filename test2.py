import random

wordlist = ["_", "_", "_", "_", "_"]

def hangman_letter(word, wordlist, input, incorrect_guesses):
    if len(input) != 1:
        return incorrect_guesses, wordlist, False
    splitWord = list(word)
    result = None  # Initialize result variable outside the loop

    while incorrect_guesses < 6:
        letter_found = False
        for index, letter in enumerate(splitWord):
            if letter == input:
                wordlist[index] = input
                letter_found = True
        if not letter_found:
            incorrect_guesses += 1

        if incorrect_guesses == 6:
            result = "lose"
            break
        if input in word:
            result = "yes"
        if input in wordlist:
            result = "repeat"

        break  # Add a break statement to exit the loop

    return incorrect_guesses, wordlist, result

result = hangman_letter('apple', wordlist, 'p', 0)
print(result)
print(wordlist)

def hangman_word(word, wordlist, input, incorrect_guesses):
    result = None  # Initialize result variable outside the loop

    while incorrect_guesses < 6:
        if input == word:
            wordlist = list(word)
            result = "yes"
        else:
            incorrect_guesses += 1
            result = "lose"

        break  # Add a break statement to exit the loop

    return incorrect_guesses, wordlist, result

result_word = hangman_word('apple', wordlist, 'apple', 0)
print(result_word)
print(wordlist)