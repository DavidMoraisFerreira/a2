# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\eric\io\code\a2\ui\a2element\menu_item_edit.ui',
# licensing of 'c:\Users\eric\io\code\a2\ui\a2element\menu_item_edit.ui' applies.
#
# Created: Tue Jan 28 21:59:37 2020
#      by: pyside2-uic  running on PySide2 5.14.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_edit(object):
    def setupUi(self, edit):
        edit.setObjectName("edit")
        edit.resize(549, 86)
        self.edit_layout = QtWidgets.QFormLayout(edit)
        self.edit_layout.setObjectName("edit_layout")
        self.displayLabelLabel = QtWidgets.QLabel(edit)
        self.displayLabelLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.displayLabelLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.displayLabelLabel.setObjectName("displayLabelLabel")
        self.edit_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.displayLabelLabel)
        self.cfg_label = QtWidgets.QLineEdit(edit)
        self.cfg_label.setText("")
        self.cfg_label.setObjectName("cfg_label")
        self.edit_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cfg_label)
        self.displayLabelLabel_3 = QtWidgets.QLabel(edit)
        self.displayLabelLabel_3.setMinimumSize(QtCore.QSize(100, 0))
        self.displayLabelLabel_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.displayLabelLabel_3.setObjectName("displayLabelLabel_3")
        self.edit_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.displayLabelLabel_3)
        self.script_selector = ScriptSelector(edit)
        self.script_selector.setObjectName("script_selector")
        self.edit_layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.script_selector)

        self.retranslateUi(edit)
        QtCore.QMetaObject.connectSlotsByName(edit)

    def retranslateUi(self, edit):
        edit.setWindowTitle(QtWidgets.QApplication.translate("edit", "Form", None, -1))
        self.displayLabelLabel.setText(QtWidgets.QApplication.translate("edit", "display label", None, -1))
        self.displayLabelLabel_3.setText(QtWidgets.QApplication.translate("edit", "python script", None, -1))

from a2widget.local_script import ScriptSelector
