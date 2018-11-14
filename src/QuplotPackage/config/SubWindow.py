#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
デフォルト設定の変更サブウインドのWidget
'''

__author__ = "T.Yoshizawa <toru.yoshi.5.1@gmail.com>"
__version__ = "0.9.0"
__date__    = "14 November 2018"

from PyQt5.QtWidgets import QDialog, QHBoxLayout
from .ConfigTab import ConfigTab
from .ColorMarkerTab import ColorMarkerTab

class SubWindow:
    def __init__(self, mode, parent=None):
        self.dialog = QDialog(parent)
        if mode == 'default':
            self.config_tab = ConfigTab()
        else:
            self.config_tab = ColorMarkerTab()

        layout = QHBoxLayout()
        layout.addWidget(self.config_tab)
        self.dialog.setLayout(layout)

    def show(self):
        self.dialog.exec_()
