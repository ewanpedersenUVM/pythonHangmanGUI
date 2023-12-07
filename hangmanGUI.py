import tkinter as tk
from PIL import Image, ImageTk
import random

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

    
def hangman(word, wordlist, decision, input, incorrect_guesses):

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
  return incorrect_guesses, wl, guess_result

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
        self.word_text = tk.Label(root, text="Word: ")
        self.word_text.pack()

    def button0_clicked(self): # start button
        global hiddenWord, wordlist, incorrect_guesses
        hiddenWord, wordlist = chooseWord()
        incorrect_guesses = 0
        self.update_image(0)

    def button1_clicked(self): # letter button
        input = self.text_box.get()
        incorrect_guesses = hangman(hiddenWord, wordlist, 'letter', input, incorrect_guesses)
        self.update_image(incorrect_guesses)

    def button2_clicked(self): # word button
        self.update_image()

    def update_image(self, number):
        # Replace the following line with your function to get a number between 0 and 6
        image_path = f"images/Hangman_{number}.png"
        self.img = Image.open(image_path)
        self.img = ImageTk.PhotoImage(self.img)
        self.img_label.configure(image=self.img)

if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanApp(root)
    root.mainloop()
