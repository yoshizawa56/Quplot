#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
プロット設定の入力用Widget
'''

__author__ = "T.Yoshizawa <toru.yoshi.5.1@gmail.com>"
__status__ = "production"
__version__ = "0.1.0"
__date__    = "06 November 2018"

from PyQt5.QtWidgets import QWidget, QPushButton, QFileDialog
import os
from .GeneralSetting import GeneralSetting
from .DataTab import DataTab
from .AxisSetting import AxisSetting
from .Canvas import Canvas
from .SaveFigure import SaveFigure
from ..logic.Util import Util
from ..logic.Plot import Plot


class PlotField(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setup_ui()

        self.plot_button.clicked.connect(self.plot)
        self.setting.export_button.clicked.connect(self.export_plot)
        self.setting.import_last_button.clicked.connect(self.import_last_plot)
        self.setting.import_button.clicked.connect(self.import_plot)

        #デフォルト設定を適用
        self.set_default_config(Util.load_config())

    def setup_ui(self):
        #左側
        self.data_tab = DataTab(self)
        self.x_axis = AxisSetting('X')
        self.y_axis = AxisSetting('Y')
        self.plot_button = QPushButton('Plot!!')
        left_widgets = [
            self.data_tab,
            Util.Hbox([self.x_axis, self.y_axis]),
            self.plot_button
        ]
        
        #右側
        self.setting = GeneralSetting()
        self.canvas = Canvas()
        self.save_figure = SaveFigure(self)
        right_widgets = [
            self.setting,
            self.canvas.canvas,
            self.save_figure
        ]

        #子Widgetをセット
        self.setLayout(
            Util.Hlayout(
                [
                    Util.Vbox(left_widgets),
                    Util.Vbox(right_widgets)
                ]
            )
        )

        #設定を扱うwidgetのリスト
        self.widget_list = [
            self.data_tab,
            self.x_axis,
            self.y_axis,
            self.setting,
            self.save_figure
        ]

    def export_plot(self):
        filename = QFileDialog.getSaveFileName(self, "Open file")
        if filename[0] != '':
            Util.save_config(self.config_dict(), filename[0])

    def import_plot(self):
        filename = QFileDialog.getOpenFileName(self, "Open file")
        if filename[0] != '':
            try:
                config = Util.load_config(filename[0])
                self.set_config(config)
            except IOError:
                msg = QMessageBox()
                msg.setText('ファイルが開けませんでした')
                msg.exec_()

    def import_last_plot(self):
        self.set_config(Util.load_config(filename), 'last')

    def config_dict(self):
        config = {}
        for widget in self.widget_list:
            config.update(widget.config_dict())

        return config

    def set_default_config(self, default_config_dict):
        for widget in self.widget_list:
            widget.set_default_config(default_config_dict)

    def set_config(self, config_dict):
        for widget in self.widget_list:
            widget.set_config(config_dict)

    def plot(self):
        Util.save_config(self.config_dict(), 'last')
        config = Util.fill_by_default(self.config_dict(), Util.load_config())
        
        Plot.execute(self.canvas, config)
