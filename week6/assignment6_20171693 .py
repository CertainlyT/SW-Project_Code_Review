import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, QGridLayout,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()
        
        
    def initUI(self):
        
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.title = QLabel('Name:')
        self.author = QLabel('Age:')
        self.review = QLabel('Score:')
        self.amount = QLabel('Amount:')
        result = QLabel('Result:')
        resultext = QTextEdit()
        add = QPushButton('Add ', self)
        delete = QPushButton('Del ', self)
        find = QPushButton('Find', self)
        inc = QPushButton('Inc ', self)
        show = QPushButton('Show', self)
        combobox1 = QComboBox()

        self.titleEdit = QLineEdit()
        self.authorEdit = QLineEdit()
        self.reviewEdit = QLineEdit()
        self.amountEdit = QLineEdit()
        combobox1.addItems(['Name', 'Show', 'Age'])
        layout = QVBoxLayout()
        upLayOut = QHBoxLayout()
        upLayOut.addWidget(self.title)
        upLayOut.addWidget(self.titleEdit)

        upLayOut.addWidget(self.author)
        upLayOut.addWidget(self.authorEdit)

        upLayOut.addWidget(self.review)
        upLayOut.addWidget(self.reviewEdit)
        middleLayOut = QHBoxLayout()
        middleLayOut.addStretch(1)
        middleLayOut.addWidget(self.amount)
        middleLayOut.addWidget(self.amountEdit)

        middleLayOut.addWidget(combobox1)
        downLayOut = QHBoxLayout()
        downLayOut.addStretch(1)
        downLayOut.addWidget(add)
        downLayOut.addWidget(delete)
        downLayOut.addWidget(find)
        downLayOut.addWidget(inc)
        downLayOut.addWidget(show)


        layout.addLayout(upLayOut)
        layout.addLayout(middleLayOut)
        layout.addLayout(downLayOut)
        layout.addWidget(result)
        layout.addWidget(resultext)



        self.setLayout(layout)
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

    def showScoreDB(self):
        pass
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())





