'''
plotを実行するクラス
'''

__author__ = "T.Yoshizawa <toru.yoshi.5.1@gmail.com>"
__status__ = "production"
__version__ = "0.1.0"
__date__    = "06 November 2018"

import numpy as np
from matplotlib import pyplot as plt


class Plot:
    #Canvasクラスとconfig_dictを受け取り、プロットを実行
    @staticmethod
    def execute(canvas, config_dict):
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
                    print('error')
                    #QMessageBox.warning(w, "Message", u"File can't open !")
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
                else:
                    #実装
                    print('test')

                # min, max = 0, 300
                x = np.arange(min, max, (max-min)/500)

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
            if conf['linestyle'] != 'None':
                options.update(linestyle=conf['linestyle'])
            if conf['line_color'] != 'Auto':
                options.update(color=conf['line_color'])
            options.update(linewidth=conf['line_width'])

            #markerの設定(Functionの場合にはないため省略)
            if conf.get('marker', 'None') != 'None':
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
                    font = 'serif'
                else:
                    font = 'Times New Roman'
                if axis == 'X':
                    axes.set_xlabel(label, fontsize=conf['font'], fontname=font)
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