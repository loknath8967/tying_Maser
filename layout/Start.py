from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from STYLESHEET.start import STYLESHEET
class started(QWidget):
    def __init__(self, parent):
        super(started, self).__init__()
        layout = QGridLayout()
        gp_gp = QGroupBox()
        gp_gp.setStyleSheet(STYLESHEET.MAIN())
        gp_lay = QGridLayout()
        gp_gp.setLayout(gp_lay)
        btn_gp = QGroupBox()
        btn_gp.setStyleSheet(STYLESHEET.BUTTON())
        btn_lay = QGridLayout()
        btn_gp.setLayout(btn_lay)
        btn_gp.setFixedSize(130, 120)
        gp_lay.addWidget(btn_gp)
        start = QPushButton('Start')
        start.pressed.connect(parent.exams.emit)
        start.setFixedSize(120, 30)
        login=QPushButton("log In")
        login.pressed.connect(parent.logIn.emit)
        login.setFixedSize(120, 30)

        exits = QPushButton('Quit')
        exits.pressed.connect(lambda: parent.close())
        exits.setFixedSize(120, 30)
        btn_lay.addWidget(start)
        btn_lay.addWidget(login)

        btn_lay.addWidget(exits)
        layout.addWidget(gp_gp)
        self.setLayout(layout)