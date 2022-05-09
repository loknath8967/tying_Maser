from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from DATABASE.database import DATABASE
from STYLESHEET.QuestionEntry import STYLESHEET
from Incharge.signature import signature, Incharge


class Item(QLabel):
	def __init__(self, TxT):
		super(Item, self).__init__()
		self.setText(TxT)
		self.setStyleSheet(STYLESHEET.ITEM())


class VALUE(QLabel):
	def __init__(self, TxT):
		super(VALUE, self).__init__()
		self.setText(TxT)
		self.setStyleSheet(STYLESHEET.VALUE())


class NewQuestion(QWidget):
	def __init__(self, parent, QNO, QUIZ, PMark, sign):
		super(NewQuestion, self).__init__()

		lay_win = QGridLayout()
		self.setStyleSheet(STYLESHEET.NewQuestion())
		gp_gp = QGroupBox()
		gp_gp.setFixedSize(530, 520)
		lay_win.addWidget(gp_gp)
		layout = QGridLayout()
		gp_gp.setLayout(layout)
		# ---------------------
		# ----------------
		HeaderStatus = QLabel("!!! Congratulation !!!\n !! New Question successfully Inserted !!!")
		HeaderStatus.setFixedWidth(510)
		HeaderStatus.setAlignment(Qt.AlignCenter)
		HeaderStatus.setStyleSheet(STYLESHEET.HeaderStatus())

		layout.addWidget(HeaderStatus, 0, 0, 0, 3, Qt.AlignTop)
		#
		gp = QGroupBox()
		gp.setStyleSheet(STYLESHEET.NewQuestion_gp())
		layout1 = QFormLayout()
		gp.setLayout(layout1)

		# ====================
		layout.addWidget(gp, 4, 0, 4, 5, Qt.AlignHCenter)

		layout1.addRow(Item('QNO : '), VALUE(f"TEST {str(QNO)}"))
		layout1.addRow(Item('Quiz Size : '), VALUE(f'{str(QUIZ)} Words'))
		layout1.addRow(Item('Pass Mark : '), VALUE(str(PMark)))

		btn_gp = QGroupBox()
		btn_gp.setStyleSheet(STYLESHEET.BTN_Gp())
		btn_gp.setFixedHeight(120)
		btn_layout = QGridLayout()
		btn_layout.addWidget(Incharge(sign), 0, 0, Qt.AlignRight)
		btn_gp.setLayout(btn_layout)
		NewEntry = QPushButton("Insert New Question")
		NewEntry.pressed.connect(parent.Back.emit)
		NewEntry.setStyleSheet(STYLESHEET.Insert())
		NewEntry.setFixedSize(210, 30)
		btn_layout.addWidget(NewEntry, 1, 0, Qt.AlignLeft)

		layout.addWidget(btn_gp, 6, 0, 6, 4, Qt.AlignBottom)
		self.setLayout(lay_win)


class QUESTION(QTextEdit):
	def __init__(self):
		super(QUESTION, self).__init__()
		self.setStyleSheet(STYLESHEET.QUESTION())


class TopBar(QGroupBox):
	def __init__(self):
		super(TopBar, self).__init__()
		self.setFixedHeight(50)
		self.setStyleSheet(STYLESHEET.TopBar())
		layout=QGridLayout()
		self.setLayout(layout)
		self.NUMBER=QLabel()
		self.NUMBER.setStyleSheet(STYLESHEET.NUMBER())
		layout.addWidget(self.NUMBER, 0, 0, Qt.AlignLeft)
		self.REQUIRE=QLabel("Minimum 100 are required........")
		self.REQUIRE.setStyleSheet(STYLESHEET.REQUIRE())
		self.REQUIRE.setVisible(False)
		layout.addWidget(self.REQUIRE, 0, 2, Qt.AlignHCenter)
		PLabel=QLabel("Pass Mark :")
		PLabel.setStyleSheet(STYLESHEET.PLabel())
		self.PassMark = QSpinBox()
		self.PassMark.setStyleSheet(STYLESHEET.PassMark())
		self.PassMark.setFixedSize(50, 30)
		self.PassMark.setRange(25, 100)
#
		layout.addWidget(PLabel, 0, 4, Qt.AlignRight)
		layout.addWidget(self.PassMark, 0, 5)

	def QNO(self, NO):
		self.NUMBER.setText(f"Q.NO : {NO}")

class Bottom(QGroupBox):
	def __init__(self, sign, Entry):
		super(Bottom, self).__init__()
		self.setFixedHeight(50)
		self.setStyleSheet(STYLESHEET.BOTTOM())
		layout=QGridLayout()
		self.setLayout(layout)
		layout.addWidget(signature(sign), 0, 0, Qt.AlignLeft)


		layout.addWidget(Entry, 0, 5, Qt.AlignRight)

class QENTRY(QWidget):
	Back=pyqtSignal()
	QNO=DATABASE.MaxQuiz()
	def __init__(self, sign):
		super(QENTRY, self).__init__()
		self.newLayout=None
		self.setStyleSheet(STYLESHEET.QENTRY())
		if sign == 'friend group':
			sign="SYSTEM"
		self.QUIZ=QUESTION()
		self.layout=QGridLayout()
		Frame=QGroupBox()
		self.layout.addWidget(Frame)
		self.oldLayout =Frame
		layout=QGridLayout()
		Frame.setLayout(layout)
		self.topBar=TopBar()
		self.topBar.QNO(self.QNO)
		Entry = QPushButton("Entry")
		Entry.pressed.connect(lambda: self.Insert(int(self.QNO), self.QUIZ.toPlainText(), self.topBar.PassMark.value(), self.topBar.REQUIRE, sign))
		Entry.setFixedSize(90, 30)
		Entry.setStyleSheet(STYLESHEET.ENTRY())
		layout.addWidget(self.topBar)
		layout.addWidget(self.QUIZ)
		layout.addWidget(Bottom(sign, Entry))
		self.setLayout(self.layout)
		self.Back.connect(self.back)

	def Insert(self, QNO, QUIZ, PMark, Require, sign):
		if len(QUIZ.split(" "))<100:
			Require.setVisible(True)
		else:
			Require.setVisible(False)
			if DATABASE.QuestionInsert(QNO, QUIZ, PMark, sign):
				self.newLayout = NewQuestion(self, QNO, len(QUIZ.split(" ")), PMark, sign)
				self.layout.replaceWidget(self.oldLayout, self.newLayout)
				self.oldLayout.hide()
				self.newLayout.show()


	def back(self):
		self.QNO = DATABASE.MaxQuiz()
		self.topBar.QNO(self.QNO)

		self.QUIZ.clear()
		self.layout.replaceWidget(self.newLayout, self.oldLayout)
		self.newLayout.hide()
		self.oldLayout.show()
