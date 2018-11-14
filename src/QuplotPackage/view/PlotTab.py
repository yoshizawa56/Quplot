#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
+ボタンでタブを自由に増やせるtabWidget
'''

__author__ = "T.Yoshizawa <toru.yoshi.5.1@gmail.com>"
__version__ = "0.9.0"
__date__    = "14 November 2018"

from PyQt5.QtWidgets import QWidget, QTabWidget, QPushButton, QMessageBox

from .PlotField import PlotField
from ..logic.Util import Util


class PlotTab(QTabWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setTabsClosable(True)
        self.setMovable(True)
        self.tabCloseRequested.connect(self.delete_tab)
        self.setup_ui()

    def setup_ui(self):
        addButton = QPushButton('+', self)
        addButton.clicked.connect(self.add_tab)
        self.setCornerWidget(addButton)

        self.insertTab(0, PlotField(), 'Plot1')
        self.count = 1

        self.setFixedSize(1120, 750)


    def add_tab(self):
        self.count += 1
        self.insertTab(self.count, PlotField(), 'Plot' + str(self.count))

    def delete_tab(self, index):
        if self.count > 1:
            self.removeTab(index)
            self.count -= 1

