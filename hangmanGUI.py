"""
Ewan Pedersen, Shamus Murphy
CS1210 - F
Final Project
"""


import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import random


global hiddenWord, wordlist, incorrect_guesses, letterList
wordlist = []
letterList = []
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
    
def leaderboard(name, incorrect_guesses):
    with open("leaderboard.txt", "a") as file:
        file.write(f"{name} | {incorrect_guesses}\n")

#w = word
#wl = wordlist
#ip = input
#incorrect_guesses = ig
# we are using bad naming scheme because of global variables

def hangman_letter(w, wl, ip, ig, ll):
    global wordlist
    if len(ip) != 1:
        return ig, wl, "invalid",
    splitWord = list(w)
    result = None  # Initialize result variable outside the loop
    letter_found = False
    if ip in ll:
      result = "repeat"
    for index, letter in enumerate(splitWord):
      if letter == ip:
        wl[index] = ip
        letter_found = True
    if (not letter_found) and (result != "repeat"):
        ig += 1
        result = "no"
    elif ip in w:
        result = "yes"
    elif ig == 6:
        result = "lose"
    if ip not in ll:
      ll.append(ip)
    return ig, wl, result, ll

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

class HangmanApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman GUI")
        # use aqua theme
        self.root.tk_setPalette(background='#ececec')
        # set header
        self.root.geometry("500x500")
        self.header = tk.Label(root, text="Welcome to Shamus and Ewans Hangman Game!")
        self.header.pack()
        
        self.button0 = tk.Button(root, text="Start Game", command=self.button0_clicked)
        self.button0.pack(side=tk.TOP, padx=5)
        # Text box
        self.header = tk.Label(root, text="Enter a letter or word:")
        self.header.pack()
        self.text_box = tk.Entry(root, width=30)
        self.text_box.pack(pady=10)
        # button to start game and choose a random word
        # Buttons to choose letter or word
       

        self.button1 = tk.Button(root, text="Letter", command=self.button1_clicked)
        self.button1.pack(side=tk.TOP, padx=5)
        
        self.button2 = tk.Button(root, text="Word", command=self.button2_clicked)
        self.button2.pack(side=tk.TOP, padx=5)

        # Hangman image
        self.image_path = "images/Hangman_0.png"
        self.img = Image.open(self.image_path)
        self.img = ImageTk.PhotoImage(self.img)
        self.img_label = tk.Label(root, image=self.img)
        self.img_label.pack()

        # Text showing the word with blanks and correct guesses
        self.word_text = tk.Label(root, text="Word: " + " ".join(wordlist))
        self.word_text.pack()

        # Text showing previous letter guesses
        self.letter_text = tk.Label(root, text="Letters: " + " ".join(letterList))
        self.letter_text.pack()

        #leaderboard title, name input, and button to submit
        self.leaderboard_title = tk.Label(root, text="Submit Name for Leaderboard")
        self.leaderboard_title.pack()
        self.leaderboard_name = tk.Entry(root, width=30)
        self.leaderboard_name.pack(pady=10)
        self.leaderboard_button = tk.Button(root, text="Submit", command=self.leaderboard_button_clicked)
        self.leaderboard_button.pack(side=tk.TOP, padx=5)

        #button to view leaderboard
        self.leaderboard_button = tk.Button(root, text="View Leaderboard", command=self.leaderboardView_button_clicked)
        self.leaderboard_button.pack(side=tk.TOP, padx=5)

    def button0_clicked(self): # start button
        global hiddenWord, wordlist, incorrect_guesses, letterList
        hiddenWord, wordlist = chooseWord()
        incorrect_guesses = 0
        letterList = []
        self.update_image(0)
        self.update_word_text(wordlist)
        self.update_letter_text(letterList)

    def button1_clicked(self): # letter button
        global hiddenWord, wordlist, incorrect_guesses, letterList
        input = str(self.text_box.get())
        incorrect_guesses, wordlist, result, letterList = hangman_letter(hiddenWord, wordlist, input.lower(), incorrect_guesses, letterList)
        if result == "yes":
            self.correct_message()
        elif result == "no":
            self.incorrect_message()
        elif result == "repeat":
            self.repeat_message()
        elif result == "lose":
            self.lose_message()
        self.update_image(int(incorrect_guesses))
        self.update_word_text(wordlist)
        self.update_letter_text(letterList)

    def button2_clicked(self): # word button
        global hiddenWord, wordlist, incorrect_guesses, letterList
        global name
        input = str(self.text_box.get())
        incorrect_guesses, wordlist, result = hangman_word(hiddenWord, wordlist, input.lower(), incorrect_guesses)
        if result == "yes":
            self.win_message()
            leaderboard(name, incorrect_guesses)
        elif result == "lose":
            self.lose_message()
        self.update_image(int(incorrect_guesses))
        self.update_word_text(wordlist)

    def leaderboard_button_clicked(self): # leaderboard button
        global hiddenWord, wordlist, incorrect_guesses, letterList
        global name
        name = str(self.leaderboard_name.get())

    def leaderboardView_button_clicked(self): # leaderboard view button
        with open("leaderboard.txt", "r") as file:
            allText = file.read()
            self.leaderboard_text = tk.Label(root, text=allText)
            self.leaderboard_text.pack()
        

    def update_image(self, number):
        image_path = f"images/Hangman_{number}.png"
        self.img = Image.open(image_path)
        self.img = ImageTk.PhotoImage(self.img)
        self.img_label.configure(image=self.img)

    # function to update text showing the word with blanks and correct guesses

    def update_word_text(self, wordlist):
        self.word_text.configure(text="Word: " + " ".join(wordlist))

    # function to update text showing previous letter guesses
    def update_letter_text(self, letterList):
        self.letter_text.configure(text="Letters: " + " ".join(letterList))

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
