# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sscom.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Sscom_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(860, 645)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(40, 40, 791, 401))
        self.textBrowser.setObjectName("textBrowser")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(370, 480, 461, 101))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(40, 470, 93, 31))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(240, 470, 101, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 470, 71, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(150, 520, 81, 31))
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(240, 520, 101, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(690, 590, 141, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 10, 141, 31))
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(130, 20, 691, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 520, 121, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(360, 450, 191, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(50, 570, 72, 15))
        self.label_6.setObjectName("label_6")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(490, 460, 341, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(110, 560, 81, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(590, 590, 93, 41))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Form)
        self.pushButton_3.clicked.connect(Form.refreshdevice)
        self.pushButton.clicked.connect(Form.SwitchDevice)
        self.pushButton_4.clicked.connect(Form.SaveAsLog)
        self.pushButton_2.clicked.connect(Form.SendMessage)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Swich!"))
        self.comboBox.setItemText(0, _translate("Form", "110"))
        self.comboBox.setItemText(1, _translate("Form", "300"))
        self.comboBox.setItemText(2, _translate("Form", "600"))
        self.comboBox.setItemText(3, _translate("Form", "1200"))
        self.comboBox.setItemText(4, _translate("Form", "2400"))
        self.comboBox.setItemText(5, _translate("Form", "4800"))
        self.comboBox.setItemText(6, _translate("Form", "9600"))
        self.comboBox.setItemText(7, _translate("Form", "14400"))
        self.comboBox.setItemText(8, _translate("Form", "19200"))
        self.comboBox.setItemText(9, _translate("Form", "38400"))
        self.comboBox.setItemText(10, _translate("Form", "56000"))
        self.comboBox.setItemText(11, _translate("Form", "57600"))
        self.comboBox.setItemText(12, _translate("Form", "115200"))
        self.comboBox.setItemText(13, _translate("Form", "128000"))
        self.comboBox.setItemText(14, _translate("Form", "230400"))
        self.comboBox.setItemText(15, _translate("Form", "256000"))
        self.comboBox.setItemText(16, _translate("Form", "468000"))
        self.label.setText(_translate("Form", "Boderate"))
        self.label_2.setText(_translate("Form", "SerialName"))
        self.comboBox_2.setItemText(0, _translate("Form", "COM1"))
        self.comboBox_2.setItemText(1, _translate("Form", "COM2"))
        self.comboBox_2.setItemText(2, _translate("Form", "COM3"))
        self.comboBox_2.setItemText(3, _translate("Form", "COM4"))
        self.comboBox_2.setItemText(4, _translate("Form", "COM5"))
        self.comboBox_2.setItemText(5, _translate("Form", "COM6"))
        self.comboBox_2.setItemText(6, _translate("Form", "COM7"))
        self.comboBox_2.setItemText(7, _translate("Form", "COM8"))
        self.comboBox_2.setItemText(8, _translate("Form", "COM9"))
        self.pushButton_2.setText(_translate("Form", "Send Message"))
        self.label_4.setText(_translate("Form", "MessageView"))
        self.pushButton_3.setText(_translate("Form", "Refresh device"))
        self.label_5.setText(_translate("Form", " Sending Review"))
        self.label_6.setText(_translate("Form", "Status:"))
        self.pushButton_4.setText(_translate("Form", "Save Log"))