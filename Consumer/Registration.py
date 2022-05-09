from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Consumer.CREATEACCOUNT import Result
from DATABASE.database import DATABASE
from STYLESHEET.Registration import STYLESHEET

class Registration(QGridLayout):
    def __init__(self):
        super(Registration, self).__init__()

    def addData(self, key, value, required, row, column):
        gp = QGroupBox()
        gp.setFixedSize(418, 75)
        layout = QFormLayout()
        gp.setLayout(layout)
        layout.addRow(key, value)
        required.setAlignment(Qt.AlignBottom)
        required.setVisible(False)
        required.setFixedHeight(17)
        required.setStyleSheet(STYLESHEET.Registration())
        layout.addWidget(required)
        self.addWidget(gp, row, column)


class filed(QLineEdit):
    def __init__(self, placeholder, RegExp, Required):
        super(filed, self).__init__()
        self.setFixedSize(210, 30)

        self.setPlaceholderText(placeholder)
        self.setStyleSheet(STYLESHEET.field())
        self.setValidator(QRegExpValidator(RegExp, self))
        self.textChanged.connect(lambda: (Required.setVisible(False), self.setText(str(self.text()).upper())))


class phone(QLineEdit):
    def __init__(self, Required):
        super(phone, self).__init__()
        country_code = QComboBox(self)
        country_code.setFixedHeight(30)
        country_code.addItem("+91")
        country_code.setStyleSheet(STYLESHEET.phone_code())

        self.setFixedSize(210, 30)
        self.setInputMask('000_000_0000 ')
        self.setStyleSheet(STYLESHEET.phone_number())
        self.textChanged.connect(lambda: self.Validator(Required))

    def Validator(self, Required):
        try:
            Required.setVisible(False)
            if len(self.text()) == 13:
                self.setStyleSheet(STYLESHEET.phone_valid())
            elif len(self.text()) == 12:
                self.setStyleSheet(STYLESHEET.phone_number())

        except Exception as error:
            print(error)


class state(QLineEdit):
    def __init__(self, Required):
        super(state, self).__init__()
        self.setFixedSize(210, 30)
        self.setText("WEST BENGAL")
        self.setStyleSheet(STYLESHEET.state())
        self.setReadOnly(True)
        self.textChanged.connect(lambda: Required.setVisible(False))


class Label(QLabel):
    def __init__(self, txt):
        super(Label, self).__init__()
        self.setStyleSheet(STYLESHEET.Label())
        self.setText(txt)


class DOB(QDateEdit):
    def __init__(self, Required):
        super(DOB, self).__init__()
        self.setCalendarPopup(True)
        self.setStyleSheet(STYLESHEET.DOB())

        self.setDateRange(QDate(1990, 1, 1), QDate.currentDate())
        self.setDate(QDate.currentDate())
        self.dateChanged.connect(lambda: self.Update(Required))
        self.setFixedSize(210, 30)
        self.setAlignment(Qt.AlignRight)

    def Update(self, Required):
        if int(QDate.currentDate().toString('yyyy')) - int(self.date().toString('yyyy')) >= 5:
            Required.setVisible(False)
        else:
            Required.setVisible(True)


class PASSWORD(QLineEdit):
    def __init__(self, placeholder, Required):
        super(PASSWORD, self).__init__()
        self.setFixedSize(210, 30)

        self.setPlaceholderText(placeholder)
        self.setStyleSheet(STYLESHEET.PASSWORD())

        self.textChanged.connect(lambda: Required.setVisible(False))


class gmail(QLineEdit):
    def __init__(self, placeholder, Required):
        super(gmail, self).__init__()
        self.setFixedSize(210, 30)
        self.setValidator(QRegExpValidator(QRegExp('^[a-z0-9]+[\._]?[a-z0-9]+[@]\gmail+[.]\com$'), self))

        self.setPlaceholderText(placeholder)
        self.setStyleSheet(STYLESHEET.gmail())

        self.textChanged.connect(lambda: Required.setVisible(False))


class AccountCreate(QWidget):
    DATABASE = {"entry": "", "accountType": "", "PERMISSIONS": ""}
    def __init__(self):
        super(AccountCreate, self).__init__()
        self.new_layout = None
        self.old_layout = None
        Title = Label("Create New Account")
        Title.setFixedHeight(20)
        Title.setStyleSheet(STYLESHEET.AccountCreate_Title())
        scroller = QScrollArea()
        scroller.setMinimumSize(750, 550)
        scroller.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroller.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.old_layout = scroller
        self.surface = QGridLayout()
        self.surface.addWidget(Title, 0, 0,  Qt.AlignHCenter)
        Interface = QGroupBox()
        Interface.setFixedSize(930, 630)
        scroller.setWidget(Interface)
        self.surface.addWidget(scroller, 1, 0, 1, 1, Qt.AlignCenter)

        layout = Registration()
        Interface.setLayout(layout)

        Requirement = [QLabel("Name must be Filed *"), QLabel(" Father name must be Filed *"),
                       QLabel("Minimum age 5 years old *"), QLabel("Mobile number must be Filed *"),
                       QLabel("Gmail must be Filed *"), QLabel("Village must be Filed *"),
                       QLabel("Post office must be Filed *"), QLabel("District must be Filed *"),
                       QLabel("PIN number must be Filed *"), QLabel("State must be Filed *"),
                       QLabel("Password minimum 4 digit Filed *"), QLabel("Password not match *")]

        entryList = [filed("Enter Your Name", QRegExp('^[A-z]+[\._]'), Requirement[0]),
                     filed("Enter Your Father Name", QRegExp('^[A-z]+[\._]'), Requirement[1]),
                     DOB(Requirement[2]), phone(Requirement[3]),
                     gmail("Enter Gmail Address", Requirement[4]),
                     filed("Enter Village Name", QRegExp('^[A-z]+[\._]'), Requirement[5]),
                     filed("Enter Post Office Name", QRegExp('^[A-z]+[\._]'), Requirement[6]),
                     filed("Enter District Name", QRegExp('^[A-z]+[\._]'), Requirement[7]),
                     filed("Enter PIN Number", QRegExp("[0-9]{0,6}"), Requirement[8]),
                     state(Requirement[9])
                     ]
        self.setLayout(self.surface)

        password = [PASSWORD("Enter Password", Requirement[10]),
                    PASSWORD("Conform password", Requirement[11])]

        self.DATABASE["entry"] = [entryList, password]

        layout.addData(Label("Name          "), entryList[0], Requirement[0], 0, 0)
        layout.addData(Label("Father            "), entryList[1], Requirement[1], 0, 1)
        layout.addData(Label("Date of Barth"), entryList[2], Requirement[2], 1, 0)
        layout.addData(Label("Mobile No.      "), entryList[3], Requirement[3], 1, 1)
        layout.addData(Label("GMail           "), entryList[4], Requirement[4], 2, 0)
        layout.addData(Label("Village           "), entryList[5], Requirement[5], 2, 1)
        layout.addData(Label("Post            "), entryList[6], Requirement[6], 3, 0)
        layout.addData(Label("District           "), entryList[7], Requirement[7], 3, 1)
        layout.addData(Label("PIN             "), entryList[8], Requirement[8], 4, 0)
        layout.addData(Label("STATE           "), entryList[9], Requirement[9], 4, 1)
        layout.addData(Label("PassWord     "), password[0], Requirement[10], 5, 0)
        layout.addData(Label("Conf-PassWord"), password[1], Requirement[11], 5, 1)

        '''  Account permission '''

        Permission_gp = QGroupBox()
        Permission_gp.setStyleSheet(STYLESHEET.PERMISSION_GP())
        Permission_gp.setTitle("PERMISSION:-")
        Permission_gp.setFixedSize(930, 110)
        layout.addWidget(Permission_gp, 7, 0, 7, 2)
        Permission_Layout = QGridLayout()
        Permission_gp.setLayout(Permission_Layout)

        AC_TYPE = QComboBox()
        self.DATABASE["accountType"] = AC_TYPE
        AC_TYPE.setFixedHeight(30)

        AC_TYPE.setStyleSheet(STYLESHEET.AC_TYPE())
        AC_TYPE.addItems(["NORMAL ACCOUNT", "STANDARD ACCOUNT"])
        Permission_Layout.addWidget(Label("Account Type  "), 1, 1)
        Permission_Layout.addWidget(AC_TYPE, 1, 2, Qt.AlignLeft)

        PERMISSIONS = [PERMISSION("Question Editor"), PERMISSION("Question Entry"), PERMISSION("MarkSheet Editor"),
                       PERMISSION("Account Management"), PERMISSION("DataBase Management")]
        self.DATABASE["PERMISSIONS"] = PERMISSIONS
        PERMISSIONS[3].setVisible(False), PERMISSIONS[4].setVisible(False)
        PERMISSIONS[0].setFixedWidth(120), PERMISSIONS[1].setFixedWidth(115), PERMISSIONS[2].setFixedWidth(130)

        AC_TYPE.currentIndexChanged.connect(lambda: self.Change_Account_Type(AC_TYPE.currentText(), PERMISSIONS))

        Permission_Layout.addWidget(PERMISSIONS[0], 2, 0)
        Permission_Layout.addWidget(PERMISSIONS[1], 2, 1)
        Permission_Layout.addWidget(PERMISSIONS[2], 2, 2)
        Permission_Layout.addWidget(PERMISSIONS[3], 2, 3)
        Permission_Layout.addWidget(PERMISSIONS[4], 2, 4)
        Permission_Layout.addWidget(QLabel(), 2, 5, Qt.AlignLeft)

        createAc = QPushButton("Create Account")
        createAc.pressed.connect(lambda: self.CrateNewAccount(password, entryList, Requirement, AC_TYPE, PERMISSIONS))
        createAc.setFixedSize(210, 30)
        createAc.setStyleSheet(STYLESHEET.CreateAC())
        layout.addWidget(createAc, 15, 0, 15, 2, Qt.AlignHCenter)

        self.surface.addWidget(QLabel(""), 2, 0, Qt.AlignTop)

    @staticmethod
    def Change_Account_Type(AccountType, PERMISSION):
        if AccountType == "STANDARD ACCOUNT":
            PERMISSION[3].setVisible(True)
            PERMISSION[4].setVisible(True)
        else:
            PERMISSION[3].setVisible(False)
            PERMISSION[3].setChecked(False)
            PERMISSION[4].setVisible(False)
            PERMISSION[4].setChecked(False)

    def CrateNewAccount(self, PassWord, entryList, Required, AccountType, PERMISSIONS):
        global password
        try:
            answer = "right"
            database = []
            account_permission = []

            #   ==================  permissions   ============================

            for permission in PERMISSIONS:
                if permission.isChecked():
                    account_permission.append(permission.text())

            # -----------------------    password    ----------------------

            if len(PassWord[0].text()) >= 4:
                if PassWord[0].text() == PassWord[1].text():
                    password = PassWord[0].text()
                    Required[11].setVisible(False)
                else:
                    answer = "wrong"
                    Required[11].setVisible(True)

            else:
                answer = "wrong"
                Required[10].setVisible(True)

            # ----------------------------------- Information data   ----------------------
            for data in entryList:
                if entryList.index(data) == 2:
                    if int(QDate.currentDate().toString('yyyy')) - int(data.date().toString('yyyy')) < 5:
                        Required[entryList.index(data)].setVisible(True)
                        answer = "wrong"
                    else:
                        database.append(data.date().toString('dd-MM-yyyy'))
                elif data.text() != "":
                    if len(data.text()) < 5:
                        Required[entryList.index(data)].setVisible(True)
                    else:
                        if entryList.index(data) == 3:
                            print(data.text().replace("_", ""))
                            database.append(data.text().replace("_", ""))
                        else:
                            database.append(data.text())
                else:
                    answer = "wrong"
                    Required[entryList.index(data)].setVisible(True)

            # -------------------- Submitted database -------------------------
            if answer == "right":
                self.new_layout = Result(self, database, password=password, AccountType=AccountType.currentText(),
                                         PERMISSIONS=account_permission)
                self.surface.replaceWidget(self.old_layout, self.new_layout)
                self.old_layout.hide()
                self.new_layout.show()

        except Exception as error:
            print(error)

    def BackFunction(self):
        self.surface.replaceWidget(self.new_layout, self.old_layout)
        self.new_layout.hide()
        self.old_layout.show()

    def CreateNew(self):
        self.Refresh()
        self.surface.replaceWidget(self.new_layout, self.old_layout)
        self.new_layout.hide()
        self.old_layout.show()

    def Refresh(self):
        try:
            self.DATABASE["accountType"].setCurrentIndex(0)
            for widget in self.DATABASE["entry"]:
                for field in widget:
                    print(field.text(), end=", ")
                    try:
                        field.setText("")
                    except:
                        field.setDate(QDate.currentDate())
            for permission in self.DATABASE["PERMISSIONS"]:
                permission.setChecked(False)

        except Exception as error:
            print(error)


class PERMISSION(QCheckBox):
    def __init__(self, txt):
        super(PERMISSION, self).__init__()
        self.setStyleSheet(STYLESHEET.PERMISSION())
        self.setText(txt)
        self.setFixedSize(210, 25)
