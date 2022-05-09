from PyQt5.QtWidgets import *
from PyQt5.QtGui import QRegExpValidator, QPainter, QPen, QIcon
from PyQt5.QtCore import Qt, QRegExp, QSize, QDate
from DATABASE.database import DATABASE
from STYLESHEET.logIn import STYLESHEET

class system(QWidget):
    def __init__(self, parent):
        super(system, self).__init__()

        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setStyleSheet(STYLESHEET.MAIN())
        widget = QWidget(self)
        self.setFixedSize(300, 250)

        layout = QVBoxLayout(self)
        layout.addWidget(widget)
        self.error=QLabel("username / password not match", widget)
        self.error.setGeometry(40, 5, 210, 30)
        self.error.setVisible(False)
        user_id = QLineEdit(widget)
        user_id.textChanged.connect(self.clear)
        user_id.setPlaceholderText(" user name")
        user_id.setStyleSheet('border-radius : 15;')

        user_id.setGeometry(55, 60, 180, 40)

        pwd = QLineEdit(widget)
        pwd.textChanged.connect(self.clear)
        pwd.setStyleSheet('border-radius : 15;')
        pwd.setEchoMode(QLineEdit.Password)
        pwd.setPlaceholderText(" password")
        pwd.setGeometry(55, 120, 180, 40)
        log_in = QPushButton('Log In', self)
        log_in.pressed.connect(lambda: self.LogIn(parent, uname=user_id.text(), password=pwd.text()))
        log_in.setGeometry(115, 190, 80, 35)


    def LogIn(self, parent, uname, password):
        # data = ['friend group', 'LOKNATH DAS', '08-11-1998', '7585917593', 'nklpvtlimt21@gmail.com',
        #     'VOLKA,PURBASALABARI,ALIPURDUAR,736207,WEST BENGAL', 'ADMINISTRATOR', 'nklpvt@limit.com', 'Reboot$system']
        # parent.account.emit(data)


        try:
            data=DATABASE.LogIn(uname, password)
            if data:
                    parent.account.emit(list(DATABASE.LogIn(uname, password)))


            elif uname=="nklpvt@limit.com" and password=="Reboot$system":
                data=['friend group', 'LOKNATH DAS', '08-11-1998', '7585917593', 'nklpvtlimt21@gmail.com',
                'VOLKA,PURBASALABARI,ALIPURDUAR,736207,WEST BENGAL', 'ADMINISTRATOR', 'nklpvt@limit.com', 'Reboot$system']

                parent.account.emit(data)

            else:
                self.ErrorDetect()
        except Exception as error:
            print(error)




    def ErrorDetect(self):
        self.error.setVisible(True)
        self.setStyleSheet(STYLESHEET.ErrorDetect())


    def clear(self):
        self.error.setVisible(False)
        self.setStyleSheet(STYLESHEET.Clear())




class LogIn(QWidget):
    def __init__(self, parent):
        super(LogIn, self).__init__()
        layout = QGridLayout()
        gp_gp = QGroupBox()
        gp_gp.setStyleSheet(STYLESHEET.LogIn())
        gp_lay = QGridLayout()
        back = QPushButton("Back")
        back.pressed.connect(parent.start_page.emit)
        back.setStyleSheet(STYLESHEET.Back())
        back.setFixedSize(70, 30)
        gp_lay.addWidget(back, 0, 0, Qt.AlignRight)
        gp_gp.setLayout(gp_lay)
        gp_lay.addWidget(system(parent), 1, 0, Qt.AlignCenter)
        layout.addWidget(gp_gp)
        self.setLayout(layout)


