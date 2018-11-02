'''
plotを実行するクラス
'''

__author__ = "T.Yoshizawa <toru.yoshi.5.1@gmail.com>"
__status__ = "production"
__version__ = "0.1.0"
__date__    = "02 November 2018"

import numpy as np


class Plot:
    #Canvasクラスとconfig_dictを受け取り、プロットを実行
    @staticmethod
    def execute(canvas, config_dict):
        axes = canvas.axes

        #TODO プロットの処理(以下は仮置き)
        x = np.arange(0, 1, 0.1)
        y = np.sin(x)
        axes.plot(x,y, '-')

        #結果の出力
        canvas.canvas.draw()