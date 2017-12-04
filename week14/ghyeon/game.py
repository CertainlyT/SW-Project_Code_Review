from hangman import Hangman
from guess import Guess
from word import Word


class Game:
    def gameMain():
        word = Word('words.txt')
        guess = Guess(word.randFromDB())

        print('%d words in DB' % word.count)

        finished = False
        hangman = Hangman()

        while hangman.remainingLives > 0:

            display = hangman.currentShape()
            print(display)
            display = guess.displayCurrent()
            print('Current: ' + display)
            display = guess.displayGuessed()
            print('Already Used: ' + display)

            guessedChar = input("Select a Letter: ")

            if len(guessedChar) == 1:
                if 65 <= ord(guessedChar) <= 90 or 97 <= ord(guessedChar) <= 122:
                    if 65 <= ord(guessedChar) <= 90:
                        guessedChar = chr(ord(guessedChar) + 32)
                    if guessedChar not in guess.used_set:
                        success = guess.guess(guessedChar)
                        if not success:
                            hangman.decreaseLife()

            finished = guess.finished()
            if finished:
                break

        if finished:
            print('Success')
            print('word [' + guess.word + ']')
        else:
            print('word [' + guess.word + ']')
            print("Guess:", end=" ")
            for i in range(len(guess.current)):
                print(guess.current[i], end=" ")
            print()
            print('Fail')


if __name__ == '__main__':
    Game.gameMain()
