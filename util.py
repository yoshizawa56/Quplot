import json

'''
入力領域にデフォルトの値をセット
'''
def set_default(default_config_dict, target_list):
    for key, target in target_list:
        try:
            target(default_config_dict[key])
        except KeyError:
            #do something

'''
設定ファイルで入力がない部分をデフォルト値で補完
'''
def fill_by_default(default_config_dict, config_dict):
    for key, default in default_config_dict:
        if(config_dict.get(key, None) == None):
            config_dict[key] = default

'''
デフォルト設定ファイルを読み込む。
デフォルト設定ファイルが破損していないか、マスターファイルと比較
'''
def load_default_config():
    default_file = 'default.json'
    with open(default_file) as f:
        default_config_dict = json.load(f)
    
    master_file = 'master.json'
    with open(master_file) as f:
        master_config_dict = json.load(f)
    
    for key, val in master_config_dict:
        if default_config_dict.get(key, None) == None:
            default_config_dict[key] = val
    
    return default_config_dict

