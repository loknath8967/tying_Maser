from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from DATABASE.database import DATABASE
from STYLESHEET.CreateDataBase import STYLESHEET
class Result(QWidget):
    def __init__(self, parent):
        super(Result, self).__init__()
        layout=QGridLayout()
        try:
            result=DATABASE.CreateDataBase()
            if result=='successful':
                notice=QLabel(''' You`r database successfully created !!''')
                notice.setStyleSheet(STYLESHEET.Success())
            elif result== 'overwrite':
                notice = QLabel(''' You are not able to create database !! \n\n Because same database already here..........''')
                notice.setStyleSheet(STYLESHEET.Error())
            else:
                notice=QLabel(f''' You are not able to create database !! \n\n\n{result}''')
                notice.setStyleSheet(STYLESHEET.Error())
        except Exception as error:
            notice = QLabel(f''' You are not able to create database !! \n\n\n{str(error)}''')
            notice.setStyleSheet(STYLESHEET.Error())
        notice.setFixedHeight(90)
        layout.addWidget(notice, 0, 0, Qt.AlignHCenter)
        back=QPushButton("Back")
        back.pressed.connect(parent.back.emit)
        back.setFixedSize(120, 30)
        layout.addWidget(back, 1, 0, Qt.AlignBaseline)
        self.setLayout(layout)

class Header(QLabel):
    def __init__(self):
        super(Header, self).__init__()
        self.setFixedHeight(30)
        self.setText("!! Default Database creating........ !!")
        self.setStyleSheet('''background-color:blue; color:white;''')
        self.setAlignment(Qt.AlignCenter)
class Information(QLabel):
    def __init__(self):
        super(Information, self).__init__()
        self.setText('''
                \n1.System Create QuestionPaper Table......
                \n2.System Crate MarkSheet Table.....\n
                \n3.System Crate AccountDataBase Table.....\n
                and
                \n3.System Insert 30 Questions also.....\n
                ''')

        self.setAlignment(Qt.AlignLeft)
class CreateDataBase(QWidget):
    back=pyqtSignal()
    def __init__(self):
        super(CreateDataBase, self).__init__()
        self.newLayout=None
        self.oldLayout=None
        self.Layout=QGridLayout()
        Frame=QGroupBox()
        Frame.setFixedSize(510, 510)
        self.oldLayout=Frame
        Frame_layout=QGridLayout()
        Frame.setLayout(Frame_layout)
        self.Layout.addWidget(Frame)
        #_--------------------------------------
        information_gp=QGroupBox()
        information_gp.setFixedHeight(310)

        info_layout=QGridLayout()
        information_gp.setLayout(info_layout)
        #--------------------------------------------

        Frame_layout.addWidget(Header(), 0, 1, Qt.AlignHCenter)
        Frame_layout.addWidget(information_gp, 2, 1, Qt.AlignHCenter)
        info_layout.addWidget(Information())


        #------------------------------------------------

        create=QPushButton("create DataBase")
        create.setFixedSize(190, 35)
        create.pressed.connect(lambda: self.complete(Result(self)))
        Frame_layout.addWidget(create, 5, 1,  Qt.AlignRight)
        Frame_layout.addWidget(QLabel(), 6, 1, Qt.AlignTop)
        self.setLayout(self.Layout)
        self.back.connect(self.Back)

    def complete(self, widget):
        self.newLayout = widget
        self.Layout.replaceWidget(self.oldLayout, self.newLayout)
        self.oldLayout.hide()
        self.newLayout.show()


    def Back(self):
        self.Layout.replaceWidget(self.newLayout, self.oldLayout)
        self.oldLayout.show()
        self.newLayout.hide()
