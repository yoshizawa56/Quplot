#!/usr/bin/python
# -*- coding: utf-8 -*-
#widgetのテスト用プログラム

import sys
from PyQt5.QtWidgets import QMainWindow, QAction
from .myPackage.view.PlotTab import PlotTab
from .myPackage.config.SubWindow import SubWindow

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

    def open_default_config(self):
        config_tab = SubWindow('default')
        config_tab.show()
        self.reset()

    def open_color_config(self):
        config_tab = SubWindow('color')
        config_tab.show()
        self.reset()

    def reset(self):
        self.__init__()
