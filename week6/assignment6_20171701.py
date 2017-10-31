import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication, QLabel,
                             QComboBox, QTextEdit, QLineEdit, QMessageBox)


class ScoreDB(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()

    def initUI(self):
        # Line 1
        nameLabel = QLabel("Name: ")
        ageLabel = QLabel("Age: ")
        scoreLabel = QLabel("Score: ")
        self.nameInput = QLineEdit()
        self.ageInput = QLineEdit()
        self.scoreInput = QLineEdit()
        hbox_input = QHBoxLayout()
        hbox_input.addWidget(nameLabel)
        hbox_input.addWidget(self.nameInput)
        hbox_input.addWidget(ageLabel)
        hbox_input.addWidget(self.ageInput)
        hbox_input.addWidget(scoreLabel)
        hbox_input.addWidget(self.scoreInput)

        # Line 2
        amountLabel = QLabel("Amount: ")
        self.amountInput = QLineEdit(self)
        keyLabel = QLabel("Key: ")
        self.select = QComboBox(self)
        self.select.addItem("Name")
        self.select.addItem("Age")
        self.select.addItem("Score")
        hbox_amount_key = QHBoxLayout()
        hbox_amount_key.addStretch(1)
        hbox_amount_key.addWidget(amountLabel)
        hbox_amount_key.addWidget(self.amountInput)
        hbox_amount_key.addWidget(keyLabel)
        hbox_amount_key.addWidget(self.select)

        # Line 3
        addButton = QPushButton("Add")
        delButton = QPushButton("Del")
        findButton = QPushButton("Find")
        incButton = QPushButton("Inc")
        showButton = QPushButton("Show")
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(addButton)
        hbox.addWidget(delButton)
        hbox.addWidget(findButton)
        hbox.addWidget(incButton)
        hbox.addWidget(showButton)

        # Line 4
        resultLabel = QLabel("Result:")
        hbox_result = QHBoxLayout()
        hbox_result.addWidget(resultLabel)

        # Line 5
        self.result_print = QTextEdit(self)
        hbox_print = QHBoxLayout()
        hbox_print.addWidget(self.result_print)

        # connect
        showButton.clicked.connect(lambda: self.showButtonClicked())
        addButton.clicked.connect(lambda: self.addButtonClicked())
        delButton.clicked.connect(lambda: self.delButtonClicked())
        findButton.clicked.connect(lambda: self.findButtonClicked())
        incButton.clicked.connect(lambda: self.incButtonClicked())

        # Layout Set
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox_input)
        vbox.addLayout(hbox_amount_key)
        vbox.addLayout(hbox)
        vbox.addLayout(hbox_result)
        vbox.addLayout(hbox_print)
        self.setLayout(vbox)
        self.setGeometry(300, 300, 600, 350)
        self.setWindowTitle('Assignment6')    
        self.show()

    # re-check close, write scoredb
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.writeScoreDB()
            event.accept()
        else:
            event.ignore()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            self.result_print.setText("New DB")
            return

        try:
            self.scoredb = pickle.load(fH)
        except:
            self.result_print.setText("Empty DB")
        else:
            self.showScoreDB('Name')
        fH.close()
        return self.scoredb

    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self, keyname):
        print_text = ""
        for each in sorted(self.scoredb, key=lambda x: x[keyname]):
            for attr in sorted(each):
                print_text += attr + "=" + str(each[attr]) + "        " + "\t"
            print_text += "\n"
        self.result_print.setText(print_text)

    def getKey(self):
        text = self.select.currentText()
        return text

    def showButtonClicked(self):
        key = self.getKey()
        return self.showScoreDB(key)

    def addButtonClicked(self):
        try:
            record = {'Name': self.nameInput.text(), 'Age': int(self.ageInput.text()),
                      'Score': int(self.scoreInput.text())}
        except:
            self.result_print.setText("Input all items or input correctly.")
        else:
            self.scoredb += [record]
            self.showScoreDB(self.getKey())

    def delButtonClicked(self):
        try:
            except_list = []
            for p in self.scoredb:
                if p['Name'] != self.nameInput.text():
                    except_list.append(p)
            self.scoredb = except_list
            self.showScoreDB(self.getKey())
        except:
            pass

    def findButtonClicked(self):
        try:
            print_text = ""
            for each in self.scoredb:
                if each['Name'] == self.nameInput.text():
                    for attr in sorted(each):
                        print_text += attr + "=" + str(each[attr]) + "        " + "\t"
                    print_text += "\n"
            self.result_print.setText(print_text)
        except:
            pass

    def incButtonClicked(self):
        try:
            for each in self.scoredb:
                if each['Name'] == self.nameInput.text():
                    each['Score'] += int(self.amountInput.text())
            self.showScoreDB(self.getKey())
        except:
            self.result_print.setText("Input Name and Amount.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
