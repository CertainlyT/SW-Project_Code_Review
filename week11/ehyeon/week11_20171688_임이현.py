from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout

from keypad import numPadList, operatorList, constantList, functionList
import calcFunctions

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
        self.flag = 0;
        self.idx = 1;      #연산자를 연속하지 않고 한번만 사용하기위해 사용하는 변수./ 숫자 없이 연산자만 오는 오류도 처리할 수 있다.
        self.constantVal = ['3.141592', '3E+8', '340', '1.5E+8']
        self.parIdx = 0    #괄호가 열려있는 상태를 확인하는 변수 (열렸을 때: 1/닫혔을 때: 0)
        # Display Window
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

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


    def buttonClicked(self):

        if self.display.text() == 'Error!':
            self.display.setText('')

        button = self.sender()
        key = button.text()

        if key == '=':
            try:
                result = str(eval(self.display.text()))
                self.flag = 1
            except:
                result = 'Error!'
            self.display.setText(result)

        elif key == 'C':
            self.display.clear()
        elif key in constantList:
            self.idx = 0
            self.display.setText(self.display.text() + self.constantVal[constantList.index(key)])
        elif key in functionList:
            n = str(eval(self.display.text()))
            self.flag = 1
            if functionList.index(key) == 0:
                n=str(eval(self.display.text()))
                value = calcFunctions.factorial(n)
            elif functionList.index(key) == 1:
                value = calcFunctions.decToBin(n)
            elif functionList.index(key) == 2:
                value = calcFunctions.binToDec(n)
            elif functionList.index(key) == 3:
                value = calcFunctions.decToRoman(n)
            self.display.setText(str(value))
        elif key in operatorList:

            # 계산 결과에 괄호 연산자 버튼을 누르면 결과값이 나타나는 오류를 수정
            if self.flag == 1 and key == "(":
                self.display.setText("Error!")
                self.flag = 0;
            #괄호가 열려있을 때에만 괄호를 닫을 수 있도록 만들었다.
            elif key == "(":
                self.display.setText(self.display.text() + key)
                self.parIdx = 1
            elif self.parIdx == 1 and key == ")":
                self.display.setText(self.display.text() + key)
                self.parIdx = 0
            elif self.parIdx == 0 and key == ")":
                self.display.setText(self.display.text())
            #나머지의 경우에는 연산이 가능해지도록 한다.
            #연산자가 연속으로 중복되어 입력되는 것을 방지한다.
            else:
                if self.idx == 0:
                    self.idx = 1
                    self.display.setText(self.display.text() + key)
                    self.flag = 0

        #계산이 끝났을 때 연산자가 아닌 숫자 버튼을 누르면, 새로운 수로 시작하지 않고 결과 뒤에 새로운 숫자가 쓰여지는 것을 방지한다.
        elif key in numPadList:
            self.idx = 0
            if self.flag == 1 and key != "=":
                self.display.setText(key)
                self.flag = 0;
            #그리고 함수 계산 후에도 결과값 뒤에 새로운 숫자가 쓰여지는 것을 방지한다.
            elif self.flag == 1 :
                self.display.setText(key)
                self.flag = 0;
            else:
                self.display.setText(self.display.text() + key)
        else:
            self.display.setText(self.display.text() + key)




if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
