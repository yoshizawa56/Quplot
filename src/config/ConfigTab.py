#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
+ボタンでタブを自由に増やせるtabWidget
'''

__author__ = "T.Yoshizawa <toru.yoshi.5.1@gmail.com>"
__status__ = "production"
__version__ = "0.1.0"
__date__    = "02 November 2018"

from PyQt5.QtWidgets import QWidget, QTabWidget, QPushButton

from .Axis import Axis
from .Data import Data
from .General import General


class ConfigTab(QTabWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.general = General()
        self.data = Data()
        self.x_axis = Axis('X')
        self.y_axis = Axis('Y')

        widget_list = [
            ('Data Source', self.data),
            ('X-Axis', self.x_axis),
            ('Y-Axis', self.y_axis),
            ('Other Settings', self.general)
        ]
        self.count = 0
        for name, widget in widget_list:
            self.insertTab(self.count, widget, name)
            self.count += 1

        self.setFixedSize(800, 600)