from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from layout.PyQt import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt, QRect, QSize
from STYLESHEET.Title import STYLESHEET

class ICON(QPushButton):
    def __init__(self):
        super(ICON, self).__init__()
        self.setIcon(QIcon('image/Icon.ico'))
        self.setIconSize(QSize(30, 30))
        self.setText('Typing Test')
        self.setStyleSheet(STYLESHEET.ICON())
   
class GEOMETRY(QPushButton):
    def __init__(self, parent):
        super(GEOMETRY, self).__init__()
        self.setFixedSize(15, 12)
        self.setStyleSheet(STYLESHEET.GEOMETRY())
        try:
            self.pressed.connect(lambda: parent.maxi.emit())
        except Exception as error:
            print(error)


class MAXIMIZATION(QPushButton):
    def __init__(self, parent):
        super(MAXIMIZATION, self).__init__()
        self.setFixedSize(15, 12)
        self.setStyleSheet(STYLESHEET.MAXIMIZATION())
        try:
            self.pressed.connect(lambda: parent.geo.emit())
        except Exception as error:
            print(error)


class MAXIMIZE(QPushButton):
    maxi = pyqtSignal()
    geo = pyqtSignal()
    def __init__(self, parent):
        super(MAXIMIZE, self).__init__()
        self.setFixedSize(40, 25)
        self.parent = parent
        self.layout = QGridLayout()
        self.new = None
        self.old = MAXIMIZATION(self)
        self.layout.addWidget(self.old)
        self.setStyleSheet(STYLESHEET.MINIMIZE())
        try:
            self.maxi.connect(self.max_win)
            self.geo.connect(self.geo_win)
        except Exception as error:
            print(error)
        self.setLayout(self.layout)

    def max_win(self):
        try:
            self.parent.showNormal()
            self.new = MAXIMIZATION(self)
            self.layout.replaceWidget(self.old, self.new)
            self.old.hide()
            self.old = self.new
        except Exception as error:
            print(error)

    def geo_win(self):
        try:

            self.parent.showMaximized()
            self.new = GEOMETRY(self)
            self.layout.replaceWidget(self.old, self.new)
            self.old.hide()
            self.old = self.new
        except Exception as error:
            print(error)


class MINIMIZATION(QPushButton):
    def __init__(self, parent):
        super(MINIMIZATION, self).__init__()
        self.setFixedSize(15, 5)
        self.setStyleSheet(STYLESHEET.MINIMIZATION())

        self.pressed.connect(lambda: parent.showMinimized())


class MINIMIZE(QPushButton):
    def __init__(self, parent):
        super(MINIMIZE, self).__init__()
        self.setFixedSize(40, 25)
        layout = QGridLayout()
        layout.addWidget(MINIMIZATION(parent), *(0, 0), Qt.AlignCenter)
        self.setStyleSheet(STYLESHEET.MINIMIZE())

        self.pressed.connect(lambda: parent.showMinimized())
        self.setLayout(layout)


class CLOSE(QPushButton):
    def __init__(self, parent):
        super(CLOSE, self).__init__()
        self.setFixedSize(40, 25)
        self.setText('X')
        self.setStyleSheet(STYLESHEET.CLOSE())
        self.pressed.connect(lambda: parent.close())


class Title(QWidget):
    def __init__(self, parent):
        super(Title, self).__init__()
        self.setFixedHeight(30)
        self.setStyleSheet(STYLESHEET.TITLE())
        layout = QGridLayout()
        layout.addWidget(MINIMIZE(parent), *(0, 1), Qt.AlignRight)
        layout.addWidget(MAXIMIZE(parent), *(0, 2))
        layout.addWidget(CLOSE(parent), *(0, 3))
        self.setLayout(layout)

