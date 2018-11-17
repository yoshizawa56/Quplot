#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
軸周りの設定の入力用Widget
'''

__author__ = "T.Yoshizawa <toru.yoshi.5.1@gmail.com>"
__version__ = "0.9.0"
__date__    = "14 November 2018"

from PyQt5.QtWidgets import (QGroupBox, QPushButton, QVBoxLayout,
        QLabel, QLineEdit, QHBoxLayout, QCheckBox, QComboBox)
from ..logic.Util import Util

class AxisSetting(QGroupBox):
    def __init__(self, axis,  parent=None):
        super().__init__(axis + '-Axis')
        self.axis = axis
        self.titles = []
        self.setup_ui(axis)

        self.index_combo.currentIndexChanged.connect(self.set_label)

    def setup_ui(self, axis):
        #軸名
        axis_label = QLabel('Title : ')
        self.axis_edit = QLineEdit()
        self.axis_edit.setMaximumWidth(170)
        self.axis_style_combo = QComboBox()
        self.axis_style_combo.addItem('LaTeX', 'LaTeX')
        self.axis_style_combo.addItem('Text', 'Text')
        self.axis_style_combo.setMinimumWidth(80)
        axis_widgets = [
            axis_label,
            self.axis_edit,
            self.axis_style_combo,
        ]

        #軸名のフォントサイズ
        font_label = QLabel("Font size : ")
        self.font_edit = QLineEdit()
        self.font_edit.setFixedWidth(25)
        font_widgets = [
            font_label,
            self.font_edit
        ]

        #indexの設定
        index_label = QLabel('Data : ')
        self.index_combo = QComboBox()
        self.index_combo.setFixedWidth(150)
        for i in range(1,10):
            self.index_combo.addItem(str(i), str(i-1))
        index_widgets = [
            index_label,
            self.index_combo
        ]

        #スケールの設定
        scale_label = QLabel('Scale : ')
        self.scale_combo = QComboBox(self)
        self.scale_combo.addItem('Linear', 'Linear')
        self.scale_combo.addItem('Log', 'Log')
        self.scale_combo.setMinimumWidth(100)
        scale_widgets = [
            scale_label,
            self.scale_combo
        ]

        #rangeの設定
        range_label = range_label = QLabel('Range : ')
        self.range_edit = QLineEdit()
        self.range_edit.setPlaceholderText('~:~')
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

        #widgetと設定名の対応関係
        self.contents = [
            ('title', self.axis_edit),
            ('style', self.axis_style_combo),
            ('index', self.index_combo),
            ('font', self.font_edit),
            ('scale', self.scale_combo),
            ('range', self.range_edit),
        ]

    def config_dict(self):
        return {self.axis + '_axis' : Util.config_dict(self.contents)}

    def set_default_config(self, default_config_dict):
        default = default_config_dict[self.axis + '_axis']
        Util.set_config(default, self.contents, 'default')

    def set_config(self, config_dict):
        config = config_dict[self.axis + '_axis']
        Util.set_config(config, self.contents)

    def set_index_item(self, items, titles):
        for i in range(len(items)):
            self.index_combo.setItemText(i, items[i])
        if len(items) < 10:
            for i in range(len(items), 10):
                self.index_combo.removeItem(len(items))

        #軸に対応するラベルがあれば設定
        if titles:
            self.titles = titles
            self.set_label()

    def set_label(self):
        if len(self.titles) > self.index_combo.currentIndex():
            self.axis_edit.setText(self.titles[self.index_combo.currentIndex()])