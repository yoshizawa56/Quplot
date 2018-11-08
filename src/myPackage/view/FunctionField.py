#!/usr/bin/python
# -*- coding: utf-8 -*-
# +ボタンでタブを自由に増やせるtabWidget

'''
プロットのデータを関数から取得する際の入力用Widget
'''

__author__ = "T.Yoshizawa <toru.yoshi.5.1@gmail.com>"
__status__ = "production"
__version__ = "0.1.0"
__date__    = "06 November 2018"

from PyQt5.QtWidgets import (QWidget, QPushButton, QVBoxLayout,
        QLabel, QLineEdit, QHBoxLayout, QCheckBox, QComboBox)
from ..logic.Util import Util

class FunctionField(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        #関数入力
        function_label = QLabel('Function : ')
        self.function_edit = QLineEdit()
        self.function_edit.setPlaceholderText('Input function')
        self.function_edit.setMinimumWidth(400)
        function_widgets = [
            function_label,
            self.function_edit
        ]

        #凡例設定
        legend_label = QLabel('Legend : ')
        self.legend_edit = QLineEdit()
        self.legend_edit.setMinimumWidth(250)
        self.legend_combo = QComboBox()
        self.legend_combo.addItem('LaTeX', 'LaTeX')
        self.legend_combo.addItem('Text', 'Text')
        self.legend_combo.addItem('Text')
        self.legend_combo.setItemData(1, 'Text')
        self.legend_combo.setMinimumWidth(80)
        legend_widgets = [
            legend_label,
            self.legend_edit,
            self.legend_combo,
        ]

        #linestyle設定
        line_label = QLabel('Linestyle : ')
        self.line_style_combo = QComboBox()
        Util.set_line_style_combo(self.line_style_combo)
        line_color_label = QLabel('Color : ')
        self.line_color_combo = QComboBox()
        Util.set_color_combo(self.line_color_combo)
        line_width_label = QLabel('Width : ')
        self.line_width_edit = QLineEdit()
        self.line_width_edit.setMaximumWidth(25)
        linestyle_widgets = [
            line_label,
            self.line_style_combo,
            line_color_label,
            self.line_color_combo,
            line_width_label,
            self.line_width_edit
        ]

        #range設定
        range_label = QLabel('Range : ')
        self.range_edit = QLineEdit()
        self.range_edit.setPlaceholderText('~:~')
        range_widget = [
            range_label,
            self.range_edit
        ]

        #selfに各子Widgetを割り当てる
        self.setLayout(
            Util.Vlayout(
                [
                    Util.Hbox(function_widgets),
                    Util.Hbox(legend_widgets),
                    Util.Hbox(linestyle_widgets),
                    Util.Hbox(range_widget)
                ]
            )
        )

        self.contents = [
            ('function', self.function_edit),
            ('legend', self.legend_edit),
            ('legend_style', self.legend_combo),
            ('linestyle', self.line_style_combo),
            ('line_color', self.line_color_combo),
            ('line_width', self.line_width_edit),
            ('function_range', self.range_edit)
        ]

    def config_dict(self):
        config = Util.config_dict(self.contents)
        config.update(marker='None')
        return config

    def set_default_config(self, default_config_dict):
        Util.set_default(default_config_dict, self.contents)

    def set_config(self, config_dict):
        Util.set_config(config_dict, self.contents)