'''
plotを実行するクラス
'''

__author__ = "T.Yoshizawa <toru.yoshi.5.1@gmail.com>"
__version__ = "0.9.0"
__date__    = "14 November 2018"

import numpy as np
from matplotlib import pyplot as plt
from PyQt5.QtWidgets import QMessageBox


class Plot:
    #Canvasクラスとconfig_dictを受け取り、プロットを実行
    @staticmethod
    def execute(canvas, config_dict):
        plt.rcParams["mathtext.fontset"] = 'cm'
        plt.rcParams["font.family"] = 'Times New Roman'

        #長いから省略名を設定
        axes = canvas.axes
        c = config_dict

        #axesを初期化
        canvas.axes.clear()

        #データを読み込んでプロット
        for conf in c['tab'].values():
            #データソースがファイルの場合
            if conf['data_type'] == 'File':
                #ファイル名がない場合はスキップ
                if not conf.get('file', False):
                    continue

                try:
                    data = np.loadtxt(conf['file'])
                except IOError:
                    msg = QMessageBox()
                    msg.setText('ファイルが開けませんでした')
                    msg.exec_()
                    return

                x = []
                y = []
                for line in data:
                    x.append(line[int(config_dict['X_axis']['index'])])
                    y.append(line[int(config_dict['Y_axis']['index'])])

            #データソースがFunctionの場合
            elif conf['data_type'] == 'Function':
                #functionがない場合はスキップ
                if not conf.get('function', False):
                    continue

                #xの範囲を定義
                if conf.get('function_range', False):
                    min, max = conf['function_range'].split(':')
                    min, max = float(min), float(max)
                elif c['X_axis'].get('range', False):
                    min, max = c['X_axis']['range'].split(':')
                    min, max = float(min), float(max)
                else:
                    msg = QMessageBox()
                    msg.setText('Functionの定義域が定まりませんでした。\n Rangeを記述してください。')
                    msg.exec_()
                    return

                x = np.arange(min, max, (max-min)/1000)

                #function領域に書かれているコードを実行してyのデータを構築
                y = eval(conf['function'])

            #plotのオプションを構築
            options = {}

            #legendのlabel設定
            if conf.get('legend', False):
                label = conf['legend'].replace(u"\xa5", "\\")
                if conf['legend_style'] == 'LaTeX':
                    label = '$' + label + '$'
                options.update(label=label)

            #lineの設定
            options.update(linestyle=conf['linestyle'])
            if conf['line_color'] != 'Auto':
                options.update(color=conf['line_color'])
            options.update(linewidth=conf['line_width'])

            #markerの設定(Functionの場合にはないため省略)
            options.update(marker=conf['marker'])
            if conf['marker_color'] != 'Auto':
                options.update(markerfacecolor=conf['marker_color'])
                options.update(markeredgecolor=conf['marker_color'])
            options.update(markersize=conf['marker_size'])

            #プロット実行
            axes.plot(x, y, **options)

        #fig全体の設定

        #軸の設定
        for axis in ['X', 'Y']:
            conf = c[axis + '_axis']

            #ラベルの設定
            if conf.get('title', False):
                label = conf['title'].replace(u"\xa5", "\\")
                if conf['style'] == 'LaTeX':
                    label = '$' + label + '$'
                else:
                    font = 'Arial'
                if axis == 'X':
                    axes.set_xlabel(label, fontsize=conf['font'])
                else:
                    axes.set_ylabel(label, fontsize=conf['font'])

            #rangeとscaleの設定
            if conf.get('range', False):
                min, max = conf['range'].split(':')
                min, max = float(min), float(max)
                if axis == 'X':
                    axes.set_xlim(min, max)
                else:
                    axes.set_ylim(min, max)

            if conf.get('scale', False):
                if axis == 'X':
                    axes.set_xscale(conf['scale'])
                else:
                    axes.set_yscale(conf['scale'])


        #titleの設定
        if c.get('title', False):
            axes.set_title(c['title'], fontsize=c['title_font'])

        #legendの設定
        if config_dict['legend_status'] == 'enable':
            axes.legend(loc=c['legend_position'], fontsize=c['legend_font'])
            
        #Tickフォントサイズの設定
        axes.tick_params(labelsize=c['tick_font'])

        #結果の出力
        canvas.fig.tight_layout()
        canvas.canvas.draw()