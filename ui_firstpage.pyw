# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstpage.ui'
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import * 

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)

class Ui_firstPage(object):
    def setupUi(self, firstPage):
        label = QLabel(self)
        pixmap = QtGui.QPixmap('bg.JPG')
        label.setPixmap(pixmap)
        firstPage.setObjectName(_fromUtf8("firstPage"))
        firstPage.resize(500, 350)
        self.widget = QWidget(firstPage)
        self.widget.setGeometry(QtCore.QRect(0, 0, 500, 400))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.firstDisplay = QPlainTextEdit(self.widget)
        self.firstDisplay.setGeometry(QtCore.QRect(0, 0, 500, 400))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.firstDisplay.setFont(font)
        self.firstDisplay.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.firstDisplay.setAutoFillBackground(False)
        self.firstDisplay.setReadOnly(True)
        self.firstDisplay.setObjectName(_fromUtf8("firstDisplay"))
        self.startBtn = QPushButton(self.widget)
        self.startBtn.setGeometry(QtCore.QRect(170, 280, 101, 31))
        self.startBtn.setObjectName(_fromUtf8("startBtn"))
        

        self.retranslateUi(firstPage)
        QtCore.QMetaObject.connectSlotsByName(firstPage)

    def retranslateUi(self, firstPage):
        firstPage.setWindowTitle(_translate("firstPage", "Expert Diagnoser", None))
        self.firstDisplay.setPlainText(_translate("firstPage", "WELCOME TO OUR EXPERT DIAGNOSIS APPLICATION. \n \n THIS APPLICATION IS TARGETED TOWARDS MALARIA AND TYPHOID. ITS GONNA HELP YOU DIAGNOSE MALARIA AND TYPHOID BY ASKING YOU SOME SERIES OF QUESTIONS.\n"
"CLICK THE START BUTTON TO START ", None))
        self.startBtn.setText(_translate("firstPage", "START DIAGNOSIS", None))

