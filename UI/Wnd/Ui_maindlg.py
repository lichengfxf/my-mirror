# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\BaiduNetdiskWorkspace\Project\src\MyMirror\UI\Wnd\MainDlg.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 500)
        Dialog.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ctnVideo = QtWidgets.QWidget(Dialog)
        self.ctnVideo.setStyleSheet("background-color: rgb(0, 85, 127);")
        self.ctnVideo.setObjectName("ctnVideo")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.ctnVideo)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.VideoShow = QtWidgets.QLabel(self.ctnVideo)
        self.VideoShow.setObjectName("VideoShow")
        self.verticalLayout_2.addWidget(self.VideoShow)
        self.verticalLayout.addWidget(self.ctnVideo)
        self.ctnVoice = QtWidgets.QWidget(Dialog)
        self.ctnVoice.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.ctnVoice.setObjectName("ctnVoice")
        self.verticalLayout.addWidget(self.ctnVoice)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "MagicMirror"))
        self.VideoShow.setText(_translate("Dialog", "没有摄像头"))
