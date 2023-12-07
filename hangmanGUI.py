import tkinter as tk
from tkinter import messagebox
import random

class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")

        self.word = ""
        self.guess_letters = []
        self.incorrect_guesses = 0

        # Create GUI elements
        self.word_label = tk.Label(master, text="")
        self.word_label.pack()

        self.incorrect_label = tk.Label(master, text="")
        self.incorrect_label.pack()

        self.guess_entry = tk.Entry(master)
        self.guess_entry.pack()

        self.guess_button = tk.Button(master, text="Guess", command=self.make_guess)
        self.guess_button.pack()

        self.final_guess_button = tk.Button(master, text="Final Guess", command=self.final_guess)
        self.final_guess_button.pack()

        # Start the game
        self.start_game()

    def start_game(self):
        self.word = input("Enter a word: ")
        self.update_display()

    def update_display(self):
        self.word_label.config(text=f"Word: {self.get_display_word()}")
        self.incorrect_label.config(text=f"Incorrect guesses: {self.incorrect_guesses}")

    def get_display_word(self):
        display_word = ""
        for letter in self.word:
            if letter in self.guess_letters:
                display_word += letter
            else:
                display_word += "_"
        return display_word

    def make_guess(self):
        guess = self.guess_entry.get().lower()

        if guess in self.guess_letters:
            messagebox.showinfo("Invalid Guess", "Letter already guessed. Please try again.")
        else:
            self.guess_letters.append(guess)
            if guess in self.word:
                messagebox.showinfo("Correct Guess", f"{guess} is in the word!")
            else:
                self.incorrect_guesses += 1
                messagebox.showinfo("Incorrect Guess", f"{guess} is not in the word.")
                if self.incorrect_guesses == 6:
                    self.end_game("You lost!")

        self.guess_entry.delete(0, tk.END)
        self.update_display()

    def final_guess(self):
        final_guess = input("What is the word?").lower()
        if final_guess == self.word:
            self.end_game(f"You Win! and you had only {self.incorrect_guesses} incorrect guesses!")
        else:
            messagebox.showinfo("Incorrect Guess", f"Incorrect. You have {self.incorrect_guesses} incorrect guesses.")

    def end_game(self, message):
        messagebox.showinfo("Game Over", message)
        self.master.destroy()

def main():
    root = tk.Tk()
    hangman_game = HangmanGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
