# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'g:\code\python\handwritten_numeral_recognition\layout.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(839, 529)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 371, 111))
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(570, 180, 241, 251))
        self.groupBox.setObjectName("groupBox")
        self.pixmapLabel = QtWidgets.QLabel(self.groupBox)
        self.pixmapLabel.setGeometry(QtCore.QRect(10, 20, 224, 224))
        self.pixmapLabel.setMouseTracking(False)
        self.pixmapLabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pixmapLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.pixmapLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.pixmapLabel.setLineWidth(4)
        self.pixmapLabel.setMidLineWidth(0)
        self.pixmapLabel.setText("")
        self.pixmapLabel.setObjectName("pixmapLabel")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 221, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.dAreaLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.dAreaLayout.setContentsMargins(0, 0, 0, 0)
        self.dAreaLayout.setSpacing(0)
        self.dAreaLayout.setObjectName("dAreaLayout")
        self.recognizeButton = QtWidgets.QPushButton(Dialog)
        self.recognizeButton.setGeometry(QtCore.QRect(640, 450, 121, 41))
        self.recognizeButton.setObjectName("recognizeButton")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(210, 180, 351, 251))
        self.groupBox_2.setObjectName("groupBox_2")
        self.resultTextLabel = QtWidgets.QLabel(self.groupBox_2)
        self.resultTextLabel.setGeometry(QtCore.QRect(40, 40, 111, 51))
        self.resultTextLabel.setObjectName("resultTextLabel")
        self.recognizeResultLabel = QtWidgets.QLabel(self.groupBox_2)
        self.recognizeResultLabel.setGeometry(QtCore.QRect(200, 30, 51, 101))
        self.recognizeResultLabel.setObjectName("recognizeResultLabel")
        self.truthTextLabel = QtWidgets.QLabel(self.groupBox_2)
        self.truthTextLabel.setGeometry(QtCore.QRect(40, 150, 81, 51))
        self.truthTextLabel.setObjectName("truthTextLabel")
        self.truthLabel = QtWidgets.QLabel(self.groupBox_2)
        self.truthLabel.setGeometry(QtCore.QRect(170, 150, 111, 51))
        self.truthLabel.setObjectName("truthLabel")
        self.modeSelectBox = QtWidgets.QComboBox(Dialog)
        self.modeSelectBox.setGeometry(QtCore.QRect(40, 190, 151, 21))
        self.modeSelectBox.setObjectName("modeSelectBox")
        self.modeSelectBox.addItem("")
        self.modeSelectBox.addItem("")
        self.modelSelectTextLabel = QtWidgets.QLabel(Dialog)
        self.modelSelectTextLabel.setGeometry(QtCore.QRect(90, 170, 54, 12))
        self.modelSelectTextLabel.setObjectName("modelSelectTextLabel")
        self.clearButton = QtWidgets.QPushButton(Dialog)
        self.clearButton.setGeometry(QtCore.QRect(480, 450, 121, 41))
        self.clearButton.setObjectName("clearButton")
        self.saveButton = QtWidgets.QPushButton(Dialog)
        self.saveButton.setGeometry(QtCore.QRect(570, 80, 111, 41))
        self.saveButton.setObjectName("saveButton")
        self.nameEdit = QtWidgets.QLineEdit(Dialog)
        self.nameEdit.setGeometry(QtCore.QRect(410, 90, 113, 20))
        self.nameEdit.setObjectName("nameEdit")

        self.retranslateUi(Dialog)
        self.modeSelectBox.activated['QString'].connect(Dialog.mode_change_callback)
        self.saveButton.clicked.connect(Dialog.save_clicked_callback)
        self.clearButton.clicked.connect(Dialog.clear_clicked_callback)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "手写数字识别平台v1.0--------by 钟超承"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">软件说明</span></p><p><span style=\" font-size:14pt;\">1.模式一：训练模式。</span></p><p><span style=\" font-size:14pt;\">2.模式二：识别模式。</span></p><p><br/></p></body></html>"))
        self.groupBox.setTitle(_translate("Dialog", "手写区"))
        self.recognizeButton.setText(_translate("Dialog", "识别"))
        self.groupBox_2.setTitle(_translate("Dialog", "结果区"))
        self.resultTextLabel.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">识别结果：</span></p></body></html>"))
        self.recognizeResultLabel.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:72pt; font-weight:600;\">9</span></p></body></html>"))
        self.truthTextLabel.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">可信度：</span></p></body></html>"))
        self.truthLabel.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">0.99999999</span></p></body></html>"))
        self.modeSelectBox.setItemText(0, _translate("Dialog", "1.训练模式"))
        self.modeSelectBox.setItemText(1, _translate("Dialog", "2.手写识别模式"))
        self.modelSelectTextLabel.setText(_translate("Dialog", "模式选择"))
        self.clearButton.setText(_translate("Dialog", "清除数据"))
        self.saveButton.setText(_translate("Dialog", "保存"))
