#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
プロットのソースデータの入力用Widget
'''

__author__ = "T.Yoshizawa <toru.yoshi.5.1@gmail.com>"
__status__ = "production"
__version__ = "0.1.0"
__date__    = "02 November 2018"

from PyQt5.QtWidgets import (QWidget, QVBoxLayout,
        QLabel, QHBoxLayout, QComboBox)

from ..logic.util import util
from .FileField import FileField
from .FunctionField import FunctionField

class DataField(QWidget):
    def __init__(self, parent=None):
        super().__init__(self, parent=parent)
        self.setup_ui()

        #データソースの変更
        self.data_type.currentIndexChanged.connect(self.data_type_changed)

    def setup_ui(self):
        #データソースの種類の選択領域
        label = Qlabel('Data source : ')
        self.data_type = QComboBox()
        self.data_type.addItem('File')
        self.data_type.addItem('Function')
        type_widgets = [
            label,
            self.data_type
        ]

        # type_layout = QHBoxLayout()
        # type_layout.addWidget(label)
        # type_layout.addWidget(self.data_type)
        # data_widget = QWidget()
        # data_widget.setLayout(type_layout)

        #データソース入力領域
        self.data = FileField()

        #データソース入力領域と結合
        self.setLayout(
            Vlayout(
                [
                    Hbox(type_layout),
                    self.data
                ]
            )
        )

    #データソースの種類変更
    def data_type_changed(self):
        self.layout.removeWidget(self.data)
        if self.data_type.currentIndex == 0:
            self.data = FileField()
        else:
            self.data = FunctionField()

        self.layout.addWidget(self.data)



    def config_dict(self):
        config = {
            'data_type' : self.data_type.currentIndex
        }
        config.update(self.data.config_dict)

        return config

    def set_default_config(self, default_config_dict):
        target_list = [
            ('data_type', self.data_type.setCurrentIndex)
        ]
        util.set_default(default_config_dict, target_list)

        #子要素にデフォルト設定を適用
        self.set_default_config(default_config_dict)


