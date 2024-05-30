import os
import yaml


class MasterConfig:
    _instance = None
    _config_loaded = False

    def __new__(cls, config_file=None):
        if cls._instance is None:
            cls._instance = super(MasterConfig, cls).__new__(cls)
            cls._instance.config_file = config_file if config_file else 'default_config.yaml'
            cls._instance.config = cls._instance.load_config()
        return cls._instance

    def load_config(self):
        """加载配置文件"""
        try:
            with open(self.config_file, 'r', encoding='utf-8') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            print(f"配置文件 {self.config_file} 未找到。")
            return {}
        except Exception as e:
            print(f"加载配置文件时出错: {e}")
            return {}

    def get_config(self, section, *keys, default=None):
        """从指定的section和key中读取配置项"""
        config = self.config.get(section, {})
        for key in keys:
            config = config.get(key, {})
        return config if config else default

    
    def set_config(self, section, *keys, value, write_to_file=False):
        """设置配置项，可选写入到文件"""
        config = self.config.setdefault(section, {})
        for key in keys[:-1]:
            config = config.setdefault(key, {})
        config[keys[-1]] = value

        if write_to_file:
            self.write_config()

    def write_config(self):
        """将当前配置写入到文件"""
        try:
            with open(self.config_file, 'w') as file:
                yaml.dump(self.config, file, default_flow_style=False)
        except Exception as e:
            print(f"写入配置文件时出错: {e}")
            raise


class MasterConfig1:
    _instance = None
    _config_loaded = False

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            if kwargs.get('config_file'):
                cls._instance.config_file = kwargs.get('config_file')
            else:
                cls._instance.config_file = None
            cls._instance.config = cls._instance.load_config()
            cls._config_loaded = True
        return cls._instance

    def __init__(self, *args, **kwargs):
        if not self._config_loaded:
            self.config_file = None
            self.config = self.load_config()

    def load_config(self):
        if not self.config_file:
            root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            self.config_file = os.path.join(root_dir, 'conf', 'config.yaml')
        try:
            with open(self.config_file, 'r') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            raise Exception(f"Configuration file {self.config_file} not found!")

    def write_config(self, config_data, file_path=None):
        """
        将配置数据写入到 YAML 文件。

        :param config_data: 要写入的配置数据
        :param file_path: 配置文件的路径，如果为 None，则使用初始化时的路径
        """
        if not file_path:
            file_path = self.config_file

        if not file_path:
            raise ValueError("未提供配置文件路径")

        try:
            with open(file_path, 'w') as file:
                yaml.dump(config_data, file)
        except Exception as e:
            print(f"写入配置文件时出错: {e}")
            raise
        
    def get_config_obj(self):
        return self.config

    def get_config(self, section, *keys, default=None):
        dict_ = self.config
        if not dict_:
            return default
        
        keys = [section] + list(keys)
        for key in keys:
            dict_ = dict_.get(key, {})
            if dict_ is None or dict_ == {}:
                return default
        
        return dict_
    
    
    