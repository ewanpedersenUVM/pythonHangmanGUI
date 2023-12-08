# HANGMAN GAME
Hangman Python Game with GUI
## Project Members
Ewan Pedersen\
Shamus Murphy

## Imports:
> pillow\
> random\
> tkinter\

## Wordlist
[Tom25 Hangman](https://github.com/Tom25/Hangman/blob/master/wordlist.txt)

## Used Resources for Questions:
[Geeks For Geeks](https://www.geeksforgeeks.org/)

## Tutorial:
- After running the program, click start game to select a random word from the database\
- The underscores that appear are the amount of letters in the word\
- Before you continue, submit your name to the leaderboard so that if you win it saves\
- But if you forgot to, do it before you finish solving or else it will not be added to the leaderboard\
- Just like regular hangman, you get six guesses, the amount it takes to complete the body\
- In the text box, submit either a letter or word for as a guess\
- Depending on which you choose, select the right button\
- If you get the correct letter, you will see a message and it will be replaced in the correct spot below the hangman image\
- If you get the wrong letter, the hangman image will update adding a new piece to the body\
- Each time the letter is added to the list of used letters\
- It will not let you use the same letter twice\
- Once you guess the correct word or get the last letter right, your name and amount of guesses will be added to the leaderboard\
- The word list that we used has a long list of words so it will be hard to get the same word twice\

## Notes:
- We had to use global variables which is the reason that many of the variables used are very short\
- Their full names are displayed in comments\
- Our Professor Murat said that using hangman was ok as long as we went above the expectations which is why the GUI is implemented\
- Most of the code used we already knew before but any questions were asked on Geeks for Geeks then used to our own advantage\

## Feature List:
- Leaderboard implemented\
- Using tkinter to create a GUI making a visually pleasing hangman game\
- Images visualizing and updating in real time showing the amount of guesses remaining\
- Thorough verification of inputs and use of buttons to separate letter guesses from word guesses\
- Algorithm created to make sure no guess is wasted\
- Massive word bank making the game playable for longer periods of time\
