from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from DATABASE.database import DATABASE
from STYLESHEET.QuestionPaper import STYLESHEET
class time(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(150, 50)
        self.setStyleSheet(STYLESHEET.MAIN())
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
        self.setStyleSheet(STYLESHEET.Button())
        self.setFixedSize(70, 30)

class Question(QScrollArea):
    def __init__(self, Quiz):
        super(Question, self).__init__()
        self.setWidgetResizable(True)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Quiz=Quiz
        self.Paper=QLabel(self.Quiz)
        self.Paper.setWordWrap(True)
        self.Paper.setStyleSheet('''background-color:white; font-size:21px; color: gray; padding:10px; ''')
        self.Paper.setAlignment(Qt.AlignTop)
        self.setWidget(self.Paper)


    def completed(self, ans):
        Quiz = list(self.Quiz)
        for i in range(len(ans)):
            if Quiz[i] == ans[i]:
                Quiz[i] = f'<font color="black">{Quiz[i]}</font>'
            else:
                Quiz[i] = f'<font style="background-color:red; color: black;">{Quiz[i]}</font>'

        self.Paper.setText("".join(Quiz))

class AnswerBox(QTextEdit):
    def __init__(self,  Question):
        super(AnswerBox, self).__init__()
        self.Paper = Question
        self.setStyleSheet("font-size: 18px;")
        self.widget.installEventFilter(self)
        self.setContextMenuPolicy(False)

    @property
    def widget(self):
        return self
    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress:
            if event.matches(QKeySequence.Copy) or event.matches(QKeySequence.Paste) or event.matches(QKeySequence.SelectAll):
                return True
        return super().eventFilter(obj, event)
    def dragEnterEvent(self, e: QDragEnterEvent) -> None:
        pass
    def dropEvent(self, e: QDropEvent) -> None:
        pass
    def mouseMoveEvent(self, e: QMouseEvent) -> None:
        pass
    def mouseDoubleClickEvent(self, e: QMouseEvent) -> None:
        pass

    def keyPressEvent(self, event: QKeyEvent) -> None:
        try:

            if len(self.Paper.Quiz) > len(self.toPlainText()):
                super(AnswerBox, self).keyPressEvent(event)
                self.Paper.completed(self.toPlainText())

            elif event.key() == Qt.Key_Backspace:
                self.setReadOnly(False)
                super(AnswerBox, self).keyPressEvent(event)

            else:
                self.setReadOnly(True)
        except Exception as error:
            print(error)

class QuestionPaper(QWidget):
    def __init__(self, parent, Quiz):
        super(QuestionPaper, self).__init__()
        self.second = 0
        self.SNO = None
        self.setGeometry(350, 350, 350, 350)
        self.HH = 00
        self.MM = 00
        self.SS = 00
        self.time_left_int = 0
        layout = QGridLayout()
        display_gp = QGroupBox()
        wind = QGridLayout()
        title_gp = QGroupBox()
        title_gp.setStyleSheet(STYLESHEET.Title())
        title_lay = QGridLayout()
        title_gp.setLayout(title_lay)
        display = Question(DATABASE.Question(Quiz))
        title_lay.addWidget(Time(Quiz, display), *(1, 0), Qt.AlignLeft)
        title_lay.addWidget(time(), *(1, 1), Qt.AlignRight)
        wind.addWidget(title_gp, *(1, 0), Qt.AlignTop)
        display.setStyleSheet(STYLESHEET.Display())
        wind.addWidget(display, *(2, 0))

        display_gp.setLayout(wind)
        editor = AnswerBox(display)
        editor.setStyleSheet(STYLESHEET.Editor())
        editor.textChanged.connect(lambda: self.avg(parent, Quiz, editor))
        editor.setReadOnly(True)
        wind.addWidget(editor)
        layout.addWidget(display_gp, *(3, 0))
        result_gp = QGroupBox()
        result_gp.setStyleSheet(STYLESHEET.Result())
        result_gp.setFixedHeight(80)
        result_layout = QGridLayout()
        self.complete = QLabel('0%')
        result_gp.setLayout(result_layout)
        # ------------=-----------timer ----------------------------------
        self.stopwatch = QLabel(f'{str(self.HH).zfill(2)}:{str(self.MM).zfill(2)}:'
                                f'{str(self.SS).zfill(2)}:{str(self.time_left_int).zfill(2)}')
        timer = QTimer(self)
        timer.timeout.connect(self.timer_timeout)
        # -------------=----------timer-----------------------------
        start = QPushButton('start')

        start.setMaximumSize(90, 30)
        result_layout.addWidget(start, *(0, 2), Qt.AlignRight)

        submit = QPushButton('submit')
        submit.setStyleSheet('background-color:gray;')
        try:
            start.pressed.connect(lambda: self.starter(timer, Quiz, start, editor, submit))
            submit.pressed.connect(lambda: self.submit(parent, Quiz, editor))
        except Exception:
            pass
        submit.setDisabled(True)
        submit.setMaximumSize(90, 30)
        result_layout.addWidget(submit, *(0, 4))
        result_layout.addWidget(self.stopwatch, *(0, 5), Qt.AlignRight)
        result_layout.addWidget(self.complete, *(0, 1), Qt.AlignLeft)
        layout.addWidget(result_gp, *(4, 0))
        self.setLayout(layout)

    def avg(self, parent, Quiz, editor):
        avg = "{:.2f}".format((len(editor.toPlainText()) / len(DATABASE.Question(Quiz))) * 100)
        self.complete.setText(f'{avg} %')
        if len(editor.toPlainText()) >= len(DATABASE.Question(Quiz)):
            self.submit(parent, Quiz, editor)

    def starter(self, timer, Quiz, start, editor, submit):
        try:
            timer.start(100)
            editor.setReadOnly(False)
            submit.setDisabled(False)
            submit.setStyleSheet('''background-color:blue;''')
            start.setDisabled(True)
            start.setStyleSheet('''background-color:gray;''')
            c_time = QDateTime.currentDateTime().toString('hh:mm:ss')
            self.SNO = DATABASE.ExamStart(Quiz, c_time, datetime.now().strftime("%d-%m-%Y"))
        except Exception:
            pass

    def timer_timeout(self):
        self.time_left_int += 1
        if self.time_left_int == 10:
            self.SS += 1
            self.second += 1
            self.time_left_int = 0
        if self.SS == 59:
            self.MM += 1
            self.SS = 0
            self.time_left_int = 0
        if self.MM == 59:
            self.HH += 1
            self.MM = 0
            self.time_left_int = 0
        self.update_gui()

    def update_gui(self):
        self.stopwatch.setText(f'{str(self.HH).zfill(2)}:{str(self.MM).zfill(2)}:'
                               f'{str(self.SS).zfill(2)}:{str(self.time_left_int).zfill(2)}')

    def submit(self, parent, Quiz, editor):
        MessageBox = QMessageBox(self)
        MessageBox.setText('\n\n \t  Conformation \n Message For Submit Answer Script\t   \n\n')
        submitBtn = MessageBox.addButton('Submit', QMessageBox.YesRole)
        cancelBtn = MessageBox.addButton(' No', QMessageBox.RejectRole)
        MessageBox.setWindowIcon(QIcon('image/Icon.ico'))
        MessageBox.setWindowTitle('Typing Test')
        submitBtn.setStyleSheet(STYLESHEET.MsgSubmit())
        cancelBtn.setStyleSheet(STYLESHEET.MsgCancel())
        MessageBox.setStyleSheet(STYLESHEET.MsgBox())

        MessageBox.exec_()

        if MessageBox.clickedButton() == submitBtn:
            try:
                parent.result.emit(self.SNO, Quiz, editor.toPlainText(), str(self.second))
            except Exception:
                pass
        elif MessageBox.clickedButton() == cancelBtn:
            pass
        else:
            pass