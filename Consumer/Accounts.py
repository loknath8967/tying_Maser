from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from DATABASE.database import DATABASE
from STYLESHEET.Accounts import STYLESHEET
class manager(QScrollArea):

    def __init__(self, details):
        super(manager, self).__init__()
        self.setFixedWidth(250)
        self.setWidgetResizable(True)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        gp=QWidget()
        self.setWidget(gp)
        self.List=QFormLayout()
        gp.setLayout(self.List)
        self.entry(details)
    def entry(self, details):
        DBMS=DATABASE.AccountList()
        if DBMS is not None:
            for name, uuid in DBMS:
                btn=QPushButton(name)
                btn.setStyleSheet(STYLESHEET.manager_btn())
                btn.pressed.connect(lambda uuid=uuid: details.Entry(btn, uuid))
                self.List.addWidget(btn)

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
    def __init__(self, txt, color, font):
        super(Button, self).__init__()
        self.setText(txt)
        self.setStyleSheet(STYLESHEET.Button(color, font))

class details(QGroupBox):
    def __init__(self, ):
        super(details, self).__init__()
        self.account=None

        self.setStyleSheet(STYLESHEET.details())
        Label = QLabel("-:Information:-")
        Label.setFixedSize(250, 50)
        page = QGridLayout()
        page.addWidget(Label, 0, 0, Qt.AlignHCenter)
        self.setLayout(page)
        From_GP = QGroupBox()
        From_GP.setFixedSize(510, 510)
        page.addWidget(From_GP, 1, 0, Qt.AlignTop)
        Form = QGridLayout()
        From_GP.setLayout(Form)


        Form.addWidget(QLabel("Name: "), 0, 0)
        Form.addWidget(QLabel("Father: "), 1, 0)
        Form.addWidget(QLabel("DOB: "), 2, 0)
        Form.addWidget(QLabel("MOB: "), 3, 0)
        Form.addWidget(QLabel("gmail: "), 4, 0)
        Form.addWidget(QLabel("Address: "), 5, 0)
        Form.addWidget(QLabel("UserName: "), 6, 0)
        Form.addWidget(QLabel("PassWord: "), 7, 0)
        Form.addWidget(QLabel("Account: "), 8, 0)



        self.ListLine = [Line(), Line(), Line(),  Line(), Line(), Address(), Line(), Line(), Line()]

        Form.addWidget(self.ListLine[0], 0, 1, Qt.AlignRight)
        Form.addWidget(self.ListLine[1], 1, 1, Qt.AlignRight)
        Form.addWidget(self.ListLine[2], 2, 1, Qt.AlignRight)
        Form.addWidget(self.ListLine[3], 3, 1, Qt.AlignRight)
        Form.addWidget(self.ListLine[4], 4, 1, Qt.AlignRight)
        Form.addWidget(self.ListLine[5], 5, 1, Qt.AlignRight)
        Form.addWidget(self.ListLine[6], 6, 1, Qt.AlignRight)
        Form.addWidget(self.ListLine[7], 7, 1, Qt.AlignRight)
        Form.addWidget(self.ListLine[8], 8, 1, Qt.AlignRight)
        #==============

        update = Button("update", "white", "blue")
        update.setFixedSize(120, 30)
        Form.addWidget(update, 9, 1, Qt.AlignRight)

        delete = Button("Delete Account", "red", "white")
        delete.pressed.connect(self.Delete)
        delete.setFixedSize(210, 30)
        Form.addWidget(delete, 9, 0, Qt.AlignLeft)


    def Delete(self):
        DATABASE.DelAccount(self.ListLine[6].text())
        self.account.deleteLater()

    def Entry(self, button, userId):
        self.account=button
        DBMS=DATABASE.AccountDetails(userId)
        for db in DBMS:
            try:
                self.ListLine[DBMS.index(db)].setText(str(db))
            except Exception as error:
                print(error)

class AccountManager(QWidget):
    def __init__(self):
        super(AccountManager, self).__init__()
        layout=QGridLayout()
        self.setLayout(layout)
        detail=details()
        layout.addWidget(manager(detail), 0, 0)
        layout.addWidget(detail, 0, 1)

