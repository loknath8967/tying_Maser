from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys, sqlite3, string, random
from DATABASE.database import DATABASE
from STYLESHEET.CREATEACCOUNT import STYLESHEET
from Incharge.signature import Incharge

class Item(QLabel):
    def __init__(self, TxT):
        super(Item, self).__init__()
        self.setText(TxT)
        self.setStyleSheet(STYLESHEET.ITEM())
class Error(QWidget):
    def __init__(self, parent, errorType, error):
        super(Error, self).__init__()
        lay_win = QGridLayout()
        self.setStyleSheet(STYLESHEET.ERROR())
        gp_gp = QGroupBox()
        lay_win.addWidget(gp_gp)
        layout = QGridLayout()
        gp_gp.setLayout(layout)
        gp_gp.setStyleSheet(STYLESHEET.ERROR_GP_GP())
        ErrorResult = QLabel('!!! SORRY !!!\n !! You`r Account Not Created For Some Issue !!')
        ErrorResult.setAlignment(Qt.AlignCenter)
        ErrorResult.setStyleSheet(STYLESHEET.ERROR_RESULT())

        layout.addWidget(ErrorResult, *(0, 0), Qt.AlignCenter)
        gp = QGroupBox()
        gp.setStyleSheet(STYLESHEET.ERROR_GP())
        layout1 = QGridLayout()
        gp.setLayout(layout1)
        layout.addWidget(gp, *(1, 0), Qt.AlignCenter)
        if errorType == "account":
            error = QLabel(
                f" ******** Mr./Miss. {error}  your {errorType} already here ***********\n\n***  please don`t  recreate new account  ***")
        else:
            error = QLabel(
                f" ******** Your {errorType} ' {error} ' already here ***********\n\n***  change {errorType} and Retry  ***")
        error.setAlignment(Qt.AlignCenter)
        error.setStyleSheet(STYLESHEET.ERROR_error())
        layout1.addWidget(error)
        btn_gp = QGroupBox()
        btn_gp.setStyleSheet(STYLESHEET.ERROR_BTN())

        btn_gp.setFixedSize(250, 120)
        btn_layout = QGridLayout()
        btn_gp.setLayout(btn_layout)
        btn_layout.addWidget(QLabel(""), 0, 0)
        Back = QPushButton("New Account")
        Back.pressed.connect(parent.CreateNew)
        btn_layout.addWidget(Back, 1, 2)
        Retry = QPushButton("Retry ")
        Retry.pressed.connect(parent.BackFunction)
        Retry.setStyleSheet(STYLESHEET.RETRY())
        btn_layout.addWidget(Retry, 1, 0)
        layout.addWidget(btn_gp, *(2, 0), Qt.AlignHCenter)
        lay_win.addWidget(QLabel(), 3, 0, Qt.AlignTop)
        self.setLayout(lay_win)


class Id(QLabel):
    def __init__(self, txt):
        super(Id, self).__init__()
        self.setText(txt)
        self.setStyleSheet(STYLESHEET.Id())


class NewAccount(QWidget):
    def __init__(self, parent, database, userId, password, accountType):
        super(NewAccount, self).__init__()

        lay_win = QGridLayout()
        self.setStyleSheet(STYLESHEET.NewAccount())
        # ---------------------
        gp_gp = QGroupBox()
        gp_gp.setFixedSize(530, 520)
        lay_win.addWidget(gp_gp)
        layout = QGridLayout()
        gp_gp.setLayout(layout)
        gp_gp.setStyleSheet(STYLESHEET.NewAccount_gp_gp())
        # ----------------
        HeaderStatus = QLabel("!!! Congratulation !!!\n !! New Account Has Been Created !!!")
        HeaderStatus.setFixedWidth(510)
        HeaderStatus.setAlignment(Qt.AlignCenter)
        HeaderStatus.setStyleSheet(STYLESHEET.HeaderStatus())

        layout.addWidget(HeaderStatus, 0, 0, 0, 3, Qt.AlignTop)
        # -----------------------------------------
        gp = QGroupBox()
        gp.setStyleSheet(STYLESHEET.NewAccount_gp())
        layout1 = QFormLayout()
        gp.setLayout(layout1)

        # ====================
        layout.addWidget(gp, *(2, 0), Qt.AlignCenter)
        layout1.addWidget(QLabel('\n\n'))
        layout1.addRow(Item('Name : '), Item(database[0]))
        layout1.addRow(Item('Father : '), Item(database[1]))
        layout1.addRow(Item('DOB : '), Item(database[2]))
        layout1.addRow(Item('Address : '),
                       Item(f'{database[5]},{database[6]},{database[7]},{database[8]}, {database[9]}'))
        layout1.addRow("Account: ", Item(accountType))
        layout1.addRow(Item('Username : '), Id(userId))
        layout1.addRow(Item('password : '), Id(password))

        # --------------------       button group      ----------------------------------------------------------------
        btn_gp = QGroupBox()
        btn_gp.setStyleSheet(STYLESHEET.BTN_Gp())
        btn_gp.setFixedHeight(120)
        btn_layout = QGridLayout()
        btn_layout.addWidget(Incharge("SYSTEM"), 0, 0, Qt.AlignRight)
        btn_gp.setLayout(btn_layout)
        NewEntry = QPushButton("Create New Account ")
        NewEntry.pressed.connect(parent.CreateNew)
        NewEntry.setStyleSheet(STYLESHEET.NewEntry())
        NewEntry.setFixedSize(210, 30)
        btn_layout.addWidget(NewEntry, 1, 0, Qt.AlignLeft)

        layout.addWidget(btn_gp, 4, 0, 4, 4, Qt.AlignTop)
        self.setLayout(lay_win)


class Result(QWidget):
    def __init__(self, parent, database, password, AccountType, PERMISSIONS):
        super(Result, self).__init__()

        self.new_layout = None
        self.old_layout = QGroupBox()
        self.Layout = QGridLayout()
        self.Layout.addWidget(self.old_layout)
        self.setLayout(self.Layout)

        self.dataProcess(parent, database, password, AccountType, PERMISSIONS)

    def dataProcess(self, parent, database, password, AccountType, PERMISSIONS):
        gmail = DATABASE.Gmail(database[4])
        if gmail:
            self.complete(Error(parent, "gmail address", gmail[0]))
        else:
            data = DATABASE.detailsChecking(database)
            if data:
                if data[0][0] == database[0]:
                    self.complete(Error(parent, "account", database[0]))
                else:
                    self.complete(Error(parent, "mobile number", database[3]))
            else:

                self.createAccount(parent, database, password, AccountType, PERMISSIONS)

    def createAccount(self, parent, database, password, account, PERMISSIONS):
        try:
            userId = self.username(database[0])
            if DATABASE.idChecking(userId):
                self.createAccount(parent, database, password, account, PERMISSIONS)

            else:
                DATABASE.NewAccount(database, userId, password, account, PERMISSIONS)
                self.complete(NewAccount(parent, database, userId=userId, password=password, accountType=account))
        except Exception as error:
            print(error)



    @staticmethod
    def username(name):
        name = name.split(" ")
        try:
            letter = name[1][0]
        except:
            letter = random.choice(string.ascii_uppercase)
        userId = f'{name[0][0]}{random.randint(1000, 9999)}{random.choice(string.ascii_letters)}{random.randint(1000, 9999)}{letter}'
        return userId

    def complete(self, widget):
        self.new_layout = widget
        self.Layout.replaceWidget(self.old_layout, self.new_layout)
        self.old_layout.close()
        self.new_layout.show()
