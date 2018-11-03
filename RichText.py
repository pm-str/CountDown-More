# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RichText.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(342, 242)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(0, 10, 341, 192))
        self.textEdit.setAutoFillBackground(False)
        self.textEdit.setObjectName("textEdit")
        self.applyButton = QtWidgets.QPushButton(Dialog)
        self.applyButton.setGeometry(QtCore.QRect(250, 210, 89, 25))
        self.applyButton.setStyleSheet("\n"
"background-color: rgb(255, 255, 255, 50%);")
        self.applyButton.setObjectName("applyButton")
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setGeometry(QtCore.QRect(150, 210, 89, 25))
        self.cancelButton.setStyleSheet("\n"
"background-color: rgb(255, 255, 255, 50%);")
        self.cancelButton.setObjectName("cancelButton")

        self.retranslateUi(Dialog)
        self.applyButton.clicked.connect(Dialog.apply_slot)
        self.cancelButton.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.applyButton.setText(_translate("Dialog", "Apply"))
        self.cancelButton.setText(_translate("Dialog", "Cancel"))
