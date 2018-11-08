'''
Utilクラス
'''

__author__ = "T.Yoshizawa <toru.yoshi.5.1@gmail.com>"
__status__ = "production"
__version__ = "0.1.0"
__date__    = "06 November 2018"

import json
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout,
                            QLineEdit, QCheckBox, QComboBox,
                            QComboBox)
from PyQt5
import os

class Util:
    #入力領域にデフォルトの値をセット
    @staticmethod
    def set_default(default_config_dict, contents):
        for key, widget in contents:
            #デフォルト設定に含まれているパラメータのみ設定
            if default_config_dict.get(key, False):
                value = default_config_dict[key]
                if type(widget) == QLineEdit:
                    widget.setPlaceholderText(value)
                elif type(widget) == QCheckBox:
                    if value == 'enable':
                        widget.setCheckState(2)
                    elif value == 'disable':
                        widget.setCheckState(0)
                elif type(widget) == QComboBox:
                    widget.setCurrentIndex(widget.findData(value))

    #入力領域に設定値をセット
    @staticmethod
    def set_config(config_dict, contents):
        for key, widget in contents:
            #設定に含まれているパラメータのみ設定
            if config_dict.get(key, False):
                value = config_dict[key]
                if type(widget) == QLineEdit:
                    widget.setText(value)
                elif type(widget) == QCheckBox:
                    if value == 'enable':
                        widget.setCheckState(2)
                    elif value == 'disable':
                        widget.setCheckState(0)
                elif type(widget) == QComboBox:
                    widget.setCurrentIndex(widget.findData(value))

    #contentsのリストから設定Dictを出力
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

    #設定ファイルで入力がない部分をデフォルト値で補完
    @staticmethod
    def fill_by_default(config_dict, default_config_dict):
        config = config_dict
        for key, default in default_config_dict.items():
            #keyが'data'の場合には、すべてのdataタブにデフォルト設定を適用
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

    #デフォルト設定ファイルを読み込む。
    #デフォルト設定ファイルが破損していないか、マスターファイルと比較
    @staticmethod
    def load_default_config():
        base = os.path.dirname(os.path.abspath(__file__))
        default_file = os.path.normpath(os.path.join(base, '../../settings/default.json'))
        with open(default_file) as f:
            default_config_dict = json.load(f)

        #TODO マスターファイルの実装
        # master_file = 'master.json'
        # with open(master_file) as f:
        #     master_config_dict = json.load(f)
        
        # for key, val in master_config_dict:
        #     if default_config_dict.get(key, None) == None:
        #         default_config_dict[key] = val

        return default_config_dict

    #itemsファイルを読み込む
    @staticmethod
    def load_items():
        base = os.path.dirname(os.path.abspath(__file__))
        items_file = os.path.normpath(os.path.join(base, '../../settings/items.json'))
        with open(items_file) as f:
            items = json.load(f)
        return items

    #
    @staticmethod
    def load_config(filename):
        with open(filename) as f:
            return json.load(f)

    @staticmethod
    def save_export_file(filename, config_dict):
        #文字列をExportファイルで出力
        if filename != '':
            with open(filename, 'w') as f:
                f.write(json.dumps(config_dict, indent=4))

    #Widgetのリストを受け取り、QHBoxLayoutにセットして返す
    @staticmethod
    def Hlayout(widget_list):
        layout = QHBoxLayout()
        #layout.setContentsMargin(0,0,0,0)
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
        #Hbox_widget.setContentsMargins(0,0,0,0)
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
            combo.addItem(key, value)





