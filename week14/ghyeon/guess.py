class Guess:

    def __init__(self, word):
        self.word = word
        self.used_set = set()
        self.numTries = 0
        self.current = ["_"] * len(word)

    def finished(self):
        if "_" not in self.current:
            return True
        else:
            return False

    def displayCurrent(self):
        tmp = ""
        for i in range(len(self.current)):
            tmp += self.current[i] + " "
        return tmp

    def displayGuessed(self):
        tmp = ""
        for each in sorted(self.used_set):
            tmp += each + " "
        return tmp

    def guess(self, character):
        self.used_set.add(character)
        if character in self.word:
            for i in range(len(self.word)):
                if self.word[i] == character:
                    self.current[i] = character
            return True
        else:
            return False

