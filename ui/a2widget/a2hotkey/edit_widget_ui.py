# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\eric\io\code\a2\ui\a2widget\a2hotkey\edit_widget.ui',
# licensing of 'C:\Users\eric\io\code\a2\ui\a2widget\a2hotkey\edit_widget.ui' applies.
#
# Created: Sun Jun 17 23:09:57 2018
#      by: pyside2-uic  running on PySide2 5.11.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtWidgets

class Ui_edit(object):
    def setupUi(self, edit):
        edit.setObjectName("edit")
        edit.resize(830, 363)
        self.edit_layout = QtWidgets.QFormLayout(edit)
        self.edit_layout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.edit_layout.setLabelAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop | QtCore.Qt.AlignTrailing)
        self.edit_layout.setObjectName("edit_layout")
        self.internalNameLabel = QtWidgets.QLabel(edit)
        self.internalNameLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.internalNameLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.internalNameLabel.setObjectName("internalNameLabel")
        self.edit_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.internalNameLabel)
        self.cfg_name = QtWidgets.QLineEdit(edit)
        self.cfg_name.setObjectName("cfg_name")
        self.edit_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cfg_name)
        self.displayLabelLabel = QtWidgets.QLabel(edit)
        self.displayLabelLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.displayLabelLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.displayLabelLabel.setObjectName("displayLabelLabel")
        self.edit_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.displayLabelLabel)
        self.cfg_label = QtWidgets.QLineEdit(edit)
        self.cfg_label.setObjectName("cfg_label")
        self.edit_layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cfg_label)
        self.hotkeyLabel = QtWidgets.QLabel(edit)
        self.hotkeyLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.hotkeyLabel.setMaximumSize(QtCore.QSize(200, 16777215))
        self.hotkeyLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.hotkeyLabel.setObjectName("hotkeyLabel")
        self.edit_layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.hotkeyLabel)
        self.hotkey_layout = QtWidgets.QVBoxLayout()
        self.hotkey_layout.setObjectName("hotkey_layout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.hotkey_button = A2Hotkey(edit)
        self.hotkey_button.setEnabled(True)
        self.hotkey_button.setObjectName("hotkey_button")
        self.horizontalLayout_2.addWidget(self.hotkey_button)
        self.a2option_button = A2MoreButton(edit)
        self.a2option_button.setAutoRaise(True)
        self.a2option_button.setObjectName("a2option_button")
        self.horizontalLayout_2.addWidget(self.a2option_button)
        self.hotkey_layout.addLayout(self.horizontalLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(15)
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.cfg_disablable = QtWidgets.QCheckBox(edit)
        self.cfg_disablable.setChecked(True)
        self.cfg_disablable.setObjectName("cfg_disablable")
        self.gridLayout.addWidget(self.cfg_disablable, 1, 0, 1, 1)
        self.cfg_scopeChange = QtWidgets.QCheckBox(edit)
        self.cfg_scopeChange.setChecked(True)
        self.cfg_scopeChange.setObjectName("cfg_scopeChange")
        self.gridLayout.addWidget(self.cfg_scopeChange, 1, 1, 1, 1)
        self.cfg_enabled = QtWidgets.QCheckBox(edit)
        self.cfg_enabled.setChecked(True)
        self.cfg_enabled.setObjectName("cfg_enabled")
        self.gridLayout.addWidget(self.cfg_enabled, 0, 0, 1, 1)
        self.cfg_keyChange = QtWidgets.QCheckBox(edit)
        self.cfg_keyChange.setChecked(True)
        self.cfg_keyChange.setObjectName("cfg_keyChange")
        self.gridLayout.addWidget(self.cfg_keyChange, 0, 1, 1, 1)
        self.cfg_multiple = QtWidgets.QCheckBox(edit)
        self.cfg_multiple.setChecked(True)
        self.cfg_multiple.setObjectName("cfg_multiple")
        self.gridLayout.addWidget(self.cfg_multiple, 2, 0, 1, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.hotkey_layout.addLayout(self.gridLayout)
        self.edit_layout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.hotkey_layout)
        self.functionLabel = QtWidgets.QLabel(edit)
        self.functionLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.functionLabel.setMaximumSize(QtCore.QSize(200, 16777215))
        self.functionLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.functionLabel.setObjectName("functionLabel")
        self.edit_layout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.functionLabel)
        self.func_widget = FuncWidget(edit)
        self.func_widget.setObjectName("func_widget")
        self.edit_layout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.func_widget)

        self.retranslateUi(edit)
        QtCore.QMetaObject.connectSlotsByName(edit)

    def retranslateUi(self, edit):
        edit.setWindowTitle(QtWidgets.QApplication.translate("edit", "Form", None, -1))
        self.internalNameLabel.setText(QtWidgets.QApplication.translate("edit", "internal name:", None, -1))
        self.cfg_name.setText(QtWidgets.QApplication.translate("edit", "extensionX_hotkey1", None, -1))
        self.displayLabelLabel.setText(QtWidgets.QApplication.translate("edit", "display label:", None, -1))
        self.cfg_label.setText(QtWidgets.QApplication.translate("edit", "make some awesome stuff", None, -1))
        self.hotkeyLabel.setText(QtWidgets.QApplication.translate("edit", "hotkey:", None, -1))
        self.hotkey_button.setText(QtWidgets.QApplication.translate("edit", "Win+Shift+A", None, -1))
        self.cfg_disablable.setText(QtWidgets.QApplication.translate("edit", "can be disabled", None, -1))
        self.cfg_scopeChange.setText(QtWidgets.QApplication.translate("edit", "allow scope change", None, -1))
        self.cfg_enabled.setText(QtWidgets.QApplication.translate("edit", "enabled by default", None, -1))
        self.cfg_keyChange.setText(QtWidgets.QApplication.translate("edit", "allow key change", None, -1))
        self.cfg_multiple.setText(QtWidgets.QApplication.translate("edit", "allow multiple hotkeys", None, -1))
        self.functionLabel.setText(QtWidgets.QApplication.translate("edit", "function:", None, -1))

from a2widget import A2MoreButton
from a2widget.a2hotkey import A2Hotkey
from a2widget.a2hotkey.edit_func_widget import FuncWidget
