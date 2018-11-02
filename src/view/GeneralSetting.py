#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
プロット全体に関わる設定の入力用Widget
'''

__author__ = "T.Yoshizawa <toru.yoshi.5.1@gmail.com>"
__status__ = "production"
__version__ = "0.1.0"
__date__    = "02 November 2018"

from PyQt5.QtWidgets import (QWidget, QPushButton, QVBoxLayout,
        QLabel, QLineEdit, QHBoxLayout, QCheckBox, QComboBox)

from ..logic.util import util

class GeneralSetting(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.setup_ui()

    def setup_ui(self):
        #タイトルの編集
        #title_widget = QWidget()
        title_label = QLabel('Title : ')
        self.title_edit = QLineEdit()
        self.title_edit.setPlaceholderText('Input plot title')
        title_font_label = QLabel('Font size : ')
        self.title_font_edit = QLineEdit()
        self.title_font_edit.setMaximumWidth(25)
        title_widgets = [
            title_label,
            self.title_edit,
            title_font_label,
            self.title_font_edit
        ]

        # title_layout = QHBoxLayout()
        # title_layout.addWidget(title_label)
        # title_layout.addWidget(self.title_edit)
        # title_layout.addWidget(title_font_label)
        # title_layout.addWidget(self.title_font_edit)
        # title_widget.setLayout(title_layout)


        #凡例の編集
        legend_widget = QWidget()
        legend_label = QLabel('Legend : ')
        self.legend_checkbox = QCheckBox()
        legend_position_label = QLabel('Position : ')
        self.legend_combo = QComboBox()
        self.legend_combo.addItem('Best')
        self.legend_combo.addItem('Upper Right')
        self.legend_combo.addItem('Upper Left')
        self.legend_combo.addItem('Lower Right')
        self.legend_combo.addItem('Lower Left')
        legend_widgets = [
            legend_label,
            self.legend_checkbox,
            legend_position_label,
            self.legend_combo
        ]

        # legend_layout = QHBoxLayout()
        # legend_layout.addWidget(legend_label)
        # legend_layout.addWidget(self.legend_checkbox)
        # legend_layout.addWidget(legend_position_label)
        # legend_layout.addWidget(self.legend_combo)
        # legend_widget.setLayout(legend_layout)

        #selfに各子Widgetを割り当てる
        self.setLayout(
            Vlayout(
                [
                    Hbox(title_widgets),
                    Hbox(legend_widgets)
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

        util.set_default(default_config_dict, target_list)


