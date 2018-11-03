#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
+ボタンでタブを自由に増やせるtabWidget
'''

__author__ = "T.Yoshizawa <toru.yoshi.5.1@gmail.com>"
__status__ = "production"
__version__ = "0.1.0"
__date__    = "02 November 2018"


from PyQt5.QtWidgets import QTabWidget, QPushButton
from .DataField import DataField


class DataTab(QTabWidget):
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

        self.insertTab(0, DataField(self), 'Data1')
        self.count = 1
        self.setFixedSize(600, 340)


    def add_tab(self):
        self.count += 1
        self.insertTab(self.count, DataField(self), 'Data' + str(self.count))

    def delete_tab(self, index):
        if self.count > 1:
            self.removeTab(index)
            self.count -= 1

    def broadcast_base_dir(self, base_dir):
        self.base_dir = base_dir
        for i in range(self.count):
            self.widget(i).data.base_dir = base_dir