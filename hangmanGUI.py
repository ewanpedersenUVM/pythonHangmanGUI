import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import random

global hiddenWord, wordlist, incorrect_guesses
wordlist = []

def get_number(x):
    # Replace the following line with your function to get a number between 0 and 6
    return x+1

def chooseWord():
    with open("wordlist.txt", "r") as file: 
        allText = file.read() 
        words = list(map(str, allText.split()))
        word = random.choice(words)
        wordList = ["_"] * len(word)
        return word, wordList

    
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

class HangmanApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman GUI")

        # Text box
        self.text_box = tk.Entry(root, width=30)
        self.text_box.pack(pady=10)
        # button to start game and choose a random word
        # Buttons to choose letter or word
        self.button0 = tk.Button(root, text="Start Game", command=self.button0_clicked)
        self.button0.pack(side=tk.TOP, padx=5)

        self.button1 = tk.Button(root, text="Letter", command=self.button1_clicked)
        self.button1.pack(side=tk.LEFT, padx=5)
        
        self.button2 = tk.Button(root, text="Word", command=self.button2_clicked)
        self.button2.pack(side=tk.RIGHT, padx=5)

        # Hangman image
        self.image_path = "images/Hangman_0.png"
        self.img = Image.open(self.image_path)
        self.img = ImageTk.PhotoImage(self.img)
        self.img_label = tk.Label(root, image=self.img)
        self.img_label.pack()

        # Text showing the word with blanks and correct guesses
        self.word_text = tk.Label(root, text="Word: " + " ".join(wordlist))
        self.word_text.pack()

    def button0_clicked(self): # start button
        global hiddenWord, wordlist, incorrect_guesses
        hiddenWord, wordlist = chooseWord()
        incorrect_guesses = 0
        self.update_image(0)
        self.update_word_text(wordlist)

    def button1_clicked(self): # letter button
        input = str(self.text_box.get())
        incorrect_guesses, wordlist, result = hangman_letter(hiddenWord, wordlist, input, incorrect_guesses)
        if result == "yes":
            self.correct_message()
        elif result == "no":
            self.incorrect_message()
        elif result == "repeat":
            self.repeat_message()
        self.update_image(int(incorrect_guesses))
        self.update_word_text(wordlist)

    def button2_clicked(self): # word button
        input = str(self.text_box.get())
        incorrect_guesses, wordlist, result = hangman_word(hiddenWord, wordlist, input, incorrect_guesses)
        if result == "yes":
            self.win_message()
        elif result == "lose":
            self.lose_message()
        self.update_image(int(incorrect_guesses))
        self.update_word_text(wordlist)

    def update_image(self, number):
        image_path = f"images/Hangman_{number}.png"
        self.img = Image.open(image_path)
        self.img = ImageTk.PhotoImage(self.img)
        self.img_label.configure(image=self.img)

    # function to update text showing the word with blanks and correct guesses

    def update_word_text(self, wordlist):
        self.word_text.configure(text="Word: " + " ".join(wordlist))

    #message boxes for all outcomes: win, lose, repeat, incorrect guess
    def win_message(self):
        messagebox.showinfo("Win", "You win! Would you like to add your name to the leaderboard?")
        #add name to leaderboard
        #display leaderboard

    def lose_message(self):
        messagebox.showinfo("Lose", "You lose!")
#messagebox text input and button to add name to leaderboard, input name and incorrect guesses to function leaderboard(name, incorrect_guesses)


    def repeat_message(self):
        messagebox.showinfo("Repeat", "You've already guessed that letter!")

    def incorrect_message(self):
        messagebox.showinfo("Incorrect", "Incorrect letter!")

    def correct_message(self):
        messagebox.showinfo("Correct", "Correct letter!")


if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanApp(root)
    root.mainloop()
