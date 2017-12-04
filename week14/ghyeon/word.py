import random


class Word:

    def __init__(self, filename):

        self.words = []
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()

        self.count = 0
        for line in lines:
            word = line.rstrip()
            self.words.append(word)
            self.count += 1

    def table(self):
        return 'default'

    def randFromDB(self):
        r = random.randrange(self.count)
        return self.words[r]
