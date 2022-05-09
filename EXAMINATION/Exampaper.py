from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from DATABASE.database import DATABASE
from layout.PyQt import MainLayout
from STYLESHEET.Exampaper import STYLESHEET
class UNLOCK(QPushButton):
    def __init__(self, parent, txt):
        super(UNLOCK, self).__init__()
        self.setText(txt)
        self.setStyleSheet(STYLESHEET.UNLOCK())

        try:
            self.pressed.connect(lambda txt=txt: parent.exam_paper.emit(str(txt)))
        except Exception:
            pass


class LOCK(QPushButton):
    def __init__(self, txt):
        super(LOCK, self).__init__()
        self.setText(txt)
        self.setStyleSheet(STYLESHEET.LOCK())
        self.setDisabled(True)


class Exams(QWidget):
    def __init__(self, parent):
        super(Exams, self).__init__()
        self.setStyleSheet(STYLESHEET.Exams())
        layout = QGridLayout()
        back = QPushButton("Back")
        back.setStyleSheet(STYLESHEET.Back())
        back.pressed.connect(parent.start_page.emit)
        back.setFixedSize(90, 30)
        layout.addWidget(back, *(0, 0), Qt.AlignRight)
        main_gp = QGroupBox()
        main_gp.setStyleSheet(STYLESHEET.Exams_Gp())
        main_l = MainLayout()
        main_gp.setLayout(main_l)
        try:
            for Quiz, status in DATABASE.QuestionNumber():
                if status == 'UNLOCK':
                    main_l.addWidget(UNLOCK(parent, Quiz))
                elif status == 'LOCK':
                    main_l.addWidget(LOCK(Quiz))
        except Exception:
            pass
        layout.addWidget(main_gp)
        self.setLayout(layout)
