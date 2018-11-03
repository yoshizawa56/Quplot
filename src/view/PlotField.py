#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
プロット設定の入力用Widget
'''

__author__ = "T.Yoshizawa <toru.yoshi.5.1@gmail.com>"
__status__ = "production"
__version__ = "0.1.0"
__date__    = "02 November 2018"

from PyQt5.QtWidgets import QWidget, QPushButton

from .GeneralSetting import GeneralSetting
from .DataTab import DataTab
from .AxisSetting import AxisSetting
from .Canvas import Canvas
from ..logic.Util import Util
from ..logic.Plot import Plot


class PlotField(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setup_ui()

        #TODO connect系の処理
        self.plot_button.clicked.connect(self.plot)

        #テスト用
        d = Util.load_default_config()
        self.setting.set_default_config(d)
        
    def setup_ui(self):
        #左側
        self.data_tab = DataTab()
        self.x_axis = AxisSetting('X')
        self.y_axis = AxisSetting('Y')
        self.plot_button = QPushButton('Plot!!')
        #TODO Widgetの追加
        left_widgets = [
            self.data_tab,
            Util.Hbox([self.x_axis, self.y_axis]),
            self.plot_button
        ]
        
        #右側
        #TODO Widgetの追加
        self.setting = GeneralSetting()
        self.canvas = Canvas()
        right_widgets = [
            self.setting,
            self.canvas.canvas
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
            self.setting
        ]

    def config_dict(self):
        config = {}
        for widget in self.widget_list:
            config.update(widget)

        return config

    def set_default_config(self, default_config_dict):
        for widget in self.widget_list:
            widget.set_default_config(default_config_dict)

    def plot(self):
        Plot.execute(self.canvas, [])
