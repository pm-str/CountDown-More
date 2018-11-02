# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Clocks.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(384, 88)
        self.timeFormat = QtWidgets.QLineEdit(Dialog)
        self.timeFormat.setGeometry(QtCore.QRect(220, 10, 151, 25))
        self.timeFormat.setObjectName("timeFormat")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 101, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_3.setFont(font)
        self.label_3.setOpenExternalLinks(True)
        self.label_3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 111, 25))
        self.label_4.setObjectName("label_4")
        self.applyButton = QtWidgets.QPushButton(Dialog)
        self.applyButton.setGeometry(QtCore.QRect(280, 50, 89, 25))
        self.applyButton.setStyleSheet("\n"
"background-color: rgb(255, 255, 255, 50%);")
        self.applyButton.setObjectName("applyButton")
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setGeometry(QtCore.QRect(180, 50, 89, 25))
        self.cancelButton.setStyleSheet("\n"
"background-color: rgb(255, 255, 255, 50%);")
        self.cancelButton.setObjectName("cancelButton")

        self.retranslateUi(Dialog)
        self.cancelButton.clicked.connect(Dialog.close)
        self.applyButton.clicked.connect(Dialog.apply_slot)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.timeFormat, self.cancelButton)
        Dialog.setTabOrder(self.cancelButton, self.applyButton)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.timeFormat.setText(_translate("Dialog", "%H:%M:%S"))
        self.label_3.setText(_translate("Dialog", "<a href=\"https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior\">Time formats?</a>"))
        self.label_4.setText(_translate("Dialog", "Format"))
        self.applyButton.setText(_translate("Dialog", "Apply"))
        self.cancelButton.setText(_translate("Dialog", "Cancel"))

