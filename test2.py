import random
#w = word
#wl = wordlist
#ip = input
#incorrect_guesses = ig
wl = ["_", "_", "_", "_", "_"]

def hangman_letter(w, wl, ip, ig):
    if len(ip) != 1:
        return ig, wl, False
    splitWord = list(w)
    result = None  # Initialize result variable outside the loop

    while ig < 6:
        letter_found = False
        for index, letter in enumerate(splitWord):
            if letter == ip:
                wl[index] = ip
                letter_found = True
        if not letter_found:
            ig += 1

        if ig == 6:
            result = "lose"
            break
        if ip in w:
            result = "yes"
        if ip in wl:
            result = "repeat"

        break  # Add a break statement to exit the loop

    return ig, wl, result

result = hangman_letter('apple', wl, 'p', 0)
print(result)
print(wl)

def hangman_word(w, wl, ip, ig):
    result = None  # Initialize result variable outside the loop

    while ig < 6:
        if ip == w:
            wl = list(w)
            result = "yes"
        else:
            ig += 1
            result = "lose"

        break  # Add a break statement to exit the loop

    return ig, wl, result

result_word = hangman_word('apple', wl, 'apple', 0)
print(result_word)
print(wl)