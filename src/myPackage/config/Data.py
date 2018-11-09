#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
デフォルト設定の変更用Widget
'''

__author__ = "T.Yoshizawa <toru.yoshi.5.1@gmail.com>"
__status__ = "production"
__version__ = "0.1.0"
__date__    = "08 November 2018"

from PyQt5.QtWidgets import (QWidget, QPushButton, QVBoxLayout,
        QLabel, QLineEdit, QHBoxLayout, QComboBox, QFileDialog)
from ..logic.Util import Util
import os

class Data(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setup_ui()

        self.apply_button.clicked.connect(self.apply)

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

        #凡例設定
        legend_label = QLabel('Legend style : ')
        self.legend_combo = QComboBox()
        self.legend_combo.addItem('LaTeX', 'LaTeX')
        self.legend_combo.addItem('Text', 'Text')
        self.legend_combo.setMinimumWidth(80)
        legend_widgets = [
            legend_label,
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

        #marker設定
        marker_label = QLabel('Marker : ')
        self.marker_style_combo = QComboBox()
        Util.set_marker_style_combo(self.marker_style_combo)
        marker_color_label = QLabel('Color : ')
        self.marker_color_combo = QComboBox()
        Util.set_color_combo(self.marker_color_combo)
        marker_size_label = QLabel('Size : ')
        self.marker_size_edit = QLineEdit()
        self.marker_size_edit.setFixedWidth(25)
        marker_widgets = [
            marker_label,
            self.marker_style_combo,
            marker_color_label,
            self.marker_color_combo,
            marker_size_label,
            self.marker_size_edit
        ]

        #適用ボタン
        apply_widget = QWidget()
        self.apply_button = QPushButton('Apply')
        apply_layout = QHBoxLayout()
        apply_layout.setStretch(0,0)
        apply_layout.addWidget(self.apply_button)
        apply_widget.setLayout(apply_layout)

        #selfに各子Widgetを割り当てる
        self.setLayout(
            Util.Vlayout(
                [
                    Util.Hbox(type_widgets),
                    Util.Hbox(legend_widgets),
                    Util.Hbox(linestyle_widgets),
                    Util.Hbox(marker_widgets),
                    apply_widget
                ]
            )
        )

        #widgetと設定名の対応関係
        self.contents = [
            ('data_type', self.data_type),
            ('legend_style', self.legend_combo),
            ('linestyle', self.line_style_combo),
            ('line_color', self.line_color_combo),
            ('line_width', self.line_width_edit),
            ('marker', self.marker_style_combo),
            ('marker_color', self.marker_color_combo),
            ('marker_size', self.marker_size_edit)
        ]

    def apply(self):
        current_default = Util.load_config()
        for key, value in Util.config_dict(self.contents).items():
            current_default['tab']['data'][key] = value

        #defaultファイルのExport
        Util.save_config(current_default)

    def clear(self):
        default = Util.load_config()
        Util.clear_contents(self.contents, default)

    def set_default_config(self, default_config_dict):
        Util.set_config(default_config_dict, self.contents, 'default')