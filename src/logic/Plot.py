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
        #データの読み込み
        for i in range(20):
            if config_dict.get('data' + str(i), False):
                conf = config_dict['data' + str(i)]
                #データソースがファイルの場合
                if conf['data_type'] == 'File':
                    try:
                        data = np.loadtxt(conf['file'])
                    except IOError as e:
                        QMessageBox.warning(w, "Message", u"File can't open !")
                        return

                    x = []
                    y = []
                    for line in data:
                        x.append(line[int(config_dict['X_axis']['index'])])
                        y.append(line[int(config_dict['Y_axis']['index'])])

                    axes.plot(x,y)

                #データソースがFunctionの場合
                else:
                    print('test')

        # x = np.arange(0, 1, 0.1)
        # y = np.sin(x)
        # axes.plot(x,y, '-')

        #結果の出力
        canvas.canvas.draw()