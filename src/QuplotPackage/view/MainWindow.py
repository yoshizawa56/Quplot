#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
MainWindowのWidget
'''

__author__ = "T.Yoshizawa <toru.yoshi.5.1@gmail.com>"
__version__ = "0.9.0"
__date__    = "14 November 2018"

import sys
from PyQt5.QtWidgets import QMainWindow, QAction
from .PlotTab import PlotTab
from ..config.SubWindow import SubWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.plot_tab = PlotTab()
        self.setCentralWidget(self.plot_tab)

        menubar = self.menuBar()
        app_menu = menubar.addMenu('&Quplot')

        #defaultコンフィグ
        config_action = QAction('&Default value config', self)
        config_action.triggered.connect(self.open_default_config)
        app_menu.addAction(config_action)

        #marker color設定
        color_action = QAction('&Colors and Markers', self)
        color_action.triggered.connect(self.open_color_config)
        app_menu.addAction(color_action)

        self.move(160,40)

    def open_default_config(self):
        config_tab = SubWindow('default')
        config_tab.show()
        self.reset()

    def open_color_config(self):
        config_tab = SubWindow('color')
        config_tab.show()
        self.reset()

    def reset(self):
        self.plot_tab = None
        self.setCentralWidget(None)
        self.close()
        self.__init__()
        self.show()
