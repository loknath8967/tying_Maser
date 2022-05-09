from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from DATABASE.database import DATABASE
from STYLESHEET.MARKSHEET import STYLESHEET
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


class Marksheet(QWidget):
    def __init__(self):
        super(Marksheet, self).__init__()

        SHEET=DATABASE.MarkSheet()
        layout = QGridLayout()
        Label = QLabel('MARKSHEET')
        Label.setFixedHeight(35)
        Label.setStyleSheet(STYLESHEET.MarkSheet())
        layout.addWidget(Label, 0, 0, Qt.AlignHCenter)
        if SHEET=="Data Not Found !!":
            layout.addWidget(Empty(SHEET), 1, 0, Qt.AlignHCenter)
        else:
            layout.addWidget(Table(SHEET[0], SHEET[1], len(SHEET[1]), len(SHEET[0])))
        self.setLayout(layout)