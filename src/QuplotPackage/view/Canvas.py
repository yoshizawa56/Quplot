#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
プロット全体に関わる設定の入力用Widget
'''

__author__ = "T.Yoshizawa <toru.yoshi.5.1@gmail.com>"
__version__ = "0.9.0"
__date__    = "14 November 2018"

import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QWidget

class Canvas(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setup_ui()

        #self.canvas.mpl_connect('button_press_event', self.show_window)

    def setup_ui(self):
        self.fig = plt.Figure()
        self.axes = self.fig.add_subplot(111)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setFixedSize(420,340)