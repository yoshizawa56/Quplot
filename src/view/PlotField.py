#!/usr/bin/python
# -*- coding: utf-8 -*-
# +ボタンでタブを自由に増やせるtabWidget
from PyQt5.QtWidgets import QWidget, QHBoxLayout

from .GeneralSetting import GeneralSetting


class PlotField(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.setup_ui()
        d = {
            'title' : 'test plot',
            'title_font' : '8',
            'legend_status' : 2,
            'legend_position' : 2
        }
        self.setting.set_default_config(d)
        
    def setup_ui(self):
        layout = QHBoxLayout()
        self.setting = GeneralSetting()
        layout.addWidget(self.setting)
        self.setLayout(layout)
