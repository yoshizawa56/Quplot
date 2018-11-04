#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
プロットのデータをファイルから取得する際の入力用Widget
'''

__author__ = "T.Yoshizawa <toru.yoshi.5.1@gmail.com>"
__status__ = "production"
__version__ = "0.1.0"
__date__    = "02 November 2018"

from PyQt5.QtWidgets import (QWidget, QPushButton, QVBoxLayout,
        QLabel, QLineEdit, QHBoxLayout, QComboBox, QFileDialog)
from ..logic.Util import Util
import os

class FileField(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent

        #DataTabでbase_dirが定義されていれば、それをbase_dirとして利用
        if hasattr(self.parent, 'base_dir'):
            self.base_dir = self.parent.base_dir
        self.setup_ui()

        #referenceボタンクリック時
        self.file_reference.clicked.connect(self.file_open)

    def setup_ui(self):
        #ファイル名入力
        file_label = QLabel('File name : ')
        self.file_edit = QLineEdit()
        self.file_edit.setMinimumWidth(300)
        self.file_reference = QPushButton('Reference')
        file_widgets = [
            file_label,
            self.file_edit,
            self.file_reference
        ]

        #凡例設定
        legend_label = QLabel('Legend : ')
        self.legend_edit = QLineEdit()
        self.legend_edit.setMinimumWidth(250)
        self.legend_combo = QComboBox()
        self.legend_combo.addItem('LaTeX', 'LaTeX')
        self.legend_combo.addItem('Text', 'Text')
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

        #marker設定
        marker_label = QLabel('Marker : ')
        self.marker_style_combo = QComboBox()
        self.set_marker_style_combo()
        marker_color_label = QLabel('Color : ')
        self.marker_color_combo = QComboBox()
        self.set_color_combo(self.marker_color_combo)
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

        #selfに各子Widgetを割り当てる
        self.setLayout(
            Util.Vlayout(
                [
                    Util.Hbox(file_widgets),
                    Util.Hbox(legend_widgets),
                    Util.Hbox(linestyle_widgets),
                    Util.Hbox(marker_widgets)
                ]
            )
        )

        #widgetと設定名の対応関係
        self.contents = [
            ('file', self.file_edit),
            ('legend', self.legend_edit),
            ('legend_style', self.legend_combo),
            ('legend_font', self.legend_font_edit),
            ('linestyle', self.line_style_combo),
            ('line_color', self.line_color_combo),
            ('line_width', self.line_width_edit),
            ('marker', self.marker_style_combo),
            ('marker_color', self.marker_color_combo),
            ('marker_size', self.marker_size_edit)
        ]

    def set_line_style_combo(self):
        self.line_style_combo.addItem('None', 'None')
        self.line_style_combo.addItem('-', '-')
        self.line_style_combo.addItem('--', '--')
        self.line_style_combo.addItem('-.', '-.')
        self.line_style_combo.setMinimumWidth(80)
        #TODO linestyleを追加

    def set_marker_style_combo(self):
        self.marker_style_combo.addItem('None', 'None')
        self.marker_style_combo.addItem('o', 'o')
        self.marker_style_combo.addItem('x', 'x')
        self.marker_style_combo.addItem('^', '^')
        self.marker_style_combo.setMinimumWidth(80)
        #TODO linestyleを追加

    def set_color_combo(self, combo):
        combo.addItem('Auto', 'Auto')
        combo.addItem('Black', 'Black')
        combo.setMinimumWidth(120)
        #TODO colorを追加

    def file_open(self):
        #TODO 始点となるディレクトリをどうするか
        self.base_dir = '~/'
        filename = QFileDialog.getOpenFileName(self, "Open file", self.base_dir)
        if(filename != ''):
            self.file_edit.setText(filename[0])
            #次回のファイル
            self.parent.broadcast_base_dir(os.path.dirname(filename[0]))

    def config_dict(self):
        return Util.config_dict(self.contents)

    def set_default_config(self, default_config_dict):
        Util.set_default(default_config_dict, self.contents)

    def set_config(self, config_dict):
        Util.set_config(config_dict, self.contents)

    #TODO connectするメソッド


