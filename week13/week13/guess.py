class Guess:

    def __init__(self, word):

        self.secretWord = word
        self.ans_list = []
        self.currentStatus = ''
        self.count = 0
        for i in range (len(self.secretWord)):
            self.ans_list.append('_')
            self.currentStatus += '_'
        self.numTries = 0
        self.guessedChars = {''}
        self.idx = []



    def display(self):

        print("Current: "+self.currentStatus)
        print("Tries: "+str(self.numTries))


    def guess(self, character):
        # 지금까지 알아낸 글자와 위치 반환하기
        # 주어진 글자를 사용한 글자의 집합에 원소로 추가

        self.currentStatus = ''
        self.count = 0
        self.guessedChars.add(character)
        for i in range (len(self.secretWord)):
            if i not in self.idx and ( self.secretWord[i] == character ):
                self.count += 1
                self.idx.append(i)
                self.ans_list[i] = character
                self.currentStatus += self.ans_list[i]


            else:
                self.currentStatus += self.ans_list[i]

        if self.count == 0:
            self.numTries +=1
            return False

        elif len(self.idx) == len(self.secretWord):
            return True
        else:
            return False




