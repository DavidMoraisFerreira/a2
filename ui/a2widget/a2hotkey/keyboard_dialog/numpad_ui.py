# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\eric\io\code\a2\ui\a2widget\a2hotkey\keyboard_dialog\numpad.ui',
# licensing of 'C:\Users\eric\io\code\a2\ui\a2widget\a2hotkey\keyboard_dialog\numpad.ui' applies.
#
# Created: Sun Jun 17 23:09:57 2018
#      by: pyside2-uic  running on PySide2 5.11.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtWidgets

class Ui_Numpad(object):
    def setupUi(self, Numpad):
        Numpad.setObjectName("Numpad")
        Numpad.resize(726, 550)
        self.gridLayout = QtWidgets.QGridLayout(Numpad)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.numlock = QtWidgets.QPushButton(Numpad)
        self.numlock.setObjectName("numlock")
        self.gridLayout.addWidget(self.numlock, 1, 0, 1, 1)
        self.numpaddiv = QtWidgets.QPushButton(Numpad)
        self.numpaddiv.setObjectName("numpaddiv")
        self.gridLayout.addWidget(self.numpaddiv, 1, 1, 1, 1)
        self.numpad1 = QtWidgets.QPushButton(Numpad)
        self.numpad1.setObjectName("numpad1")
        self.gridLayout.addWidget(self.numpad1, 4, 0, 1, 1)
        self.numpad5 = QtWidgets.QPushButton(Numpad)
        self.numpad5.setObjectName("numpad5")
        self.gridLayout.addWidget(self.numpad5, 3, 1, 1, 1)
        self.numpadmult = QtWidgets.QPushButton(Numpad)
        self.numpadmult.setObjectName("numpadmult")
        self.gridLayout.addWidget(self.numpadmult, 1, 2, 1, 1)
        self.numpad8 = QtWidgets.QPushButton(Numpad)
        self.numpad8.setObjectName("numpad8")
        self.gridLayout.addWidget(self.numpad8, 2, 1, 1, 1)
        self.numpad4 = QtWidgets.QPushButton(Numpad)
        self.numpad4.setObjectName("numpad4")
        self.gridLayout.addWidget(self.numpad4, 3, 0, 1, 1)
        self.numpad3 = QtWidgets.QPushButton(Numpad)
        self.numpad3.setObjectName("numpad3")
        self.gridLayout.addWidget(self.numpad3, 4, 2, 1, 1)
        self.numpad6 = QtWidgets.QPushButton(Numpad)
        self.numpad6.setObjectName("numpad6")
        self.gridLayout.addWidget(self.numpad6, 3, 2, 1, 1)
        self.numpad7 = QtWidgets.QPushButton(Numpad)
        self.numpad7.setObjectName("numpad7")
        self.gridLayout.addWidget(self.numpad7, 2, 0, 1, 1)
        self.numpad2 = QtWidgets.QPushButton(Numpad)
        self.numpad2.setObjectName("numpad2")
        self.gridLayout.addWidget(self.numpad2, 4, 1, 1, 1)
        self.numpaddot = QtWidgets.QPushButton(Numpad)
        self.numpaddot.setObjectName("numpaddot")
        self.gridLayout.addWidget(self.numpaddot, 5, 2, 1, 1)
        self.numpad9 = QtWidgets.QPushButton(Numpad)
        self.numpad9.setObjectName("numpad9")
        self.gridLayout.addWidget(self.numpad9, 2, 2, 1, 1)
        self.numpad0 = QtWidgets.QPushButton(Numpad)
        self.numpad0.setObjectName("numpad0")
        self.gridLayout.addWidget(self.numpad0, 5, 0, 1, 2)
        self.numpadsub = QtWidgets.QPushButton(Numpad)
        self.numpadsub.setObjectName("numpadsub")
        self.gridLayout.addWidget(self.numpadsub, 1, 3, 1, 1)
        self.num_spacer = QtWidgets.QWidget(Numpad)
        self.num_spacer.setObjectName("num_spacer")
        self.gridLayout.addWidget(self.num_spacer, 0, 0, 1, 5)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.numpadadd = QtWidgets.QPushButton(Numpad)
        self.numpadadd.setMinimumSize(QtCore.QSize(0, 120))
        self.numpadadd.setObjectName("numpadadd")
        self.verticalLayout_2.addWidget(self.numpadadd)
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout_2, 2, 3, 2, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.numpadenter = QtWidgets.QPushButton(Numpad)
        self.numpadenter.setMinimumSize(QtCore.QSize(0, 90))
        self.numpadenter.setObjectName("numpadenter")
        self.verticalLayout.addWidget(self.numpadenter)
        spacerItem1 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.verticalLayout, 4, 3, 2, 1)
        self.gridLayout.setRowStretch(0, 1)

        self.retranslateUi(Numpad)
        QtCore.QMetaObject.connectSlotsByName(Numpad)

    def retranslateUi(self, Numpad):
        Numpad.setWindowTitle(QtWidgets.QApplication.translate("Numpad", "Form", None, -1))
        self.numlock.setText(QtWidgets.QApplication.translate("Numpad", "Num\n"
"Lock", None, -1))
        self.numpaddiv.setText(QtWidgets.QApplication.translate("Numpad", "/", None, -1))
        self.numpad1.setText(QtWidgets.QApplication.translate("Numpad", "1", None, -1))
        self.numpad5.setText(QtWidgets.QApplication.translate("Numpad", "5", None, -1))
        self.numpadmult.setText(QtWidgets.QApplication.translate("Numpad", "*", None, -1))
        self.numpad8.setText(QtWidgets.QApplication.translate("Numpad", "8", None, -1))
        self.numpad4.setText(QtWidgets.QApplication.translate("Numpad", "4", None, -1))
        self.numpad3.setText(QtWidgets.QApplication.translate("Numpad", "3", None, -1))
        self.numpad6.setText(QtWidgets.QApplication.translate("Numpad", "6", None, -1))
        self.numpad7.setText(QtWidgets.QApplication.translate("Numpad", "7", None, -1))
        self.numpad2.setText(QtWidgets.QApplication.translate("Numpad", "2", None, -1))
        self.numpaddot.setText(QtWidgets.QApplication.translate("Numpad", ".", None, -1))
        self.numpad9.setText(QtWidgets.QApplication.translate("Numpad", "9", None, -1))
        self.numpad0.setText(QtWidgets.QApplication.translate("Numpad", "0", None, -1))
        self.numpadsub.setText(QtWidgets.QApplication.translate("Numpad", "-", None, -1))
        self.numpadadd.setText(QtWidgets.QApplication.translate("Numpad", "+", None, -1))
        self.numpadenter.setText(QtWidgets.QApplication.translate("Numpad", "Enter", None, -1))

