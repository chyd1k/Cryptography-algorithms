# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(331, 294)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnHiSqr = QtWidgets.QPushButton(self.centralwidget)
        self.btnHiSqr.setObjectName("btnHiSqr")
        self.verticalLayout.addWidget(self.btnHiSqr)
        self.btnXor = QtWidgets.QPushButton(self.centralwidget)
        self.btnXor.setObjectName("btnXor")
        self.verticalLayout.addWidget(self.btnXor)
        self.btnHill = QtWidgets.QPushButton(self.centralwidget)
        self.btnHill.setObjectName("btnHill")
        self.verticalLayout.addWidget(self.btnHill)
        self.btnFeistel = QtWidgets.QPushButton(self.centralwidget)
        self.btnFeistel.setObjectName("btnFeistel")
        self.verticalLayout.addWidget(self.btnFeistel)
        self.btnDes = QtWidgets.QPushButton(self.centralwidget)
        self.btnDes.setObjectName("btnDes")
        self.verticalLayout.addWidget(self.btnDes)
        self.btnGenPrime = QtWidgets.QPushButton(self.centralwidget)
        self.btnGenPrime.setObjectName("btnGenPrime")
        self.verticalLayout.addWidget(self.btnGenPrime)
        self.btnPrimitiveRoots = QtWidgets.QPushButton(self.centralwidget)
        self.btnPrimitiveRoots.setObjectName("btnPrimitiveRoots")
        self.verticalLayout.addWidget(self.btnPrimitiveRoots)
        self.btnDiffieHellman = QtWidgets.QPushButton(self.centralwidget)
        self.btnDiffieHellman.setObjectName("btnDiffieHellman")
        self.verticalLayout.addWidget(self.btnDiffieHellman)
        self.btnRSA = QtWidgets.QPushButton(self.centralwidget)
        self.btnRSA.setObjectName("btnRSA")
        self.verticalLayout.addWidget(self.btnRSA)
        self.btnHash = QtWidgets.QPushButton(self.centralwidget)
        self.btnHash.setObjectName("btnHash")
        self.verticalLayout.addWidget(self.btnHash)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 331, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Криптография"))
        self.btnHiSqr.setText(_translate("MainWindow", "Тестирование скремблера"))
        self.btnXor.setText(_translate("MainWindow", "XOR"))
        self.btnHill.setText(_translate("MainWindow", "Шифр Хилла. Демонстрация"))
        self.btnFeistel.setText(_translate("MainWindow", "Сеть Фейстеля"))
        self.btnDes.setText(_translate("MainWindow", "DES"))
        self.btnGenPrime.setText(_translate("MainWindow", "Генерация простых чисел заданной длины"))
        self.btnPrimitiveRoots.setText(_translate("MainWindow", "Поиск первых 100 первообразных корней числа"))
        self.btnDiffieHellman.setText(_translate("MainWindow", "Демонстрация протокола Диффи-Хеллмана"))
        self.btnRSA.setText(_translate("MainWindow", "RSA"))
        self.btnHash.setText(_translate("MainWindow", "ЭЦП"))

