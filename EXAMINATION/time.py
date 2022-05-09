from PyQt5.QtCore import QTimer, QDateTime

class time(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(150, 50)
        self.setStyleSheet('''
        background-color:red;
        border-radius:10px;
        color:white;

        border-style:hidden;font-size:21px; 
                font-family: "Comic Sans MS";''')
        self.timer = QTimer()
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)
        layout = QGridLayout()
        self.label = QLabel('HH:MM:SS')
        layout.addWidget(self.label, *(0, 0), Qt.AlignRight)
        self.setLayout(layout)

    def showTime(self):
        time = QDateTime.currentDateTime()
        timeDisplay = time.toString('hh:mm:ss')
        self.label.setText(timeDisplay)


class Time(QPushButton):
    def __init__(self, Txt, display):
        super(Time, self).__init__()
        self.setText(Txt)
        self.pressed.connect(lambda: display.setVisible(False) if display.isVisible() else display.setVisible(True))
        self.setStyleSheet('''
        background-color:green;
        border:2px solid green;
        border-radius:10px;
        border-style:hidden;font-size:15px; 
        font-family: "Comic Sans MS";''')
        self.setFixedSize(70, 30)
