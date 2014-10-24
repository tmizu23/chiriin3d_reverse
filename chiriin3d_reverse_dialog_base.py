# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chiriin3d_reverse_dialog_base.ui'
#
# Created: Fri Oct 24 21:00:38 2014
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Chiriin3D_reverseDialogBase(object):
    def setupUi(self, Chiriin3D_reverseDialogBase):
        Chiriin3D_reverseDialogBase.setObjectName(_fromUtf8("Chiriin3D_reverseDialogBase"))
        Chiriin3D_reverseDialogBase.resize(400, 211)
        self.toolButton = QtGui.QToolButton(Chiriin3D_reverseDialogBase)
        self.toolButton.setGeometry(QtCore.QRect(330, 40, 61, 18))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.lineEdit = QtGui.QLineEdit(Chiriin3D_reverseDialogBase)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 311, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Chiriin3D_reverseDialogBase)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 90, 311, 20))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label = QtGui.QLabel(Chiriin3D_reverseDialogBase)
        self.label.setGeometry(QtCore.QRect(10, 10, 50, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Chiriin3D_reverseDialogBase)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 71, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(Chiriin3D_reverseDialogBase)
        self.pushButton.setGeometry(QtCore.QRect(120, 170, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Chiriin3D_reverseDialogBase)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 170, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.radioButton = QtGui.QRadioButton(Chiriin3D_reverseDialogBase)
        self.radioButton.setGeometry(QtCore.QRect(110, 130, 41, 16))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.buttonGroup = QtGui.QButtonGroup(Chiriin3D_reverseDialogBase)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(Chiriin3D_reverseDialogBase)
        self.radioButton_2.setGeometry(QtCore.QRect(180, 130, 51, 16))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.buttonGroup.addButton(self.radioButton_2)
        self.radioButton_3 = QtGui.QRadioButton(Chiriin3D_reverseDialogBase)
        self.radioButton_3.setGeometry(QtCore.QRect(250, 130, 41, 16))
        self.radioButton_3.setChecked(True)
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.buttonGroup.addButton(self.radioButton_3)
        self.label_3 = QtGui.QLabel(Chiriin3D_reverseDialogBase)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 71, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(Chiriin3D_reverseDialogBase)
        QtCore.QMetaObject.connectSlotsByName(Chiriin3D_reverseDialogBase)

    def retranslateUi(self, Chiriin3D_reverseDialogBase):
        Chiriin3D_reverseDialogBase.setWindowTitle(QtGui.QApplication.translate("Chiriin3D_reverseDialogBase", "Chiriin3D reverse", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton.setText(QtGui.QApplication.translate("Chiriin3D_reverseDialogBase", "Browse...", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Chiriin3D_reverseDialogBase", "Input STL", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Chiriin3D_reverseDialogBase", "Output STL", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Chiriin3D_reverseDialogBase", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Chiriin3D_reverseDialogBase", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton.setText(QtGui.QApplication.translate("Chiriin3D_reverseDialogBase", "left", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_2.setText(QtGui.QApplication.translate("Chiriin3D_reverseDialogBase", "right", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_3.setText(QtGui.QApplication.translate("Chiriin3D_reverseDialogBase", "all", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Chiriin3D_reverseDialogBase", "Output Parts", None, QtGui.QApplication.UnicodeUTF8))

