from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout

from keypad2 import numPadList, operatorList, constantList, functionList, constantValueList
import calcFunctions
from factorial import factorial


class Button(QToolButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


class Calculator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Display Window
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)
        self.display.setText("")

        # Button Creation and Placement
        numLayout = QGridLayout()
        opLayout = QGridLayout()
        constLayout = QGridLayout()
        funcLayout = QGridLayout()

        buttonGroups = {
            'num': {'buttons': numPadList, 'layout': numLayout, 'columns': 3},
            'op': {'buttons': operatorList, 'layout': opLayout, 'columns': 2},
            'constants': {'buttons': constantList, 'layout': constLayout, 'columns': 1},
            'functions': {'buttons': functionList, 'layout': funcLayout, 'columns': 1},
        }
        # Set Flag for Error Exception
        self.flag = ""

        for label in buttonGroups.keys():
            r = 0; c = 0
            buttonPad = buttonGroups[label]
            for btnText in buttonPad['buttons']:
                button = Button(btnText, self.buttonClicked)
                buttonPad['layout'].addWidget(button, r, c)
                c += 1
                if c >= buttonPad['columns']:
                    c = 0; r += 1

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 2)
        mainLayout.addLayout(numLayout, 1, 0)
        mainLayout.addLayout(opLayout, 1, 1)
        mainLayout.addLayout(constLayout, 2, 0)
        mainLayout.addLayout(funcLayout, 2, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle("My Calculator")

    def flagCheck(self):
        if self.flag == "error":
            self.display.clear()

    def buttonClicked(self):
        self.flagCheck()
        button = self.sender()
        key = button.text()

        if key == "=":
            try:
                result = str(eval(self.display.text()))
            except:
                result = "Error!"
                self.display.setText(result)
                self.flag = "error"
            else:
                self.display.setText(result)

        elif key == "C":
            self.display.clear()
            self.flag = ""

        elif key in constantList:
            if self.flag != "number" and self.flag != "constant":
                idx = constantList.index(key)
                self.display.setText(self.display.text() + constantValueList[idx])
                self.flag = "constant"

        elif key == functionList[0]:
            if self.display.text() != "":
                n = eval(self.display.text())
                if isinstance(n, int):
                    if 0 <= int(n) <= 17:
                        value = factorial(int(n))
                        self.flag = "number"
                    else:
                        value = 'Error!'
                        self.flag = "error"
                else:
                    value = 'Error!'
                    self.flag = "error"
            else:
                value = 'Error!'
                self.flag = "error"
            self.display.setText(str(value))
        elif key == functionList[1]:
            if self.display.text() != "":
                n = str(eval(self.display.text()))
                value = calcFunctions.decToBin(n)
                if len(value) > 15:
                    value = "Too long"
                    self.flag = "error"
                else:
                    self.flag = "bin"
            else:
                value = 'Error!'
                self.flag = "error"
            self.display.setText(str(value))

        elif key == functionList[2]:
            if self.display.text() != "":
                n = str(eval(self.display.text()))
                value = calcFunctions.binToDec(n)
                if value == "Error!":
                    self.flag = "error"
                else:
                    self.flag = "number"
            else:
                value = 'Error!'
                self.flag = "error"
            self.display.setText(str(value))

        elif key == functionList[3]:
            n = self.display.text()
            value = calcFunctions.decToRoman(n)
            self.display.setText(str(value))
        elif key in operatorList:
            if self.flag == "bin":
                pass
            elif key == "(" or key == ")":
                self.display.setText(self.display.text() + key)
            elif self.flag != "operator":
                self.display.setText(self.display.text() + key)
                self.flag = "operator"

        else:
            self.flagCheck()
            if self.flag != "constant" and self.flag != "bin":
                if self.display.text() == "0":
                    if key == "0":
                        pass
                    elif key == ".":
                        self.display.setText(self.display.text() + key)
                    else:
                        self.display.setText(key)
                elif key == ".":
                    if "." in self.display.text():
                        pass
                    elif self.display.text() == "":
                        pass
                    else:
                        self.display.setText(self.display.text() + key)
                else:
                    self.display.setText(self.display.text() + key)
                self.flag = "number"
        print(self.flag)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
