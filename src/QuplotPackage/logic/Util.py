'''
Utilクラス
'''

__author__ = "T.Yoshizawa <toru.yoshi.5.1@gmail.com>"
__status__ = "production"
__version__ = "0.1.0"
__date__    = "14 November 2018"

import json
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout,
                            QLineEdit, QCheckBox, QComboBox,
                            QComboBox, QMessageBox)
from PyQt5.QtGui import QIcon, QPainter, QPixmap, QBrush, QColor
import os
import sys

class Util:
    #入力領域に設定値をセット
    #modeに何らかの文字列（'default'を推奨）がセットされている場合はデフォルト設定
    @staticmethod
    def set_config(config_dict, contents, mode=''):
        for key, widget in contents:
            #設定に含まれているパラメータのみ設定
            if config_dict.get(key, False):
                value = config_dict[key]
                if type(widget) == QLineEdit:
                    if mode == '':
                        widget.setText(value)
                    else:
                        widget.setPlaceholderText(value)
                elif type(widget) == QCheckBox:
                    if value == 'enable':
                        widget.setCheckState(2)
                    elif value == 'disable':
                        widget.setCheckState(0)
                elif type(widget) == QComboBox:
                    widget.setCurrentIndex(widget.findData(value))

    #ファイルを読み込んで、dict形式でreturnする
    #filenameを省略した場合はdefault.jsonを読み込む
    @staticmethod
    def load_config(filename = ''):
        base = os.path.dirname(os.path.abspath(__file__))
        if filename == '':
            filename = os.path.normpath(os.path.join(base, './settings/default.json'))
        elif filename == 'last':
            filename = os.path.normpath(os.path.join(base, './settings/last_plot.json'))
        with open(filename) as f:
            return json.load(f)

    #config_dictをもとに設定ファイルを作成して保存
    #filenameを省略した場合は、default.jsonに保存
    @staticmethod
    def save_config(config_dict, filename=''):
        #文字列をExportファイルで出力
        base = os.path.dirname(os.path.abspath(__file__))
        if filename == '':
            filename = os.path.normpath(os.path.join(base, './settings/default.json'))
        elif filename == 'last':
            filename = os.path.normpath(os.path.join(base, './settings/last_plot.json'))
        try:
            with open(filename, 'w') as f:
                f.write(json.dumps(config_dict, indent=4))
        except IOError:
            msg = QMessageBox()
            msg.setText('ファイルが開けませんでした')
            msg.exec_()

    #contentsのリストから設定dictを出力
    @staticmethod
    def config_dict(contents):
        dict = {}
        for key, widget in contents:
            if type(widget) == QLineEdit:
                #入力が空の場合はデフォルト値を使うため、辞書に追加しない
                if str(widget.text()) == '':
                    continue
                tmp = widget.text()
            elif type(widget) == QCheckBox:
                if widget.checkState() == 2:
                    tmp = 'enable'
                elif widget.checkState() == 0:
                    tmp = 'disable'
            elif type(widget) == QComboBox:
                tmp = widget.itemData(widget.currentIndex())
            dict[key] = tmp

        return dict

    #itemsファイルを読み込む
    @staticmethod
    def load_items():
        base = os.path.dirname(os.path.abspath(__file__))
        items_file = os.path.normpath(os.path.join(base, './settings/items.json'))
        with open(items_file) as f:
            items = json.load(f)
        return items

    #itemsファイルに書き込む
    @staticmethod
    def save_items(items):
        base = os.path.dirname(os.path.abspath(__file__))
        items_file = os.path.normpath(os.path.join(base, './settings/items.json'))
        with open(items_file, 'w') as f:
            f.write(json.dumps(items, indent=4))

    #設定ファイルで入力がない部分をデフォルト値で補完
    @staticmethod
    def fill_by_default(config_dict, default_config_dict):
        config = config_dict
        for key, default in default_config_dict.items():
            #keyが'tab'の場合には、すべてのdataタブにデフォルト設定を適用
            if key == 'tab':
                data_default_config = default_config_dict['tab']['data']
                for key, conf in config_dict['tab'].items():
                    config['tab'][key] = Util.fill_by_default(conf, data_default_config)

            #辞書が入れ子になっている場合は再帰的にデフォルト設定を適用
            elif type(default) == dict:
                if config_dict.get(key, False):
                    config[key] = Util.fill_by_default(
                        config_dict[key],
                        default_config_dict[key])
            else:
                if not config_dict.get(key, False):
                    config[key] = default

        return config

    #Widgetのリストを受け取り、QHBoxLayoutにセットして返す
    @staticmethod
    def Hlayout(widget_list):
        layout = QHBoxLayout()
        for widget in widget_list:
            layout.addWidget(widget)
        layout.addStretch()
        return layout

    #Widgetのリストを受け取り、QVBoxLayoutにセットして返す
    @staticmethod
    def Vlayout(widget_list):
        layout = QVBoxLayout()
        layout.setSpacing(1)
        for widget in widget_list:
            layout.addWidget(widget)
        return layout

    #Widgetのリストを受け取り、QHBoxLayoutをセットしたWidgetを返す
    @staticmethod
    def Hbox(widget_list):
        Hbox_widget = QWidget()
        Hbox_widget.setLayout(Util.Hlayout(widget_list))
        return Hbox_widget

    #Widgetのリストを受け取り、QVBoxLayoutをセットしたWidgetを返す
    @staticmethod
    def Vbox(widget_list):
        Vbox_widget = QWidget()
        Vbox_widget.setLayout(Util.Vlayout(widget_list))
        return Vbox_widget

    #comboBoxで現在指定されているDataを表示
    @staticmethod
    def combo_data(combo):
        return combo.itemData(combo.currentIndex())

    #色指定用のcomboBoxをセット
    @staticmethod
    def set_color_combo(combo):
        combo.setMinimumWidth(120)
        #自動選択
        combo.addItem('Auto', 'Auto')

        #default.jsonから色のリストを取得してセット
        colors = Util.load_items()['colors']
        for key, value in colors.items():
            combo.addItem(Util.color_icon(value), key, value)


    #colorに対応する色の円のQIconを返す
    @staticmethod
    def color_icon(color):
        pix = QPixmap(50,50)
        pix.fill(QColor(color))

        return QIcon(pix)


    #linestyle指定用のcomboBoxをセット
    @staticmethod
    def set_line_style_combo(combo):
        combo.setMinimumWidth(80)
        #lineなし
        combo.addItem('None', 'None')

        #default.jsonから線のリストを取得してセット
        lines = Util.load_items()['lines']
        for key, value in lines.items():
            combo.addItem(key, value)

    #marker指定用のcomboBoxをセット
    @staticmethod
    def set_marker_style_combo(combo):
        combo.setMinimumWidth(80)
        #マーカーなし
        combo.addItem('None', 'None')

        #default.jsonからマーカのリストを取得してセット
        markers = Util.load_items()['markers']
        for key, value in markers.items():
            combo.addItem(key, value)





