import random
#w = word
#wl = wordlist
#ip = input
#incorrect_guesses = ig
#ll = letter list
wl = ["_", "_", "_", "_", "_"]
ll = []
def hangman_letter(w, wl, ip, ig):
    global wordlist
    if len(ip) != 1:
        return ig, wl, False
    splitWord = list(w)
    result = None  # Initialize result variable outside the loop

    letter_found = False
    if ip in wl:
        result = "repeat"
    for index, letter in enumerate(splitWord):
        if letter == ip:
            wl[index] = ip
            letter_found = True
    if not letter_found:
          ig += 1
          result = "no"
          ll.append(ip)
    elif ip in w:
        result = "yes"
        ll.append(ip)
    elif ig == 6:
        result = "lose"
    return ig, wl, result

result = hangman_letter('apple', wl, 'p', 0)
print(result)
print(wl)

def hangman_word(w, wl, ip, ig):
    global wordlist
    result = None  # Initialize result variable outside the loop

    while ig < 6:
        if ip == w:
            wl = list(w)
            result = "yes"
        else:
            ig += 1
            result = "no"

        break  # Add a break statement to exit the loop

    return ig, wl, result

result_word = hangman_word('apple', wl, 'apple', 0)
print(result_word)
print(wl)