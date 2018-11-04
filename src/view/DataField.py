#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
プロットのソースデータの入力用Widget
'''

__author__ = "T.Yoshizawa <toru.yoshi.5.1@gmail.com>"
__status__ = "production"
__version__ = "0.1.0"
__date__    = "04 November 2018"

from PyQt5.QtWidgets import (QWidget, QVBoxLayout,
        QLabel, QHBoxLayout, QComboBox)

from ..logic.Util import Util
from .FileField import FileField
from .FunctionField import FunctionField

class DataField(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.setup_ui()

        #データソースの変更
        self.data_type.currentIndexChanged.connect(self.data_type_changed)

    def setup_ui(self):
        #データソースの種類の選択領域
        label = QLabel('Data source : ')
        self.data_type = QComboBox()
        self.data_type.addItem('File', 'File')
        self.data_type.addItem('Function', 'Function')
        self.data_type.setMinimumWidth(150)
        type_widgets = [
            label,
            self.data_type
        ]

        #データソース入力領域
        self.data = FileField(self.parent)

        #データソース入力領域と結合
        self.layout = Util.Vlayout(
            [
                Util.Hbox(type_widgets),
                self.data
            ]
        )
        self.setLayout(self.layout)

        #widgetと設定名の対応関係
        self.contents = [
            ('data_type', self.data_type)
        ]

    #データソースの種類変更
    def data_type_changed(self):
        #既存Widgetを削除
        self.layout.removeWidget(self.data)
        self.data.deleteLater()
        self.data = None

        #新Widgetを追加
        if self.data_type.currentIndex() == 0:
            self.data = FileField(self.parent)
        else:
            self.data = FunctionField(self.parent)
        self.layout.addWidget(self.data)

        #追加されたTabにデフォルト設定を適用
        self.data.set_default_config(Util.load_default_config()['data0'])

    def config_dict(self):
        config = Util.config_dict(self.contents)
        #子Widgetの設定を追加
        config.update(self.data.config_dict())

        return config

    def set_default_config(self, default_config_dict):
        Util.set_default(default_config_dict, self.contents)
        #子Widgetにデフォルト設定を適用
        self.data.set_default_config(default_config_dict)

    def set_config(self, config_dict):
        Util.set_config(config_dict, self.contents)
        #子Widgetに設定を適用
        self.data.set_config(config_dict)