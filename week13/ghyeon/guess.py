class Guess:

    def __init__(self, word):
        self.word = word
        self.used_dic = {}
        self.numTries = 0
        self.current = ["_"] * len(word)

    def display(self):
        print()
        for i in range(len(self.current)):
            print(self.current[i], end=" ")
        print("\n")
        print("You failed %d times.\n" % self.numTries)

    def guess(self, character):
        if len(character) == 1:
            if character in self.used_dic:
                print("You've been used it.")
            else:
                self.used_dic[character] = 1
                if character in self.word:
                    idx_list = []
                    for i in range(len(self.word)):
                        if self.word[i] == character:
                            idx_list.append(i)
                    for each in idx_list:
                        self.current[each] = character
                else:
                    self.numTries += 1

            if "_" in self.current:
                return False
            else:
                return True
        else:
            print("Input one character.")
            return False

