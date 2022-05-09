from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from DATABASE.database import DATABASE
from STYLESHEET.Questions import STYLESHEET
class Table(QTableWidget):
    def __init__(self, header, DBMS, *args):
        super(Table, self).__init__(*args)
        self.setStyleSheet(STYLESHEET.Table())
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setHorizontalHeaderLabels(header)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.setData(DBMS)

    def setData(self, DBMS):
        for row, db in enumerate(DBMS):
            for column, item in enumerate(list(db)):
                self.setItem(row, column, QTableWidgetItem(str(item)))

class Empty(QLabel):
    def __init__(self, txt):
        super(Empty, self).__init__()
        self.setText(txt)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet(STYLESHEET.Empty())
class QPAPER(QWidget):
    def __init__(self):
        super(QPAPER, self).__init__()

        QUESTION=DATABASE.QuestionPaper()
        layout = QGridLayout()
        Label = QLabel('QUESTION PAPER')
        Label.setFixedHeight(35)
        Label.setStyleSheet(STYLESHEET.QPAPER())
        layout.addWidget(Label, 0, 0, Qt.AlignHCenter)
        if QUESTION=="Data Not Found !!":
            layout.addWidget(Empty(QUESTION), 1, 0, Qt.AlignHCenter)
        else:
            layout.addWidget(Table(QUESTION[0], QUESTION[1], len(QUESTION[1]), len(QUESTION[0])))
        self.setLayout(layout)


        self.setLayout(layout)