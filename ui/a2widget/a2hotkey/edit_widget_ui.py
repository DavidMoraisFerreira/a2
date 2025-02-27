# -*- coding: utf-8 -*-

"""
Form generated from reading UI file 'edit_widget.ui'

Created by: Qt User Interface Compiler version 5.15.2

WARNING! All changes made in this file will be lost when recompiling UI file!
"""

from a2qt.QtCore import *
from a2qt.QtGui import *
from a2qt.QtWidgets import *

from a2widget.a2hotkey import A2Hotkey
from a2widget.a2hotkey.edit_func_widget import FuncWidget
from a2widget.a2more_button import A2MoreButton


class Ui_edit:
    def setupUi(self, edit):
        if not edit.objectName():
            edit.setObjectName(u"edit")
        self.edit_layout = QFormLayout(edit)
        self.edit_layout.setObjectName(u"edit_layout")
        self.edit_layout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.edit_layout.setLabelAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.internalNameLabel = QLabel(edit)
        self.internalNameLabel.setObjectName(u"internalNameLabel")
        self.internalNameLabel.setMinimumSize(QSize(100, 0))
        self.internalNameLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.edit_layout.setWidget(0, QFormLayout.LabelRole, self.internalNameLabel)
        self.cfg_name = QLineEdit(edit)
        self.cfg_name.setObjectName(u"cfg_name")
        self.edit_layout.setWidget(0, QFormLayout.FieldRole, self.cfg_name)
        self.displayLabelLabel = QLabel(edit)
        self.displayLabelLabel.setObjectName(u"displayLabelLabel")
        self.displayLabelLabel.setMinimumSize(QSize(100, 0))
        self.displayLabelLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.edit_layout.setWidget(1, QFormLayout.LabelRole, self.displayLabelLabel)
        self.cfg_label = QLineEdit(edit)
        self.cfg_label.setObjectName(u"cfg_label")
        self.edit_layout.setWidget(1, QFormLayout.FieldRole, self.cfg_label)
        self.hotkeyLabel = QLabel(edit)
        self.hotkeyLabel.setObjectName(u"hotkeyLabel")
        self.hotkeyLabel.setMinimumSize(QSize(100, 0))
        self.hotkeyLabel.setMaximumSize(QSize(200, 16777215))
        self.hotkeyLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.edit_layout.setWidget(2, QFormLayout.LabelRole, self.hotkeyLabel)
        self.hotkey_layout = QVBoxLayout()
        self.hotkey_layout.setObjectName(u"hotkey_layout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.hotkey_button = A2Hotkey(edit)
        self.hotkey_button.setObjectName(u"hotkey_button")
        self.hotkey_button.setEnabled(True)
        self.hotkey_button.setText(u"")
        self.horizontalLayout_2.addWidget(self.hotkey_button)
        self.a2option_button = A2MoreButton(edit)
        self.a2option_button.setObjectName(u"a2option_button")
        self.a2option_button.setAutoRaise(True)
        self.horizontalLayout_2.addWidget(self.a2option_button)
        self.hotkey_layout.addLayout(self.horizontalLayout_2)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(15)
        self.gridLayout.setVerticalSpacing(5)
        self.cfg_disablable = QCheckBox(edit)
        self.cfg_disablable.setObjectName(u"cfg_disablable")
        self.cfg_disablable.setChecked(True)
        self.gridLayout.addWidget(self.cfg_disablable, 1, 0, 1, 1)
        self.cfg_scopeChange = QCheckBox(edit)
        self.cfg_scopeChange.setObjectName(u"cfg_scopeChange")
        self.cfg_scopeChange.setChecked(True)
        self.gridLayout.addWidget(self.cfg_scopeChange, 1, 1, 1, 1)
        self.cfg_enabled = QCheckBox(edit)
        self.cfg_enabled.setObjectName(u"cfg_enabled")
        self.cfg_enabled.setChecked(True)
        self.gridLayout.addWidget(self.cfg_enabled, 0, 0, 1, 1)
        self.cfg_keyChange = QCheckBox(edit)
        self.cfg_keyChange.setObjectName(u"cfg_keyChange")
        self.cfg_keyChange.setChecked(True)
        self.gridLayout.addWidget(self.cfg_keyChange, 0, 1, 1, 1)
        self.cfg_multiple = QCheckBox(edit)
        self.cfg_multiple.setObjectName(u"cfg_multiple")
        self.cfg_multiple.setChecked(True)
        self.gridLayout.addWidget(self.cfg_multiple, 2, 0, 1, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.hotkey_layout.addLayout(self.gridLayout)
        self.edit_layout.setLayout(2, QFormLayout.FieldRole, self.hotkey_layout)
        self.functionLabel = QLabel(edit)
        self.functionLabel.setObjectName(u"functionLabel")
        self.functionLabel.setMinimumSize(QSize(100, 0))
        self.functionLabel.setMaximumSize(QSize(200, 16777215))
        self.functionLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.edit_layout.setWidget(3, QFormLayout.LabelRole, self.functionLabel)
        self.func_widget = FuncWidget(edit)
        self.func_widget.setObjectName(u"func_widget")
        self.edit_layout.setWidget(3, QFormLayout.FieldRole, self.func_widget)
        self.retranslateUi(edit)
        QMetaObject.connectSlotsByName(edit)
    def retranslateUi(self, edit):
        edit.setWindowTitle(QCoreApplication.translate("edit", u"Form", None))
        self.internalNameLabel.setText(QCoreApplication.translate("edit", u"internal name:", None))
        self.cfg_name.setText(QCoreApplication.translate("edit", u"extensionX_hotkey1", None))
        self.displayLabelLabel.setText(QCoreApplication.translate("edit", u"display label:", None))
        self.cfg_label.setText(QCoreApplication.translate("edit", u"make some awesome stuff", None))
        self.hotkeyLabel.setText(QCoreApplication.translate("edit", u"hotkey:", None))
        self.cfg_disablable.setText(QCoreApplication.translate("edit", u"can be disabled", None))
        self.cfg_scopeChange.setText(QCoreApplication.translate("edit", u"allow scope change", None))
        self.cfg_enabled.setText(QCoreApplication.translate("edit", u"enabled by default", None))
        self.cfg_keyChange.setText(QCoreApplication.translate("edit", u"allow key change", None))
        self.cfg_multiple.setText(QCoreApplication.translate("edit", u"allow multiple hotkeys", None))
        self.functionLabel.setText(QCoreApplication.translate("edit", u"function:", None))
