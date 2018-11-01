#!/usr/bin/python
# -*- coding: utf-8 -*-
# +ボタンでタブを自由に増やせるtabWidget
from PyQt5.QtWidgets import QWidget, QTabWidget, QPushButton

from GeneralSetting import GeneralSetting


class PlotTab(QTabWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.setTabsClosable(True)
        self.setMovable(True)
        self.tabCloseRequested.connect(self.delete_tab)
        self.setup_ui()
        
    def setup_ui(self):
        addButton = QPushButton('+', self)
        addButton.clicked.connect(self.add_tab)
        self.setCornerWidget(addButton)

        self.insertTab(0, GeneralSetting(), 'Plot1')
        self.count = 1

    
    def add_tab(self):
        self.count += 1
        self.insertTab(self.count, GeneralSetting(), 'Plot' + str(self.count))

    def delete_tab(self, index):
        if self.count > 1:
            self.removeTab(index)
            self.count -= 1

