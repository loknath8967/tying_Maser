from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
# from STYLESHEET.Result import STYLESHEET
import sys
class Sign(QLabel):
    def __init__(self):
        super(Sign, self).__init__()
        self.setFixedHeight(45)
        self.setText('....................................\nSignature    ')
        self.setAlignment(Qt.AlignHCenter)
        self.setStyleSheet('''font-family: "Lucida Handwriting" ; border:1px hidden;
        color:blue; font-size:15px;''')


class signature(QLabel):
    def __init__(self, sign):
        super(signature, self).__init__()
        if sign=="L.Das" or sign=="SYSTEM":
            self.setText(" L.Das ")
        else:

            try:
                name = sign.split(" ")
                if len(name) > 1:
                    self.setText(f''' {name[0][0]}.{name[len(name) - 1].capitalize()} ''')
                else:
                    self.setText(f' {name[0][0]}{name[0][1]}{name[0][2]} ')
            except:
              pass

        self.setFixedHeight(30)
        self.setAlignment(Qt.AlignHCenter)
        self.setStyleSheet(''' font-family:"Brush Script MT";
           color:blue;   font-size:15px;  border:1px hidden;''')



class HOD(QLabel):
    def __init__(self, sign):
        super(HOD, self).__init__()
        if sign=="L.Das" or sign=="SYSTEM":
            self.setText("L.Das")
        else:

            try:
                name = sign.split(" ")
                if len(name) > 1:
                    self.setText(f'''{name[0][0]}.{name[len(name) - 1].capitalize()}''')
                else:
                    self.setText(f'{name[0][0]}{name[0][1]}{name[0][2]}')
            except:
              pass

        self.setFixedHeight(30)
        self.setAlignment(Qt.AlignHCenter)
        self.setStyleSheet(''' font-family:"Brush Script MT"; border:1px hidden;
           color:blue;   font-size:25px;''')
class Incharge(QWidget):
    def __init__(self, sign):
        super(Incharge, self).__init__()
        self.setFixedSize(190, 90)
        layout=QGridLayout()
        if sign=="SYSTEM":
            sign="L.Das"

        layout.addWidget(Sign(), *(0, 0), Qt.AlignBottom)
        layout.addWidget(HOD(sign), *(0, 0), Qt.AlignTop)
        self.setLayout(layout)

