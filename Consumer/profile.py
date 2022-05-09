from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from STYLESHEET.profile import STYLESHEET

class Line(QLineEdit):
    def __init__(self):
        super(Line, self).__init__()
        self.setStyleSheet(STYLESHEET.Line())
        self.setDisabled(True)

class Address(QTextEdit):
    def __init__(self):
        super(Address, self).__init__()
        self.setFixedSize(270, 120)
        self.setDisabled(True)
        self.setStyleSheet(STYLESHEET.Address())
class Button(QPushButton):
    def __init__(self, txt):
        super(Button, self).__init__()
        self.setText(txt)
        self.setStyleSheet(STYLESHEET.Button())





class profile(QGroupBox):
    def __init__(self, info):
        super(profile, self).__init__()
        self.setStyleSheet(STYLESHEET.profile())
        Label = QLabel("-:Information:-")
        Label.setFixedSize(250, 90)
        page = QGridLayout()
        page.addWidget(Label, 0, 0, Qt.AlignHCenter)
        self.setLayout(page)
        From_GP = QGroupBox()
        From_GP.setFixedSize(450, 490)
        page.addWidget(From_GP, 1, 0, Qt.AlignTop)
        Form = QGridLayout()
        From_GP.setLayout(Form)

        Form.addWidget(QLabel("Name: "), 0, 0)
        Form.addWidget(QLabel("Father: "), 1, 0)
        Form.addWidget(QLabel("DOB: "), 2, 0)
        Form.addWidget(QLabel("MOB: "), 3, 0)
        Form.addWidget(QLabel("gmail: "), 4, 0)
        Form.addWidget(QLabel("Address: "), 5, 0)
        Form.addWidget(QLabel("Account: "), 6, 0)
        Form.addWidget(QLabel("UserName: "), 7, 0)
        Form.addWidget(QLabel("PassWord: "), 8, 0)


        self.ListLine = [Line(), Line(), Line(), Line(), Line(), Address(), Line(), Line(), Line()]

        Form.addWidget(self.ListLine[0], 0, 1, Qt.AlignRight)
        Form.addWidget(self.ListLine[1], 1, 1, Qt.AlignRight)
        Form.addWidget(self.ListLine[2], 2, 1, Qt.AlignRight)
        Form.addWidget(self.ListLine[3], 3, 1, Qt.AlignRight)
        Form.addWidget(self.ListLine[4], 4, 1, Qt.AlignRight)
        Form.addWidget(self.ListLine[5], 5, 1, Qt.AlignRight)
        Form.addWidget(self.ListLine[6], 6, 1, Qt.AlignRight)
        Form.addWidget(self.ListLine[7], 7, 1, Qt.AlignRight)
        Form.addWidget(self.ListLine[8], 8, 1, Qt.AlignRight)
        # ==============

        update = Button("update")
        update.setFixedSize(120, 30)
        Form.addWidget(update, 9, 1, Qt.AlignRight)
        self.dataEntry(info)

    def dataEntry(self, info):
        for db in info:
            if info.index(db)<=8:
                self.ListLine[info.index(db)].setText(str(db))

