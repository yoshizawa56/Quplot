#!/usr/bin/python
# -*- coding: utf-8 -*-
# +ボタンでタブを自由に増やせるtabWidget
from PyQt5.QtWidgets import (QWidget, QPushButton, QVBoxLayout,
        QLabel, QLineEdit, QHBoxLayout, QCheckBox, QComboBox)

from ..logic.util import util

class FunctionField(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.setup_ui()

    def setup_ui(self):
        file_setting_layout = QHBoxLayout()
        
        file_setting = QWidget()
        file_setting_label = QLabel("File Name : ")
        self.file_edit = QLineEdit()
        self.file_refference = QPushButton("Reference")
        file_setting_layout.addWidget(file_setting_label)
        file_setting_layout.addWidget(self.file_edit)
        file_setting_layout.addWidget(self.file_refference)
        self.setLayout(file_setting_layout)

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


