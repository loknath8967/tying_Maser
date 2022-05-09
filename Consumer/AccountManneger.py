from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Consumer.Accounts import AccountManager
from Consumer.Registration import AccountCreate
from STYLESHEET.AccountManager import STYLESHEET
class TopBar(QGroupBox):
    def __init__(self, LAYOUT):
        super(TopBar, self).__init__()
        self.setFixedHeight(60)
        self.setStyleSheet(STYLESHEET.TopBAR())
        TopLayout = QGridLayout()
        self.setLayout(TopLayout)
        TopLayout.addWidget(QLabel("Account Management"), 0, 0, Qt.AlignLeft)

        ACCOUNTS=QPushButton("Account Manager")
        ACCOUNTS.pressed.connect(lambda: LAYOUT.setCurrentIndex(0))
        ACCOUNTS.setFixedSize(250, 40)
        TopLayout.addWidget(ACCOUNTS, 0, 0, Qt.AlignRight)
        CREATE=QPushButton("Create Account")
        CREATE.pressed.connect(lambda: LAYOUT.setCurrentIndex(1))
        CREATE.setFixedSize(250, 40)
        TopLayout.addWidget(CREATE, 0, 1)

class Layout(QTabWidget):
    def __init__(self):
        super(Layout, self).__init__()
        self.setStyleSheet(STYLESHEET.Layout())
        self.addTab(AccountManager(), "")
        self.addTab(AccountCreate(), "")

class ACCOUNT(QWidget):
    def __init__(self):
        super(ACCOUNT, self).__init__()
        surface=QGridLayout()
        self.setLayout(surface)
        TabView=Layout()
        surface.addWidget(TopBar(TabView), 0, 0)
        surface.addWidget(TabView, 1, 0)