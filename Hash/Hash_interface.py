# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Hash.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(719, 510)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnGenerateRandomRSA = QtWidgets.QPushButton(self.frame_3)
        self.btnGenerateRandomRSA.setObjectName("btnGenerateRandomRSA")
        self.horizontalLayout.addWidget(self.btnGenerateRandomRSA)
        self.btnChooseFileRSA = QtWidgets.QPushButton(self.frame_3)
        self.btnChooseFileRSA.setObjectName("btnChooseFileRSA")
        self.horizontalLayout.addWidget(self.btnChooseFileRSA)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEditP = QtWidgets.QLineEdit(self.frame_4)
        self.lineEditP.setObjectName("lineEditP")
        self.horizontalLayout_2.addWidget(self.lineEditP)
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.lineEditQ = QtWidgets.QLineEdit(self.frame_4)
        self.lineEditQ.setObjectName("lineEditQ")
        self.horizontalLayout_2.addWidget(self.lineEditQ)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnGenerateKeysRSA = QtWidgets.QPushButton(self.frame_5)
        self.btnGenerateKeysRSA.setEnabled(False)
        self.btnGenerateKeysRSA.setObjectName("btnGenerateKeysRSA")
        self.horizontalLayout_3.addWidget(self.btnGenerateKeysRSA)
        self.btnImportKeysRSA = QtWidgets.QPushButton(self.frame_5)
        self.btnImportKeysRSA.setObjectName("btnImportKeysRSA")
        self.horizontalLayout_3.addWidget(self.btnImportKeysRSA)
        self.verticalLayout.addWidget(self.frame_5)
        self.textBrowserKeysRSA = QtWidgets.QTextBrowser(self.frame)
        self.textBrowserKeysRSA.setObjectName("textBrowserKeysRSA")
        self.verticalLayout.addWidget(self.textBrowserKeysRSA)
        self.btnSignFileRSA = QtWidgets.QPushButton(self.frame)
        self.btnSignFileRSA.setEnabled(False)
        self.btnSignFileRSA.setObjectName("btnSignFileRSA")
        self.verticalLayout.addWidget(self.btnSignFileRSA)
        self.textBrowserSignRSA = QtWidgets.QTextBrowser(self.frame)
        self.textBrowserSignRSA.setObjectName("textBrowserSignRSA")
        self.verticalLayout.addWidget(self.textBrowserSignRSA)
        self.btnSaveSignRSA = QtWidgets.QPushButton(self.frame)
        self.btnSaveSignRSA.setEnabled(False)
        self.btnSaveSignRSA.setObjectName("btnSaveSignRSA")
        self.verticalLayout.addWidget(self.btnSaveSignRSA)
        self.btnCheckSignRSA = QtWidgets.QPushButton(self.frame)
        self.btnCheckSignRSA.setEnabled(False)
        self.btnCheckSignRSA.setObjectName("btnCheckSignRSA")
        self.verticalLayout.addWidget(self.btnCheckSignRSA)
        self.horizontalLayout_4.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btnGenerateRandomElGamal = QtWidgets.QPushButton(self.frame_6)
        self.btnGenerateRandomElGamal.setObjectName("btnGenerateRandomElGamal")
        self.horizontalLayout_5.addWidget(self.btnGenerateRandomElGamal)
        self.btnChoosePFileElGamal = QtWidgets.QPushButton(self.frame_6)
        self.btnChoosePFileElGamal.setObjectName("btnChoosePFileElGamal")
        self.horizontalLayout_5.addWidget(self.btnChoosePFileElGamal)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.frame_2)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.frame_7)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.lineEditPElGamal = QtWidgets.QLineEdit(self.frame_7)
        self.lineEditPElGamal.setObjectName("lineEditPElGamal")
        self.horizontalLayout_6.addWidget(self.lineEditPElGamal)
        self.verticalLayout_2.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_2)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.btnFindG = QtWidgets.QPushButton(self.frame_8)
        self.btnFindG.setEnabled(False)
        self.btnFindG.setObjectName("btnFindG")
        self.horizontalLayout_7.addWidget(self.btnFindG)
        self.btnChooseGFileElGamal = QtWidgets.QPushButton(self.frame_8)
        self.btnChooseGFileElGamal.setEnabled(False)
        self.btnChooseGFileElGamal.setObjectName("btnChooseGFileElGamal")
        self.horizontalLayout_7.addWidget(self.btnChooseGFileElGamal)
        self.verticalLayout_2.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.frame_2)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.frame_9)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        self.lineEditGElGamal = QtWidgets.QLineEdit(self.frame_9)
        self.lineEditGElGamal.setObjectName("lineEditGElGamal")
        self.horizontalLayout_8.addWidget(self.lineEditGElGamal)
        self.verticalLayout_2.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(self.frame_2)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.btnGenerateKeysElGamal = QtWidgets.QPushButton(self.frame_10)
        self.btnGenerateKeysElGamal.setEnabled(False)
        self.btnGenerateKeysElGamal.setObjectName("btnGenerateKeysElGamal")
        self.horizontalLayout_9.addWidget(self.btnGenerateKeysElGamal)
        self.btnImportKeysElGamal = QtWidgets.QPushButton(self.frame_10)
        self.btnImportKeysElGamal.setObjectName("btnImportKeysElGamal")
        self.horizontalLayout_9.addWidget(self.btnImportKeysElGamal)
        self.verticalLayout_2.addWidget(self.frame_10)
        self.textBrowserKeysElGamal = QtWidgets.QTextBrowser(self.frame_2)
        self.textBrowserKeysElGamal.setObjectName("textBrowserKeysElGamal")
        self.verticalLayout_2.addWidget(self.textBrowserKeysElGamal)
        self.btnSignFileElGamal = QtWidgets.QPushButton(self.frame_2)
        self.btnSignFileElGamal.setEnabled(False)
        self.btnSignFileElGamal.setObjectName("btnSignFileElGamal")
        self.verticalLayout_2.addWidget(self.btnSignFileElGamal)
        self.textBrowserSignElGamal = QtWidgets.QTextBrowser(self.frame_2)
        self.textBrowserSignElGamal.setObjectName("textBrowserSignElGamal")
        self.verticalLayout_2.addWidget(self.textBrowserSignElGamal)
        self.btnSaveSignElGamal = QtWidgets.QPushButton(self.frame_2)
        self.btnSaveSignElGamal.setEnabled(False)
        self.btnSaveSignElGamal.setObjectName("btnSaveSignElGamal")
        self.verticalLayout_2.addWidget(self.btnSaveSignElGamal)
        self.btnCheckSignElGamal = QtWidgets.QPushButton(self.frame_2)
        self.btnCheckSignElGamal.setEnabled(False)
        self.btnCheckSignElGamal.setObjectName("btnCheckSignElGamal")
        self.verticalLayout_2.addWidget(self.btnCheckSignElGamal)
        self.horizontalLayout_4.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 719, 21))
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
        self.label.setText(_translate("MainWindow", "RSA"))
        self.btnGenerateRandomRSA.setText(_translate("MainWindow", "Сгенерировать случайно"))
        self.btnChooseFileRSA.setText(_translate("MainWindow", "Выбрать из файла"))
        self.label_3.setText(_translate("MainWindow", "p"))
        self.label_4.setText(_translate("MainWindow", "q"))
        self.btnGenerateKeysRSA.setText(_translate("MainWindow", "Сгенерировать ключи из p и q"))
        self.btnImportKeysRSA.setText(_translate("MainWindow", "Импортировать ключи"))
        self.btnSignFileRSA.setText(_translate("MainWindow", "Выбрать файл для подписи"))
        self.btnSaveSignRSA.setText(_translate("MainWindow", "Сохранить подпись в файл"))
        self.btnCheckSignRSA.setText(_translate("MainWindow", "Проверить подпись"))
        self.label_2.setText(_translate("MainWindow", "Эль-Гамаль"))
        self.btnGenerateRandomElGamal.setText(_translate("MainWindow", "Сгенерировать p случайно"))
        self.btnChoosePFileElGamal.setText(_translate("MainWindow", "Выбрать p из файла"))
        self.label_5.setText(_translate("MainWindow", "p"))
        self.btnFindG.setText(_translate("MainWindow", "Найти g"))
        self.btnChooseGFileElGamal.setText(_translate("MainWindow", "Выбрать g из файла"))
        self.label_6.setText(_translate("MainWindow", "g"))
        self.btnGenerateKeysElGamal.setText(_translate("MainWindow", "Сгенерировать ключи"))
        self.btnImportKeysElGamal.setText(_translate("MainWindow", "Импортировать ключи"))
        self.btnSignFileElGamal.setText(_translate("MainWindow", "Выбрать файл для подписи"))
        self.btnSaveSignElGamal.setText(_translate("MainWindow", "Сохранить подпись в файл"))
        self.btnCheckSignElGamal.setText(_translate("MainWindow", "Проверить подпись"))

