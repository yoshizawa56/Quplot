#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Export、画像保存用のWidget
'''

__author__ = "T.Yoshizawa <toru.yoshi.5.1@gmail.com>"
__status__ = "production"
__version__ = "0.1.0"
__date__    = "03 November 2018"

from PyQt5.QtWidgets import (QGroupBox, QPushButton, QVBoxLayout,
        QLabel, QLineEdit, QHBoxLayout, QCheckBox, QComboBox, QFileDialog)
from ..logic.Util import Util

class SaveFigure(QGroupBox):
    def __init__(self, parent=None):
        super().__init__('Save figure')
        self.parent = parent
        self.setup_ui()

        self.file_reference.clicked.connect(self.open_save_file)
        self.save_button.clicked.connect(self.save_figure)

    def setup_ui(self):
        #タイトルの編集
        #ファイル名入力
        file_label = QLabel('File name : ')
        self.file_edit = QLineEdit()
        self.file_edit.setFixedWidth(180)
        self.file_reference = QPushButton('Reference')
        self.save_button = QPushButton('Save')
        file_widgets = [
            file_label,
            self.file_edit,
            self.file_reference,
        ]

        #selfに各子Widgetを割り当てる
        self.setLayout(
            Util.Vlayout(
                [
                    Util.Hbox(file_widgets),
                    self.save_button
                ]
            )
        )

        self.contents = [
            ('save_file', self.file_edit)
        ]

    def config_dict(self):
        return Util.config_dict(self.contents)

    def set_default_config(self, default_config_dict):
        Util.set_default(default_config_dict, self.contents)

    def set_config(self, config_dict):
        Util.set_config(config_dict, self.contents)

    def open_save_file(self):
        filename = QFileDialog.getSaveFileName(self, "Open file")
        self.file_edit.setText(filename[0])

    def save_figure(self):
        if str(self.file_edit.text()) == '':
            #TODO デフォルト出力先の設定
            filename = 'default.pdf'
        else:
            filename = self.file_edit.text()
        self.parent.canvas.fig.savefig(filename)


