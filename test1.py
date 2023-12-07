import random

wordlist = ["_", "_", "_", "_", "_"]

"""def hangman(word, wordlist, decision, input, incorrect_guesses):
    splitWord = list(word)
    result = None

    while incorrect_guesses < 6:
        letter_found = False
        splitWord = list(word)
        if decision == 'letter':
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

        elif decision == 'word':
            if input == word:
                wordlist = list(word)
            else:
                incorrect_guesses += 1

        break  # Add a break statement to exit the loop

    return incorrect_guesses, wordlist, result"""
 

def hangman_letter(word, wordlist, input, incorrect_guesses):
    splitWord = list(word)

    while incorrect_guesses < 6:
        letter_found = False
        splitWord = list(word)
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
    while incorrect_guesses < 6:
        if input == word:
            wordlist = list(word)
            result = "yes"
        else:
            incorrect_guesses += 1
            result = "lose"

        break  # Add a break statement to exit the loop

    return incorrect_guesses, wordlist, result
