import json
import os

class ConfigLoader:
    def __init__(self, default_config_file='default_config.json', user_config_file='user_config.json'):
        self.default_config_file = default_config_file
        self.user_config_file = user_config_file
        self.config = self.load_config()

    def load_config(self):
        default_config = self.load_json(self.default_config_file)
        user_config = self.load_json(self.user_config_file)
        final_config = {**default_config, **user_config}
        return final_config

    def load_json(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                return json.load(file)
        return {}

    def get(self, key, default=None):
        return self.config.get(key, default)

if __name__ == '__main__':
    config_loader = ConfigLoader()
    print(config_loader.get('some_key', 'default_value'))