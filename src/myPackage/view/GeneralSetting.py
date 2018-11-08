#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
プロット全体に関わる設定の入力用Widget
'''

__author__ = "T.Yoshizawa <toru.yoshi.5.1@gmail.com>"
__status__ = "production"
__version__ = "0.1.0"
__date__    = "06 November 2018"

from PyQt5.QtWidgets import (QWidget, QPushButton, QVBoxLayout,
        QLabel, QLineEdit, QHBoxLayout, QCheckBox, QComboBox)
from ..logic.Util import Util

class GeneralSetting(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        #importボタン(右端に表示)
        self.export_button = QPushButton('Export')
        self.import_button = QPushButton('Import')
        self.import_last_button = QPushButton('Import last plot')
        import_layout = QHBoxLayout()
        import_layout.addWidget(self.export_button)
        import_layout.addStretch(0)
        import_layout.addWidget(self.import_last_button)
        import_layout.addWidget(self.import_button)
        import_widget = QWidget()
        import_widget.setLayout(import_layout)

        #タイトルの編集
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

        #凡例の編集
        legend_label = QLabel('Legend : ')
        self.legend_checkbox = QCheckBox()
        legend_position_label = QLabel('Position : ')
        self.legend_combo = QComboBox()
        self.set_legend_combo()
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

        #selfに各子Widgetを割り当てる
        self.setLayout(
            Util.Vlayout(
                [
                    import_widget,
                    Util.Hbox(title_widgets),
                    Util.Hbox(legend_widgets),
                    Util.Hbox(tick_widgets)
                ]
            )
        )

        #widgetと設定名の対応関係
        self.contents = [
            ('title', self.title_edit),
            ('title_font', self.title_font_edit),
            ('legend_status', self.legend_checkbox),
            ('legend_position', self.legend_combo),
            ('legend_font', self.legend_font_edit),
            ('tick_font', self.tick_edit)
        ]

    def set_legend_combo(self):
        self.legend_combo.addItem('Best', 'best')
        self.legend_combo.addItem('Upper Right', 'upper right')
        self.legend_combo.addItem('Upper Left', 'upper left')
        self.legend_combo.addItem('Lower Right', 'lower right')
        self.legend_combo.addItem('Lower Left', 'lower left')

    def config_dict(self):
        return Util.config_dict(self.contents)

    def set_default_config(self, default_config_dict):
        Util.set_default(default_config_dict, self.contents)

    def set_config(self, config_dict):
        Util.set_config(config_dict, self.contents)