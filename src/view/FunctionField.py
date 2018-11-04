#!/usr/bin/python
# -*- coding: utf-8 -*-
# +ボタンでタブを自由に増やせるtabWidget

'''
プロットのデータを関数から取得する際の入力用Widget
'''

__author__ = "T.Yoshizawa <toru.yoshi.5.1@gmail.com>"
__status__ = "production"
__version__ = "0.1.0"
__date__    = "02 November 2018"

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
        legend_font_label = QLabel('Font size : ')
        self.legend_font_edit = QLineEdit()
        self.legend_font_edit.setFixedWidth(25)
        legend_widgets = [
            legend_label,
            self.legend_edit,
            self.legend_combo,
            legend_font_label,
            self.legend_font_edit
        ]

        #linestyle設定
        line_label = QLabel('Linestyle : ')
        self.line_style_combo = QComboBox()
        self.set_line_style_combo()
        line_color_label = QLabel('Color : ')
        self.line_color_combo = QComboBox()
        self.set_color_combo(self.line_color_combo)
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

        #selfに各子Widgetを割り当てる
        self.setLayout(
            Util.Vlayout(
                [
                    Util.Hbox(function_widgets),
                    Util.Hbox(legend_widgets),
                    Util.Hbox(linestyle_widgets)
                ]
            )
        )

        self.contents = [
            ('function', self.function_edit),
            ('legend', self.legend_edit),
            ('legend_style', self.legend_combo),
            ('legend_font', self.legend_font_edit),
            ('linestyle', self.line_style_combo),
            ('line_color', self.line_color_combo),
            ('line_width', self.line_width_edit)
        ]

    def set_line_style_combo(self):
        self.line_style_combo.addItem('None', 'None')
        self.line_style_combo.addItem('-', '-')
        self.line_style_combo.addItem('--', '--')
        self.line_style_combo.addItem('-.', '-.')
        self.line_style_combo.setMinimumWidth(80)
        #TODO linestyleを追加

    def set_color_combo(self, combo):
        combo.addItem('Auto', 'Auto')
        combo.addItem('Black', 'Black')
        combo.setMinimumWidth(120)
        #TODO colorを追加

    def config_dict(self):
        return Util.config_dict(self.contents)

    def set_default_config(self, default_config_dict):
        Util.set_default(default_config_dict, self.contents)

    def set_config(self, config_dict):
        Util.set_config(config_dict, self.contents)

    # def config_dict(self):
    #     config = {
    #         'function' : self.function_edit.text(),
    #         'legend' : self.legend_edit.text(),
    #         'legend_style' : Util.combo_data(self.legend_combo),
    #         'legend_font' : self.legend_font_edit.text(),
    #         'linestyle' : Util.combo_data(self.line_style_combo),
    #         'line_color' : Util.combo_data(self.line_color_combo),
    #         'line_width' : self.line_width_edit.text()
    #     }

    #     return config

    # def set_default_config(self, default_config_dict):
    #     target_list = [
    #         ('legend_style', self.legend_combo),
    #         ('legend_font', self.legend_font_edit),
    #         ('linestyle', self.line_style_combo),
    #         ('line_color', self.line_color_combo),
    #         ('line_width', self.line_width_edit)
    #     ]

    #     Util.set_default(default_config_dict, target_list)


