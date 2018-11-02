# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainMenu.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(735, 476)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 131, 17))
        self.label_3.setObjectName("label_3")
        self.choosefileButton = QtWidgets.QPushButton(self.centralwidget)
        self.choosefileButton.setGeometry(QtCore.QRect(10, 49, 131, 25))
        self.choosefileButton.setStyleSheet("\n"
"background-color: rgb(255, 255, 255, 50%);")
        self.choosefileButton.setObjectName("choosefileButton")
        self.editButton = QtWidgets.QPushButton(self.centralwidget)
        self.editButton.setGeometry(QtCore.QRect(10, 360, 171, 25))
        self.editButton.setStyleSheet("\n"
"background-color: rgb(255, 255, 255, 50%);")
        self.editButton.setObjectName("editButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 19, 231, 17))
        self.label_2.setObjectName("label_2")
        self.positionButton = QtWidgets.QPushButton(self.centralwidget)
        self.positionButton.setGeometry(QtCore.QRect(230, 360, 161, 25))
        self.positionButton.setStyleSheet("\n"
"background-color: rgb(255, 255, 255, 50%);")
        self.positionButton.setObjectName("positionButton")
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setGeometry(QtCore.QRect(10, 390, 171, 25))
        self.deleteButton.setStyleSheet("\n"
"background-color: rgb(255, 255, 255, 50%);")
        self.deleteButton.setObjectName("deleteButton")
        self.createCountdButton = QtWidgets.QPushButton(self.centralwidget)
        self.createCountdButton.setGeometry(QtCore.QRect(10, 180, 141, 25))
        self.createCountdButton.setStyleSheet("\n"
"background-color: rgb(255, 255, 255, 90%);")
        self.createCountdButton.setObjectName("createCountdButton")
        self.fileLabel = QtWidgets.QLabel(self.centralwidget)
        self.fileLabel.setGeometry(QtCore.QRect(160, 49, 231, 25))
        self.fileLabel.setText("")
        self.fileLabel.setObjectName("fileLabel")
        self.itemsList = QtWidgets.QListWidget(self.centralwidget)
        self.itemsList.setGeometry(QtCore.QRect(410, 0, 321, 431))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.itemsList.setFont(font)
        self.itemsList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.itemsList.setObjectName("itemsList")
        self.displayButton = QtWidgets.QPushButton(self.centralwidget)
        self.displayButton.setGeometry(QtCore.QRect(230, 390, 161, 25))
        self.displayButton.setStyleSheet("\n"
"background-color: rgb(255, 255, 255, 50%);")
        self.displayButton.setObjectName("displayButton")
        self.resetImageButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetImageButton.setGeometry(QtCore.QRect(370, 50, 22, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.resetImageButton.setFont(font)
        self.resetImageButton.setStyleSheet("color: rgb(164, 0, 0);\n"
"background-color: rgb(255, 255, 255, 50%);\n"
"border-color: rgb(243, 243, 243, 0%);")
        self.resetImageButton.setObjectName("resetImageButton")
        self.createTextButton = QtWidgets.QPushButton(self.centralwidget)
        self.createTextButton.setGeometry(QtCore.QRect(10, 150, 141, 25))
        self.createTextButton.setStyleSheet("\n"
"background-color: rgb(255, 255, 255, 90%);")
        self.createTextButton.setObjectName("createTextButton")
        self.createClocksButton = QtWidgets.QPushButton(self.centralwidget)
        self.createClocksButton.setGeometry(QtCore.QRect(10, 210, 141, 25))
        self.createClocksButton.setStyleSheet("\n"
"background-color: rgb(255, 255, 255, 90%);")
        self.createClocksButton.setObjectName("createClocksButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 735, 22))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionCommon = QtWidgets.QAction(MainWindow)
        self.actionCommon.setObjectName("actionCommon")
        self.menuSettings.addAction(self.actionImport)
        self.menuSettings.addAction(self.actionExport)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.actionCommon)
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        self.deleteButton.clicked.connect(MainWindow.delete_item_slot)
        self.choosefileButton.clicked.connect(MainWindow.choose_file_slot)
        self.editButton.clicked.connect(MainWindow.edit_item_slot)
        self.positionButton.clicked.connect(MainWindow.position_item_slot)
        self.displayButton.clicked.connect(MainWindow.display_layout_slot)
        self.resetImageButton.clicked.connect(MainWindow.reset_image_slot)
        self.itemsList.doubleClicked['QModelIndex'].connect(MainWindow.edit_item_slot)
        self.createCountdButton.clicked.connect(MainWindow.create_countdown_slot)
        self.createTextButton.clicked.connect(MainWindow.create_text_slot)
        self.createClocksButton.clicked.connect(MainWindow.create_clocks_slot)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Create elements"))
        self.choosefileButton.setText(_translate("MainWindow", "Choose a file"))
        self.editButton.setText(_translate("MainWindow", "Edit"))
        self.label_2.setText(_translate("MainWindow", "Background"))
        self.positionButton.setText(_translate("MainWindow", "Position Item"))
        self.deleteButton.setText(_translate("MainWindow", "Delete"))
        self.createCountdButton.setText(_translate("MainWindow", "Countdown"))
        self.displayButton.setText(_translate("MainWindow", "Display Layout"))
        self.resetImageButton.setText(_translate("MainWindow", "X"))
        self.createTextButton.setText(_translate("MainWindow", "Text"))
        self.createClocksButton.setText(_translate("MainWindow", "Clocks"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.actionImport.setText(_translate("MainWindow", "Import"))
        self.actionExport.setText(_translate("MainWindow", "Export"))
        self.actionCommon.setText(_translate("MainWindow", "Common"))

