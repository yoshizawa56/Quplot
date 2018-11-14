#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
markerのlistを表示・編集するWidget
'''

__author__ = "T.Yoshizawa <toru.yoshi.5.1@gmail.com>"
__status__ = "production"
__version__ = "0.1.0"
__date__    = "13 November 2018"

from PyQt5.QtWidgets import (QWidget, QListWidget, QListWidgetItem, QGroupBox, 
                    QLabel, QLineEdit, QPushButton, QHBoxLayout,
                    QMessageBox, QAbstractItemView)
from ..logic.Util import Util
import os

class MarkerConfig(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setup_ui()

        self.add_button.clicked.connect(self.add_marker)
        self.delete_button.clicked.connect(self.delete_marker)
        self.apply_button.clicked.connect(self.apply)

        self.marker_list.setAcceptDrops(True)
        self.marker_list.setDragEnabled(True)
        self.marker_list.setDragDropOverwriteMode(False)
        self.marker_list.setDragDropMode(QAbstractItemView.InternalMove)

    def setup_ui(self):
        #marker追加用入力領域（左側）
        add_marker_box = QGroupBox('Add new marker')

        #name
        name_label = QLabel('New marker name : ')
        self.name_edit = QLineEdit()
        name_widgets = [
            name_label,
            self.name_edit
        ]

        #value
        value_label = QLabel('Value : ')
        self.value_edit = QLineEdit()
        value_widgets = [
            value_label,
            self.value_edit
        ]

        #add button
        self.add_button = QPushButton('Add')

        #左側のレイアウト
        add_marker_box.setLayout(
            Util.Vlayout(
                [
                    Util.Hbox(name_widgets),
                    Util.Hbox(value_widgets),
                    self.add_button
                ]
            )
        )

        #markerのリスト（右側）
        self.marker_list = QListWidget()
        self.set_marker_list(self.marker_list)
        
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
                self.marker_list,
                delete_widget
            ]
        )

        #全体を配置
        self.setLayout(
            Util.Hlayout(
                [
                    add_marker_box,
                    right_box
                ]
            )
        )

    def set_marker_list(self, marker_list):
        markers = Util.load_items()['markers']
        for name, marker in markers.items():
            item = self.set_item(name, marker)
            marker_list.addItem(item)

    def set_item(self, name, marker):
        text = name + ' : ' + marker
        item = QListWidgetItem(text)
        data = (name, marker)
        item.setData(32, data)

        return item

    def add_marker(self):
        name = self.name_edit.text()
        marker = self.value_edit.text()
        item = self.set_item(name, marker)
        self.marker_list.addItem(item)

    def delete_marker(self):
        item = self.marker_list.takeItem(self.marker_list.currentRow())
        item = None

    def apply(self):
        current_items = Util.load_items()
        markers = {}
        for i in range(self.marker_list.count()):
            name, marker = self.marker_list.item(i).data(32)
            markers[name] = marker
        current_items['markers'] = markers

        Util.save_items(current_items)
        msg = QMessageBox()
        msg.setText('設定を適用しました')
        msg.exec_()