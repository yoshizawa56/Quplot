#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
colorのlistを表示・編集するWidget
'''

__author__ = "T.Yoshizawa <toru.yoshi.5.1@gmail.com>"
__version__ = "0.9.0"
__date__    = "14 November 2018"

from PyQt5.QtWidgets import (QWidget, QListWidget, QListWidgetItem, QGroupBox, 
                    QLabel, QLineEdit, QPushButton, QColorDialog, QHBoxLayout,
                    QMessageBox, QAbstractItemView)
from ..logic.Util import Util
import os

class ColorConfig(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setup_ui()

        self.value_reference.clicked.connect(self.open_color_dialog)
        self.add_button.clicked.connect(self.add_color)
        self.delete_button.clicked.connect(self.delete_color)
        self.apply_button.clicked.connect(self.apply)

        self.color_list.setAcceptDrops(True)
        self.color_list.setDragEnabled(True)
        self.color_list.setDragDropOverwriteMode(False)
        self.color_list.setDragDropMode(QAbstractItemView.InternalMove)

    def setup_ui(self):
        #色追加用入力領域（左側）
        add_color_box = QGroupBox('Add new color')

        #name
        name_label = QLabel('New Color name : ')
        self.name_edit = QLineEdit()
        name_widgets = [
            name_label,
            self.name_edit
        ]

        #color value(RGB)
        value_label = QLabel('RGB : ')
        self.value_edit = QLineEdit()
        self.value_reference = QPushButton('Edit color')
        value_widgets = [
            value_label,
            self.value_edit,
            self.value_reference
        ]

        #add button
        self.add_button = QPushButton('Add')

        #左側のレイアウト
        add_color_box.setLayout(
            Util.Vlayout(
                [
                    Util.Hbox(name_widgets),
                    Util.Hbox(value_widgets),
                    self.add_button
                ]
            )
        )

        #colorのリスト（右側）
        self.color_list = QListWidget()
        self.set_color_list(self.color_list)
        
        #deleteボタン（左詰め）
        self.apply_button = QPushButton('apply')
        self.delete_button = QPushButton('Delete')
        delete_layout = QHBoxLayout()
        delete_layout.addStretch(0)
        delete_layout.addWidget(self.apply_button)
        delete_layout.addWidget(self.delete_button)
        delete_widget = QWidget()
        delete_widget.setLayout(delete_layout)

        right_box = Util.Vbox(
            [
                self.color_list,
                delete_widget
            ]
        )

        #全体を配置
        self.setLayout(
            Util.Hlayout(
                [
                    add_color_box,
                    right_box
                ]
            )
        )

    def set_color_list(self, color_list):
        colors = Util.load_items()['colors']
        for name, color in colors.items():
            item = self.set_item(name, color)
            color_list.addItem(item)

    def set_item(self, name, color):
        text = name + ' (' + color + ')'
        icon = Util.color_icon(color)
        item = QListWidgetItem(icon, text)
        data = (name, color)
        item.setData(32, data)

        return item

    def add_color(self):
        name = self.name_edit.text()
        color = self.value_edit.text()
        item = self.set_item(name, color)
        self.color_list.addItem(item)

    def open_color_dialog(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.value_edit.setText(color.name())

    def delete_color(self):
        item = self.color_list.takeItem(self.color_list.currentRow())
        item = None

    def apply(self):
        current_items = Util.load_items()
        colors = {}
        for i in range(self.color_list.count()):
            name, color = self.color_list.item(i).data(32)
            colors[name] = color
        current_items['colors'] = colors

        Util.save_items(current_items)
        msg = QMessageBox()
        msg.setText('設定を適用しました')
        msg.exec_()