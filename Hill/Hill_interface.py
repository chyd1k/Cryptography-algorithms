# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Hill_interface.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(552, 412)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEditKey = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditKey.setObjectName("lineEditKey")
        self.verticalLayout.addWidget(self.lineEditKey)
        self.btnSetKey = QtWidgets.QPushButton(self.centralwidget)
        self.btnSetKey.setObjectName("btnSetKey")
        self.verticalLayout.addWidget(self.btnSetKey)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEditOpenText = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditOpenText.setObjectName("lineEditOpenText")
        self.verticalLayout.addWidget(self.lineEditOpenText)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnDecrypt = QtWidgets.QPushButton(self.frame)
        self.btnDecrypt.setObjectName("btnDecrypt")
        self.horizontalLayout.addWidget(self.btnDecrypt)
        self.btnEncrypt = QtWidgets.QPushButton(self.frame)
        self.btnEncrypt.setObjectName("btnEncrypt")
        self.horizontalLayout.addWidget(self.btnEncrypt)
        self.verticalLayout.addWidget(self.frame)
        self.lineEditCiphertext = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditCiphertext.setObjectName("lineEditCiphertext")
        self.verticalLayout.addWidget(self.lineEditCiphertext)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 552, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Шифр Хилла"))
        self.label.setText(_translate("MainWindow", "Ключ"))
        self.btnSetKey.setText(_translate("MainWindow", "Задать ключ"))
        self.label_2.setText(_translate("MainWindow", "Входной текст"))
        self.btnDecrypt.setText(_translate("MainWindow", "Расшифровать"))
        self.btnEncrypt.setText(_translate("MainWindow", "Зашифровать"))

