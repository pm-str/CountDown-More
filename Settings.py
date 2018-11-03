# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Settings.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 157)
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setGeometry(QtCore.QRect(200, 120, 89, 25))
        self.cancelButton.setStyleSheet("\n"
"background-color: rgb(255, 255, 255, 50%);")
        self.cancelButton.setObjectName("cancelButton")
        self.applyButton = QtWidgets.QPushButton(Dialog)
        self.applyButton.setGeometry(QtCore.QRect(300, 120, 89, 25))
        self.applyButton.setStyleSheet("\n"
"background-color: rgb(255, 255, 255, 50%);")
        self.applyButton.setObjectName("applyButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 181, 25))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 181, 25))
        self.label_2.setObjectName("label_2")
        self.updateFrLineEdit = QtWidgets.QLineEdit(Dialog)
        self.updateFrLineEdit.setGeometry(QtCore.QRect(260, 10, 113, 25))
        self.updateFrLineEdit.setObjectName("updateFrLineEdit")
        self.blinkingFrLineEdit = QtWidgets.QLineEdit(Dialog)
        self.blinkingFrLineEdit.setGeometry(QtCore.QRect(260, 40, 113, 25))
        self.blinkingFrLineEdit.setObjectName("blinkingFrLineEdit")

        self.retranslateUi(Dialog)
        self.cancelButton.clicked.connect(Dialog.close)
        self.applyButton.clicked.connect(Dialog.apply_slot)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.cancelButton.setText(_translate("Dialog", "Cancel"))
        self.applyButton.setText(_translate("Dialog", "Apply"))
        self.label.setText(_translate("Dialog", "Timer update frequency:"))
        self.label_2.setText(_translate("Dialog", "Timer blinking frequency:"))
