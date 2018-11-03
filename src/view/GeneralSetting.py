#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
プロット全体に関わる設定の入力用Widget
'''

__author__ = "T.Yoshizawa <toru.yoshi.5.1@gmail.com>"
__status__ = "production"
__version__ = "0.1.0"
__date__    = "03 November 2018"

from PyQt5.QtWidgets import (QWidget, QPushButton, QVBoxLayout,
        QLabel, QLineEdit, QHBoxLayout, QCheckBox, QComboBox)
from ..logic.Util import Util

class GeneralSetting(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setup_ui()

        #TODO import_buttonをconnect

    def setup_ui(self):
        #importボタン(右端に表示)
        self.import_button = QPushButton('Import')
        import_layout = QHBoxLayout()
        import_layout.addStretch(0)
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
        legend_widgets = [
            legend_label,
            self.legend_checkbox,
            legend_position_label,
            self.legend_combo
        ]

        #Tick labelの設定
        tick_label = QLabel('Tick label fontsize : ')
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

    #TODO import_buttonにコネクトするメソッド

    def set_legend_combo(self):
        self.legend_combo.addItem('Best')
        self.legend_combo.setItemData(0, 'best')
        self.legend_combo.addItem('Upper Right')
        self.legend_combo.setItemData(1, 'upper right')
        self.legend_combo.addItem('Upper Left')
        self.legend_combo.setItemData(2, 'upper left')
        self.legend_combo.addItem('Lower Right')
        self.legend_combo.setItemData(3, 'lower right')
        self.legend_combo.addItem('Lower Left')
        self.legend_combo.setItemData(4, 'lower left')


    def config_dict(self):
        config = {
            'title' : self.title_edit.text(),
            'title_font' : self.title_font_edit.text(),
            'legend_status' : self.legend_checkbox.isChecked(),
            'legend_position' : Util.combo_data(self.legend_combo),
            'tick_font' : self.tick_edit.text()
        }

        return config

    def set_default_config(self, default_config_dict):
        target_list = [
            ('title_font', self.title_font_edit),
            ('legend_status', self.legend_checkbox),
            ('legend_position', self.legend_combo),
            ('tick_font', self.tick_edit)
        ]

        Util.set_default(default_config_dict, target_list)


