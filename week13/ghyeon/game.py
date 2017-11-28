from hangman import Hangman
from guess import Guess
from word import Word


def gameMain():
    word = Word('words.txt')
    guess = Guess(word.randFromDB())

    finished = False
    hangman = Hangman()
    maxTries = hangman.getLife()

    while guess.numTries < maxTries:

        display = hangman.get(maxTries - guess.numTries)
        print(display)
        guess.display()

        guessedChar = input('Select a letter: ')

        finished = guess.guess(guessedChar)
        if finished:
            break

    if finished:
        print('Success')
    else:
        print(hangman.get(0))
        print('word [' + guess.word + ']')
        print("Guess:", end=" ")
        for i in range(len(guess.current)):
            print(guess.current[i], end=" ")
        print()
        print('Fail')


if __name__ == '__main__':
    gameMain()
