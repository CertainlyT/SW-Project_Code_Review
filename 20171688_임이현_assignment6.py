import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication, QLabel, QComboBox,
                             QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB(self.keyBox())
        
        
    def initUI(self):

        nameLabel=QLabel("Name:")
        ageLabel =QLabel("Age:")
        scoreLabel=QLabel("Score")
        self.writingName=QLineEdit()
        self.writingAge=QLineEdit()
        self.writingScore=QLineEdit()
        firstLine = QHBoxLayout()
        firstLine.addWidget(nameLabel)
        firstLine.addWidget(self.writingName)
        firstLine.addWidget(ageLabel)
        firstLine.addWidget(self.writingAge)
        firstLine.addWidget(scoreLabel)
        firstLine.addWidget(self.writingScore)

        amountLabel=QLabel("Amount:")
        keyLabel=QLabel("Key:")
        self.writingAmount=QLineEdit()
        self.keys=QComboBox()
        self.keys.addItem("Name")
        self.keys.addItem("Age")
        self.keys.addItem("Score")
        secondLine=QHBoxLayout()
        secondLine.addStretch(1)
        secondLine.addWidget(amountLabel)
        secondLine.addWidget(self.writingAmount)
        secondLine.addWidget(keyLabel)
        secondLine.addWidget(self.keys)


        addB=QPushButton("Add")
        delB=QPushButton("Del")
        findB=QPushButton("Find")
        incB=QPushButton("Inc")
        showB=QPushButton("Show")
        thrLine=QHBoxLayout()
        thrLine.addStretch(1)
        thrLine.addWidget(addB)
        thrLine.addWidget(delB)
        thrLine.addWidget(findB)
        thrLine.addWidget(incB)
        thrLine.addWidget(showB)

        resLabel=QLabel("Result:")
        fourLine=QHBoxLayout()
        fourLine.addWidget(resLabel)

        self.textBox=QTextEdit()
        fiveLine=QHBoxLayout()
        fiveLine.addWidget(self.textBox)

        vBox=QVBoxLayout()
        vBox.addLayout(firstLine)
        vBox.addLayout(secondLine)
        vBox.addLayout(thrLine)
        vBox.addLayout(fourLine)
        vBox.addLayout(fiveLine)

        addB.clicked.connect(lambda :self.add())
        showB.clicked.connect(lambda :self.showScoreDB(self.keyBox()))
        delB.clicked.connect(lambda  :self.delete())
        findB.clicked.connect(lambda :self.finding())
        incB.clicked.connect(lambda  :self.inc())

        self.setLayout(vBox)
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')    
        self.show()


    def closeEvent(self, event):

        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self,keyname):
        showText = ""
        for p in sorted(self.scoredb, key=lambda person: person[keyname]):
            for attr in sorted(p):
                showText += str(attr) + "=" + str(p[attr]) + "        \t"
            showText += "\n"
        self.textBox.setText(showText)


    def add(self):
        try:
            record = {'Name': self.writingName.text(), 'Age': int(self.writingAge.text()), 'Score': int(self.writingScore.text())}
        except :
            pass
        else:
            self.scoredb += [record]
            self.showScoreDB("Name")

    def keyBox(self):
        returnBox = self.keys.currentText()
        return returnBox

    def  delete(self):
        del_list = []
        for p in self.scoredb:
            if p['Name'] == self.writingName.text():
                del_list.append(p)
        for name in del_list:
            self.scoredb.remove(name)
        self.showScoreDB("Name")

    def finding(self):
        finding_text = ""
        for p in self.scoredb:
            if p['Name'] != self.writingName.text():
                continue
            for attr in sorted(p):
                finding_text += str(attr) + "=" + str(p[attr]) + "        \t"
            finding_text += "\n"
        self.textBox.setText(finding_text)

    def inc(self):
        try:
            for p in self.scoredb:
                if p['Name'] == self.writingName.text():
                    p['Score'] = str(int(p['Score']) + int(self.writingAmount.text()))
        except ValueError:
            pass
        self.showScoreDB("Name")



if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())





