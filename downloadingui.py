# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'downloadingui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Downloading_Dialog(object):
    def setupUi(self, Downloading_Dialog):
        Downloading_Dialog.setObjectName("Downloading_Dialog")
        Downloading_Dialog.resize(400, 90)
        Downloading_Dialog.setCursor(QtGui.QCursor(QtCore.Qt.BusyCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("LMCL.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Downloading_Dialog.setWindowIcon(icon)
        self.progressBar = QtWidgets.QProgressBar(Downloading_Dialog)
        self.progressBar.setGeometry(QtCore.QRect(10, 10, 381, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.speed_label = QtWidgets.QLabel(Downloading_Dialog)
        self.speed_label.setGeometry(QtCore.QRect(20, 60, 101, 16))
        self.speed_label.setAlignment(QtCore.Qt.AlignCenter)
        self.speed_label.setObjectName("speed_label")
        self.connections_label = QtWidgets.QLabel(Downloading_Dialog)
        self.connections_label.setGeometry(QtCore.QRect(190, 60, 141, 16))
        self.connections_label.setAlignment(QtCore.Qt.AlignCenter)
        self.connections_label.setObjectName("connections_label")

        self.retranslateUi(Downloading_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Downloading_Dialog)

    def retranslateUi(self, Downloading_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Downloading_Dialog.setWindowTitle(_translate("Downloading_Dialog", "Dowloading"))
        self.speed_label.setText(_translate("Downloading_Dialog", "Speed: "))
        self.connections_label.setText(_translate("Downloading_Dialog", "Connections: "))
