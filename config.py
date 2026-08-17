import json
import os

DEFAULT_CONFIG = {
    'setting1': 'value1',
    'setting2': 10,
    'setting3': True
}

class ConfigLoader:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.configuration = self.load_configuration()

    def load_configuration(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as file:
                try:
                    user_config = json.load(file)
                    return self.merge_configs(DEFAULT_CONFIG, user_config)
                except json.JSONDecodeError:
                    print('Error reading the configuration file. Using defaults.')
        return DEFAULT_CONFIG

    def merge_configs(self, default, user):
        config = default.copy()  # start with the default config
        config.update(user)      # update with user config
        return config

# Usage example:
# loader = ConfigLoader()
# print(loader.configuration)  # Outputs the merged config