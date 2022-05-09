import sys, sqlite3, os, shutil
from datetime import datetime
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import *
from PyQt5.QtCore import Qt, QRect, QSize
from layout.PyQt import MainLayout
from layout.Titile import CLOSE, MAXIMIZE, ICON, MINIMIZE
from layout.Start import started
from layout.login import LogIn
from EXAMINATION.Exampaper import Exams
from EXAMINATION.QuesrionPaper import QuestionPaper
from EXAMINATION.Result import CreateResult
from Consumer.consumer import Management
from STYLESHEET.MAIN import STYLESHEET
class MAIN_WINDOW(QWidget):
    exams = pyqtSignal()
    start_page = pyqtSignal()
    exam_paper = pyqtSignal(str)
    result = pyqtSignal(int, str, str, str)
    logIn=pyqtSignal()
    account=pyqtSignal(list)

    def __init__(self):
        super(MAIN_WINDOW, self).__init__()
        self.oldPos = None
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.new_page = None
        self.setGeometry(250, 250, 650, 550)
        self.setStyleSheet(STYLESHEET.MAIN())
        self.layout = QGridLayout()
        title_gp = QGroupBox()
        self.layout.addWidget(title_gp)
        title_lay = QGridLayout()
        title_gp.setFixedHeight(50)
        title_gp.setLayout(title_lay)
        title_lay.addWidget(ICON(), *(0, 0), Qt.AlignLeft)
        title_lay.addWidget(MINIMIZE(self), *(0, 2), Qt.AlignRight)
        title_lay.addWidget(MAXIMIZE(self), *(0, 3))
        title_lay.addWidget(CLOSE(self), *(0, 4))

        main_gp = QGroupBox()
        main_gp.setStyleSheet(STYLESHEET.GroupBox())

        self.main_l = QGridLayout()
        main_gp.setLayout(self.main_l)
        try:
            self.exams.connect(self.exam_page)
            self.start_page.connect(self.starting_page)
            self.exam_paper.connect(self.examination)
            self.result.connect(self.Result)
            self.logIn.connect(self.SystemLogin)
            self.account.connect(self.Consumer)
        except Exception:
            pass
        self.old_page = started(self)
        self.main_l.addWidget(self.old_page)
        self.layout.addWidget(main_gp)
        self.setLayout(self.layout)

    def exam_page(self):
        try:
            self.new_page = Exams(self)
            self.main_l.replaceWidget(self.old_page, self.new_page)
            self.old_page.hide()
            self.new_page.show()
            self.old_page = self.new_page
        except Exception as error:
            print(error)


    def starting_page(self):
        self.new_page = started(self)
        self.main_l.replaceWidget(self.old_page, self.new_page)
        self.old_page.hide()
        self.new_page.show()
        self.old_page = self.new_page

    def examination(self, Quiz):
        try:
            self.new_page = QuestionPaper(self, Quiz)
            self.main_l.replaceWidget(self.old_page, self.new_page)
            self.old_page.hide()
            self.new_page.show()
            self.old_page = self.new_page
        except Exception:
            pass

    def Result(self, SNO, Quiz, answer, time):
        try:
            self.new_page = CreateResult(self, SNO, Quiz, answer, time)
            self.main_l.replaceWidget(self.old_page, self.new_page)
            self.old_page.hide()
            self.new_page.show()
            self.old_page = self.new_page
        except Exception:
            pass

    def SystemLogin(self):
        try:
            self.new_page = LogIn(self)
            self.main_l.replaceWidget(self.old_page, self.new_page)
            self.old_page.hide()
            self.new_page.show()
            self.old_page = self.new_page
        except Exception as error:
            print(error)


    def Consumer(self, info):
        try:
            self.new_page = Management(self, info)
            self.main_l.replaceWidget(self.old_page, self.new_page)
            self.old_page.hide()
            self.new_page.show()
            self.old_page = self.new_page
        except Exception as error:
            print(error)



    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MAIN_WINDOW()
    w.setWindowTitle("Typing Test")

    w.show()
    sys.exit(app.exec_())