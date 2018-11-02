# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Countdown.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(406, 210)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 26))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 111, 25))
        self.label_2.setObjectName("label_2")
        self.timeFormat = QtWidgets.QLineEdit(Dialog)
        self.timeFormat.setGeometry(QtCore.QRect(220, 70, 151, 25))
        self.timeFormat.setObjectName("timeFormat")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 170, 101, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_3.setFont(font)
        self.label_3.setOpenExternalLinks(True)
        self.label_3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_3.setObjectName("label_3")
        self.timeStart = QtWidgets.QTimeEdit(Dialog)
        self.timeStart.setGeometry(QtCore.QRect(220, 10, 151, 26))
        self.timeStart.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.timeStart.setObjectName("timeStart")
        self.timeEnd = QtWidgets.QTimeEdit(Dialog)
        self.timeEnd.setGeometry(QtCore.QRect(220, 40, 151, 26))
        self.timeEnd.setTime(QtCore.QTime(1, 0, 0))
        self.timeEnd.setObjectName("timeEnd")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 111, 25))
        self.label_4.setObjectName("label_4")
        self.applyButton = QtWidgets.QPushButton(Dialog)
        self.applyButton.setGeometry(QtCore.QRect(290, 170, 89, 25))
        self.applyButton.setStyleSheet("\n"
"background-color: rgb(255, 255, 255, 50%);")
        self.applyButton.setObjectName("applyButton")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 100, 231, 41))
        self.label_5.setObjectName("label_5")
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setGeometry(QtCore.QRect(190, 170, 89, 25))
        self.cancelButton.setStyleSheet("\n"
"background-color: rgb(255, 255, 255, 50%);")
        self.cancelButton.setObjectName("cancelButton")
        self.blinkSpinBox = QtWidgets.QSpinBox(Dialog)
        self.blinkSpinBox.setGeometry(QtCore.QRect(280, 110, 91, 26))
        self.blinkSpinBox.setSpecialValueText("")
        self.blinkSpinBox.setMinimum(-1)
        self.blinkSpinBox.setProperty("value", -1)
        self.blinkSpinBox.setObjectName("blinkSpinBox")

        self.retranslateUi(Dialog)
        self.cancelButton.clicked.connect(Dialog.close)
        self.applyButton.clicked.connect(Dialog.apply_slot)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.timeStart, self.timeEnd)
        Dialog.setTabOrder(self.timeEnd, self.timeFormat)
        Dialog.setTabOrder(self.timeFormat, self.cancelButton)
        Dialog.setTabOrder(self.cancelButton, self.applyButton)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Start"))
        self.label_2.setText(_translate("Dialog", "End"))
        self.timeFormat.setText(_translate("Dialog", "%H:%M:%S"))
        self.label_3.setText(_translate("Dialog", "<a href=\"https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior\">Time formats?</a>"))
        self.timeStart.setDisplayFormat(_translate("Dialog", "hh:mm:ss"))
        self.timeEnd.setDisplayFormat(_translate("Dialog", "hh:mm:ss"))
        self.label_4.setText(_translate("Dialog", "Format"))
        self.applyButton.setText(_translate("Dialog", "Apply"))
        self.label_5.setText(_translate("Dialog", "Blink at the end\n"
"Sec before (disabled = -1)"))
        self.cancelButton.setText(_translate("Dialog", "Cancel"))

