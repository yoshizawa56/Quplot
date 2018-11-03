'''
Utilクラス
'''

__author__ = "T.Yoshizawa <toru.yoshi.5.1@gmail.com>"
__status__ = "production"
__version__ = "0.1.0"
__date__    = "02 November 2018"

import json
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout,
                            QLineEdit, QCheckBox, QComboBox)
import os

class Util:
    #入力領域にデフォルトの値をセット
    @staticmethod
    def set_default(default_config_dict, target_list):
        for key, target in target_list:
            value = default_config_dict[key]
            if type(target) == QLineEdit:
                target.setPlaceholderText(value)
            elif type(target) == QCheckBox:
                target.setCheckState(value)
            elif type(target) == QComboBox:
                target.setCurrentIndex(target.findData(value))

    #設定ファイルで入力がない部分をデフォルト値で補完
    @staticmethod
    def fill_by_default(default_config_dict, config_dict):
        for key, default in default_config_dict:
            if(config_dict.get(key, None) == None):
                config_dict[key] = default

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





