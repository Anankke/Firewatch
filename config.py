import os
import yaml
from collections import UserDict


class DotDict(UserDict):
    def __getattr__(self, item):
        if item in self.data:
            result = self.data[item]
            if type(result) == dict:
                result = DotDict(result)
            return result
        raise AttributeError("'{}' dose not exist".format(item))


class Config:
    def __init__(self, config_name: str = "config.yaml"):
        self.__config = self.__get_config(config_name)

    def __getattr__(self, item):
        return self.__config.__getattr__(item)

    def __get_config(self, config_name: str) -> DotDict:
        abs_path = os.path.join(os.path.dirname(__file__), config_name)
        return DotDict(yaml.safe_load(open(abs_path)))


CONFIG = Config()
