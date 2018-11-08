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
        file_menu = menubar.addMenu('&File')
        config_action = QAction('&Default config', self)
        config_action.triggered.connect(self.open_config)
        file_menu.addAction(config_action)

    def open_config(self):
        config_tab = SubWindow()
        config_tab.show()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     test_widget = PlotTab()

#     main_window = QMainWindow()
#     main_window.setWindowTitle("GUI Plot Test")
#     main_window.setCentralWidget(test_widget)
#     main_window.resize(100,300)
    

#     main_window.show()
#     sys.exit(app.exec_())