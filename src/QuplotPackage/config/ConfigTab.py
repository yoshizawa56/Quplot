#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
デフォルト設定変更用のタブtabWidget
'''

__author__ = "T.Yoshizawa <toru.yoshi.5.1@gmail.com>"
__version__ = "0.9.0"
__date__    = "14 November 2018"

from PyQt5.QtWidgets import QWidget, QTabWidget, QPushButton

from .Axis import Axis
from .Data import Data
from .General import General
from ..logic.Util import Util


class ConfigTab(QTabWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setup_ui()
        self.set_default_config()

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

        self.setFixedSize(500, 400)

    def set_default_config(self):
        default_config_dict = Util.load_config()
        self.general.set_default_config(default_config_dict)
        self.data.set_default_config(default_config_dict['tab']['data'])
        self.x_axis.set_default_config(default_config_dict['X_axis'])
        self.y_axis.set_default_config(default_config_dict['Y_axis'])
