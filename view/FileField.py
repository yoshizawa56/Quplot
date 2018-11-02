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
        QLabel, QLineEdit, QHBoxLayout, QComboBox)
from ..logic.util import util

class FileField(QWidget):
    def __init__(self, parent=None):
        super().__init__(self, parent=parent)
        self.setup_ui()

        #TODO connect処理

    def setup_ui(self):
        #ファイル名入力
        file_label = QLabel('File name : ')
        self.file_edit = QLineEdit()
        self.file_reference = QPushButton('Reference')
        file_widgets = [
            file_label,
            self.file_edit,
            self.file_reference
        ]

        # file_layout = QHBoxLayout()
        # file_layout.addWidget(file_label)
        # file_layout.addWidget(self.file_edit)
        # file_layout.addWidget(self.file_reference)
        # file_widget = QWidget()
        # file_widget.setLayout(file_layout)

        #凡例設定
        legend_label = QLabel('Legend : ')
        self.legend_edit = QLineEdit()
        legend_style_label = QLabel('Format : ')
        self.legend_combo = QComboBox()
        self.legend_combo.addItem('text')
        self.legend_combo.addItem('LaTeX')
        legend_font_label = QLabel('Fontsize : ')
        self.legend_font_edit = QLineEdit()
        self.legend_font_edit.setMaximumWidth(25)
        legend_widgets = [
            legend_label,
            self.legend_edit,
            legend_style_label,
            self.legend_combo,
            legend_font_label,
            self.legend_font_edit
        ]

        # legend_layout = QHBoxLayout()
        # legend_layout.addWidget(legend_label)
        # legend_layout.addWidget(self.legend_edit)
        # legend_layout.addWidget(legend_style_label)
        # legend_layout.addWidget(self.legend_combo)
        # legend_layout.addWidget(legend_font_label)
        # legend_layout.addWidget(self.legend_font_edit)
        # legend_widget = QWidget()
        # legend_widget.setLayout(legend_layout)

        #linestyle設定
        line_label = QLabel('Linestyle : ')
        self.line_style_combo = QComboBox()
        self.set_line_style_combo()
        line_color_label = QLabel('Color : ')
        self.line_color_combo()
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
        self.marker_color_combo()
        self.set_color_combo(self.marker_color_combo)
        marker_size_label = QLabel('Size : ')
        self.marker_size_edit = QmarkerEdit()
        self.marker_size_edit.setMaximumWidth(25)
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
            Vlayout(
                [
                    Hbox(file_widgets),
                    Hbox(legend_widgets),
                    Hbox(linestyle_widgets),
                    Hbox(marker_widgets)
                ]
            )
        )

    def set_line_style_combo(self):
        self.line_combo.addItem('-')
        self.line_combo.addItem('--')
        self.line_combo.addItem('-.')
        #TODO linestyleを追加
        #TODO userDataの追加

    def set_color_combo(self, combo):
        combo.addItem('Block')
        #TODO colorを追加
        #TODO userDataの追加


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

        util.set_default(default_config_dict, target_list)

    #TODO connectするメソッド


