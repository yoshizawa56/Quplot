#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
軸周りのデフォルト設定の変更用Widget
'''

__author__ = "T.Yoshizawa <toru.yoshi.5.1@gmail.com>"
__version__ = "0.9.0"
__date__    = "14 November 2018"

from PyQt5.QtWidgets import (QWidget, QPushButton, QVBoxLayout,
        QLabel, QLineEdit, QHBoxLayout, QComboBox, QFileDialog,
        QMessageBox)
from ..logic.Util import Util
import os

class Axis(QWidget):
    def __init__(self, axis, parent=None):
        super().__init__()
        self.axis = axis
        self.setup_ui()

        self.apply_button.clicked.connect(self.apply)

    def setup_ui(self):
        #軸名
        axis_label = QLabel('Axis title style : ')
        self.axis_style_combo = QComboBox()
        self.axis_style_combo.addItem('LaTeX', 'LaTeX')
        self.axis_style_combo.addItem('Text', 'Text')
        self.axis_style_combo.setMinimumWidth(80)
        font_label = QLabel("Font size : ")
        self.font_edit = QLineEdit()
        self.font_edit.setFixedWidth(25)
        axis_widgets = [
            axis_label,
            self.axis_style_combo,
            font_label,
            self.font_edit
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
                    Util.Hbox(axis_widgets),
                    Util.Hbox(scale_widgets),
                    apply_widget
                ]
            )
        )

        #widgetと設定名の対応関係
        self.contents = [
            ('style', self.axis_style_combo),
            ('font', self.font_edit),
            ('scale', self.scale_combo)
        ]

    def apply(self):
        current_default = Util.load_config()
        for key, value in Util.config_dict(self.contents).items():
            current_default[self.axis + '_axis'][key] = value

        #defaultファイルのExport
        Util.save_config(current_default)
        msg = QMessageBox()
        msg.setText('設定を適用しました')
        msg.exec_()

    def set_default_config(self, default_config_dict):
        Util.set_config(default_config_dict, self.contents, 'default')