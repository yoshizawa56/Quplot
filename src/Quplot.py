#!/usr/bin/python
# -*- coding: utf-8 -*-
#Quplotの起動プログラム

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from QuplotPackage.view.MainWindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()

    main_window.show()
    sys.exit(app.exec_())