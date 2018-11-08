#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
デフォルト設定の変更用Widget
'''

__author__ = "T.Yoshizawa <toru.yoshi.5.1@gmail.com>"
__status__ = "production"
__version__ = "0.1.0"
__date__    = "08 November 2018"

from PyQt5.QtWidgets import (QWidget, QPushButton, QVBoxLayout, QCheckBox,
        QLabel, QLineEdit, QHBoxLayout, QComboBox, QFileDialog)
from ..logic.Util import Util
import os

class General(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setup_ui()

        self.apply_button.clicked.connect(self.apply)

    def setup_ui(self):
        #デフォルト保存先
        save_help = 'ファイル名を指定せずに画像を保存した際の保存先ディレクトリを設定'
        save_label = QLabel('Default save directory')
        save_label.setToolTip(save_help)
        self.save_edit = QLineEdit()
        self.save_edit.setToolTip(save_help)
        self.save_reference = QPushButton('Reference')
        save_widgets = [
            save_label,
            self.save_edit,
            self.save_reference
        ]

        #keyword設定
        keyword_help = 'データファイルの先頭２行がこのキーワードから始まっている場合には、要素の説明と認識する'
        keyword_label = QLabel('Keyword')
        keyword_label.setToolTip(keyword_help)
        self.keyword_edit = QLineEdit()
        self.keyword_edit.setToolTip(keyword_help)
        keyword_widgets = [
            keyword_label,
            self.keyword_edit
        ]

        #title font
        title_font_label = QLabel('Title font size : ')
        self.title_font_edit = QLineEdit()
        title_widgets = [
            title_font_label,
            self.title_font_edit
        ]

        #legend
        legend_label = QLabel('Legend : ')
        self.legend_checkbox = QCheckBox()
        legend_position_label = QLabel('Position : ')
        self.legend_combo = QComboBox()
        self.legend_combo.addItem('Text', 'Text')
        self.legend_combo.addItem('LaTeX', 'LaTeX')
        legend_font_label = QLabel('Font size : ')
        self.legend_font_edit = QLineEdit()
        self.title_font_edit.setMaximumWidth(25)
        legend_widgets = [
            legend_label,
            self.legend_checkbox,
            legend_position_label,
            self.legend_combo,
            legend_font_label,
            self.legend_font_edit
        ]

        #Tick labelの設定
        tick_label = QLabel('Tick label font size : ')
        self.tick_edit = QLineEdit()
        self.tick_edit.setFixedWidth(25)
        tick_widgets = [
            tick_label,
            self.tick_edit
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
                    Util.Hbox(save_widgets),
                    Util.Hbox(keyword_widgets),
                    Util.Hbox(title_widgets),
                    Util.Hbox(legend_widgets),
                    Util.Hbox(tick_widgets),
                    apply_widget
                ]
            )
        )

        #widgetと設定名の対応関係
        self.contents = [
            ('fig_base_dir', self.save_edit),
            ('keyword', self.keyword_edit),
            ('title_font', self.title_font_edit),
            ('legend_status', self.legend_checkbox),
            ('legend_position', self.legend_combo),
            ('legend_font', self.legend_font_edit),
            ('tick_font', self.tick_edit)
        ]

    def apply(self):
        current_default = Util.load_default_config()
        for key, value in Util.config_dict(self.contents).items():
            current_default[key] = value

        #TODO defaultファイルのExportの実装
        Util.export_default_config(current_default)

    def set_default_config(self, default_config_dict):
        Util.set_default(default_config_dict, self.contents)