from word import *

class Guess:
    numTries = 0
    guessedChars = []
    currentStatus = ''
    currentList = []
    currentPrintList = []

    def __init__(self, word):
        self.secretWord = word
        for char in word:
            self.currentList += char
        print(self.currentList)
        self.currentPrintList += '_'*len(word)
    def display(self):

        self.numTries += 1

    def guess(self, character):
        if character in self.secretWord:
            self.numTries -= 1
            self.currentStatus = ''
            for i, char in enumerate(self.currentList):
                if character == char:
                    self.currentPrintList[i] = character
            for char in self.currentPrintList:
                self.currentStatus += char
        if self.secretWord == self.currentStatus:
            return True






