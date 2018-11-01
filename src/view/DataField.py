#!/usr/bin/python
# -*- coding: utf-8 -*-
# +ボタンでタブを自由に増やせるtabWidget
from PyQt5.QtWidgets import (QWidget, QPushButton, QVBoxLayout,
        QLabel, QLineEdit, QHBoxLayout, QCheckBox, QComboBox)

from ..logic.util import util
from .FileField import FileField
from .FunctionField import FunctionField

class DataField(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.setup_ui()

        self.data_type.currentIndexChanged.connect(self.data_type_changed)

    def setup_ui(self):
        self.data_type = QComboBox()
        self.data_type.addItem('File')
        self.data_type.addItem('Function')
        
        self.data = FunctionField()

        layout = QVBoxLayout()
        layout.addWidget(self.data_type)
        layout.addWidget(self.data)
        self.setLayout(layout)

    def data_type_changed(self):
        print(1)
        if self.data_type.currentIndex == 0:
            self.data = FileField()
        else:
            self.data = FunctionField()



    def config_dict(self):
        config = {
            
        }

        return config

    def set_default_config(self, default_config_dict):
        target_list = [
            
        ]

        util.set_default(default_config_dict, target_list)


