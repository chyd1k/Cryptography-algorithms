# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChiSqr.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(494, 505)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEditPolynom = QtWidgets.QLineEdit(self.frame)
        self.lineEditPolynom.setObjectName("lineEditPolynom")
        self.horizontalLayout.addWidget(self.lineEditPolynom)
        self.verticalLayout.addWidget(self.frame)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEditRoot = QtWidgets.QLineEdit(self.frame_2)
        self.lineEditRoot.setObjectName("lineEditRoot")
        self.horizontalLayout_2.addWidget(self.lineEditRoot)
        self.verticalLayout.addWidget(self.frame_2)
        self.btnTest = QtWidgets.QPushButton(self.centralwidget)
        self.btnTest.setObjectName("btnTest")
        self.verticalLayout.addWidget(self.btnTest)
        self.textBrowserResult = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowserResult.setObjectName("textBrowserResult")
        self.verticalLayout.addWidget(self.textBrowserResult)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 494, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Введите полином"))
        self.label.setText(_translate("MainWindow", "Пример: пусть полином для скремблера x⁸ + x⁵ + x³ + x² + 1, тогда ввод будет: 8 5 3 2 1"))
        self.label_2.setText(_translate("MainWindow", "Начальное значение"))
        self.btnTest.setText(_translate("MainWindow", "Тестировать"))

