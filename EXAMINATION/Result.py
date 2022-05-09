from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from DATABASE.database import DATABASE
from STYLESHEET.Result import STYLESHEET
from Incharge.signature import Incharge
class CreateResult(QWidget):
    def __init__(self, parent, SNO, Quiz, answer, time):
        super(CreateResult, self).__init__()
        self.setStyleSheet(STYLESHEET.MAIN())
        layout = QGridLayout()
        Questions = DATABASE.Question(Quiz)
        wrong_answer = 0
        right_answer = 0
        word = 0
        try:
            for ans in answer:

                if ans == Questions[answer.index(ans)]:
                    right_answer += 1
                else:
                    wrong_answer += 1

            for num in answer.split(' '):
                if num != ' ' or num != '.' or num != ',':
                    word += 1
            speed = f'{word} words in {float(int(time)/60)} minutes'
            MARKS = "{:.2f}".format(((len(answer) - wrong_answer) / len(Questions)) * 100)
            if float(MARKS) >= float(DATABASE.PassMark(Quiz)):
                DATABASE.RESULT(Quiz)
                layout.addWidget(MarkSheet(parent, Quiz, "PASSED", MARKS, wrong_answer, speed))
            else:
                layout.addWidget(MarkSheet(parent, Quiz, "FIELD", MARKS, wrong_answer, speed))
            c_time = QDateTime.currentDateTime().toString('hh:mm:ss')
            DATABASE.ExamComplete(SNO, MARKS, wrong_answer, speed, c_time)

        except Exception:
            pass
        self.setLayout(layout)


class Item(QLabel):
    def __init__(self, TxT):
        super(Item, self).__init__()
        self.setText(TxT)
        self.setStyleSheet(STYLESHEET.ITEM())


class marks(QLabel):
    def __init__(self, TxT):
        super(marks, self).__init__()
        self.setText(str(TxT))
        self.setStyleSheet(STYLESHEET.MARKS())


class Result(QLabel):
    def __init__(self, result):
        super(Result, self).__init__()
        if result == "PASSED":
            self.setText('!!! Congratulation !!!\n !! You Are Complete Your Examination !!')
            self.setStyleSheet(STYLESHEET.PASSED())
        else:
            self.setText('!!! SORRY !!!\n !! You Are Not Illegible For Next Examination !!')
            self.setStyleSheet(STYLESHEET.FAILED())
        self.setAlignment(Qt.AlignCenter)


class MarkSheet(QWidget):
    switch = pyqtSignal()

    def __init__(self, parent, Question, result, MARKS, wrong_answer, speed):
        super(MarkSheet, self).__init__()
        self.setFixedSize(550, 490)
        lay_win = QGridLayout()
        self.setStyleSheet(STYLESHEET.MARKSHEET())

        gp_gp = QGroupBox()
        lay_win.addWidget(gp_gp)
        layout = QGridLayout()
        gp_gp.setLayout(layout)
        gp_gp.setStyleSheet(STYLESHEET.MARKSHEET_GP())
        layout.addWidget(Result(result), *(0, 0), Qt.AlignCenter)
        gp = QGroupBox()
        gp.setStyleSheet(STYLESHEET.MARKSHEET_GP())
        layout1 = QFormLayout()
        gp.setLayout(layout1)
        layout.addWidget(gp, *(1, 0), Qt.AlignCenter)
        layout1.addRow(Item(f'Complete'), marks(f'  :  {MARKS}'))
        layout1.addRow(Item('wrong answer'), marks(f' :    {wrong_answer} latter is wrong'))
        layout1.addRow(Item('typing speed'), marks(f':    {speed}'))
        layout1.addWidget(QLabel('\n\n\n'))
        sign_gp = QGroupBox()
        sign_gp.setStyleSheet(STYLESHEET.SIGN())
        # sign_gp.setFixedHeight(110)
        layout1.addWidget(sign_gp)
        sign_l = QGridLayout()
        sign_l.addWidget(Incharge(DATABASE.Incharge(Quiz=Question)))
        sign_gp.setLayout(sign_l)
        btn_gp = QGroupBox()
        btn_gp.setStyleSheet(STYLESHEET.MARKSHEET_BTN())
        btn_gp.setFixedHeight(50)
        btn_layout = QGridLayout()
        btn_gp.setLayout(btn_layout)
        next_Exam = QPushButton('Next Exam')
        next_Exam.pressed.connect(lambda: MarkSheet.next_exam(parent, Question))
        next_Exam.setFixedSize(130, 40)
        retry_Exam = QPushButton('Retry Exam')
        retry_Exam.setFixedSize(130, 40)
        retry_Exam.pressed.connect(lambda: parent.exam_paper.emit(Question))
        if DATABASE.last_Quiz(Question) is False and result == "PASSED":
            btn_layout.addWidget(next_Exam, *(0, 0), Qt.AlignRight)
        else:
            btn_layout.addWidget(retry_Exam, *(0, 0), Qt.AlignRight)
        main_menu = QPushButton('Main menu')
        main_menu.pressed.connect(parent.start_page.emit)
        main_menu.setFixedSize(130, 40)
        btn_layout.addWidget(main_menu, *(0, 1))
        lay_win.addWidget(btn_gp, *(2, 0), Qt.AlignRight)
        self.setLayout(lay_win)

    @staticmethod
    def next_exam(parent, Question):
        try:
            Quiz = DATABASE.next_Quiz(Question)
            parent.exam_paper.emit(Quiz)
        except Exception:
            pass