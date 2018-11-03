#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
軸周りの設定の入力用Widget
'''

__author__ = "T.Yoshizawa <toru.yoshi.5.1@gmail.com>"
__status__ = "production"
__version__ = "0.1.0"
__date__    = "03 November 2018"

from PyQt5.QtWidgets import (QGroupBox, QPushButton, QVBoxLayout,
        QLabel, QLineEdit, QHBoxLayout, QCheckBox, QComboBox)
from ..logic.Util import Util

class AxisSetting(QGroupBox):
    def __init__(self, axis,  parent=None):
        super().__init__(axis + '-Axis')
        self.setup_ui(axis)

    def setup_ui(self, axis):
        #軸名
        axis_label = QLabel("Title : ")
        self.axis_edit = QLineEdit()
        self.axis_edit.setMaximumWidth(170)
        self.axis_style_combo = QComboBox()
        self.axis_style_combo.addItem("LaTeX")
        self.axis_style_combo.addItem("Text")
        self.axis_style_combo.setMinimumWidth(80)
        axis_widgets = [
            axis_label,
            self.axis_edit,
            self.axis_style_combo,
        ]

        #軸名のフォントサイズ
        font_label = QLabel("Fontsize : ")
        self.font_edit = QLineEdit()
        self.font_edit.setFixedWidth(25)
        font_widgets = [
            font_label,
            self.font_edit
        ]

        #indexの設定
        index_label = QLabel('Data : ')
        self.index_combo = QComboBox()
        for i in range(1,10):
            self.index_combo.addItem(str(i))
        index_widgets = [
            index_label,
            self.index_combo
        ]

        #スケールの設定
        scale_label = QLabel('Scale : ')
        self.scale_combo = QComboBox(self)
        self.scale_combo.addItem("Linear")
        self.scale_combo.addItem("Log")
        self.scale_combo.setMinimumWidth(100)
        scale_widgets = [
            scale_label,
            self.scale_combo
        ]

        #rangeの設定
        range_label = range_label = QLabel("Range : ")
        self.range_edit = QLineEdit()
        self.range_edit.setMaximumWidth(80)
        range_widgets = [
            range_label,
            self.range_edit
        ]

        #selfに各子Widgetを割り当てる
        self.setLayout(
            Util.Vlayout(
                [
                    Util.Hbox(axis_widgets),
                    Util.Hbox(font_widgets),
                    Util.Hbox(index_widgets),
                    Util.Hbox(scale_widgets),
                    Util.Hbox(range_widgets)
                ]
            )
        )

        # layout = QVBoxLayout()
        # layout.addWidget(title_widget)
        # layout.addWidget(legend_widget)
        # self.setLayout(layout)

    def config_dict(self):
        config = {
            'title' : self.title_edit.text(),
            'title_font' : self.title_font_edit.text(),
            'legend_status' : self.legend_checkbox.isChecked(),
            'legend_position' : self.legend_combo.currentIndex()
        }

        return config

    def set_default_config(self, default_config_dict):
        target_list = [
            ('title', self.title_edit.setPlaceholderText),
            ('title_font', self.title_font_edit.setPlaceholderText),
            ('legend_status', self.legend_checkbox.setCheckState),
            ('legend_position', self.legend_combo.setCurrentIndex)
        ]

        Util.set_default(default_config_dict, target_list)


