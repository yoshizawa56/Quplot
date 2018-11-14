#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
colorとmarkerの設定を行うタブ
'''

__author__ = "T.Yoshizawa <toru.yoshi.5.1@gmail.com>"
__version__ = "0.9.0"
__date__    = "14 November 2018"

from PyQt5.QtWidgets import QWidget, QTabWidget, QPushButton
from .ColorConfig import ColorConfig
from .MarkerConfig import MarkerConfig

class ColorMarkerTab(QTabWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.color = ColorConfig()
        self.marker = MarkerConfig()
        
        widget_list = [
            ('Colors', self.color),
            ('Markers', self.marker)
        ]
        self.count = 0
        for name, widget in widget_list:
            self.insertTab(self.count, widget, name)
            self.count += 1

        self.setFixedSize(600, 400)
