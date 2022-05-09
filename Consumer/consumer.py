from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Consumer.profile import profile
from Consumer.Questions import QPAPER
from Consumer.QuestionEntry import QENTRY
from Consumer.MARKSHEET import Marksheet
from Consumer.AccountManneger import ACCOUNT
from Consumer.CreateDataBase import CreateDataBase
from STYLESHEET.consumer import STYLESHEET

class TabView(QTabWidget):
    def __init__(self, info):
        super(TabView, self).__init__()
        self.setStyleSheet(STYLESHEET.TabView())
        self.addTab(profile(info), "")
        self.addTab(QPAPER(), "")
        self.addTab(QENTRY(info[0]), "")
        self.addTab(Marksheet(), "")
        self.addTab(ACCOUNT(), "")
        self.addTab(CreateDataBase(), "")

class Button(QPushButton):
    def __init__(self, txt):
        super(Button, self).__init__()
        self.setText(txt)
        self.setStyleSheet(STYLESHEET.Button())

class Management(QWidget):
    def __init__(self, parent, info):
        super(Management, self).__init__()
        self.setStyleSheet(STYLESHEET.Management())
        Maintenance = QGridLayout()
        self.setLayout(Maintenance)
        Tab = TabView(info)

        # ----------             ----------------------------------
        Maintenance.addWidget(Tab, 0, 1)
        # ---------- left side   ---------------------------------
        left_gp = QGroupBox()
        left_gp.setFixedWidth(250)
        left_page = QFormLayout()
        left_gp.setLayout(left_page)
        Maintenance.addWidget(left_gp, 0, 0)

        # --------------------left side item s----------------------------------
        profile_btn = Button("PROFILE")
        profile_btn.pressed.connect(lambda: Tab.setCurrentIndex(0))
        left_page.addWidget(profile_btn)
        Question_btn = Button("QUESTION PAPER")
        Question_btn.pressed.connect(lambda: Tab.setCurrentIndex(1))
        left_page.addWidget(Question_btn)

        Entry_btn = Button("QUESTION INSERT")
        Entry_btn.pressed.connect(lambda: Tab.setCurrentIndex(2))
        left_page.addWidget(Entry_btn)

        MarkSheet_btn = Button("MARKSHEET DISPLAY")
        MarkSheet_btn.pressed.connect(lambda: Tab.setCurrentIndex(3))
        left_page.addWidget(MarkSheet_btn)
        #
        Account_btn = Button("ACCOUNT MANAGER")
        Account_btn.pressed.connect(lambda: Tab.setCurrentIndex(4))

        DataBase_btn = Button("DATABASE")
        DataBase_btn.pressed.connect(lambda: Tab.setCurrentIndex(5))

        if info[6]=="ADMINISTRATOR":
            left_page.addWidget(Account_btn)
            left_page.addWidget(DataBase_btn)
        log_out = Button("LOG OUT")
        log_out.setStyleSheet(STYLESHEET.LogOut())
        log_out.pressed.connect(parent.logIn.emit)
        left_page.addWidget(log_out)


