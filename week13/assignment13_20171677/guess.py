class Guess:
    def __init__(self, word):
        self.secretWord = word
        self.currentStatus = []
        for i in word:
            self.currentStatus.append("_")
        self.guessedChars = []
        self.numTries = 0

    def display(self):
        print("Current status: ", " ".join(self.currentStatus))
        print("Tries:", self.numTries)
        print("Guessed char: ", " ".join(self.guessedChars))

    def guess(self, character):
        if character not in self.guessedChars:
            self.guessedChars.append(character)

            if character in self.secretWord:
                for idx in range(len(self.secretWord)):
                    if character == self.secretWord[idx]:
                        self.currentStatus[idx] = character

        if character not in self.secretWord:
            self.numTries += 1

        if "".join(self.currentStatus) == self.secretWord:
            return True

        else:
            return False
