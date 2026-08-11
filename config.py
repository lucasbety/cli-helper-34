import json
import os

DEFAULTS = {
    'host': 'localhost',
    'port': 8080,
    'debug': False,
    'timeout': 30
}

class Configuration:
    def __init__(self, config_file=None):
        self.config = DEFAULTS.copy()  # Start with default values
        if config_file:
            self.load_config(config_file)

    def load_config(self, config_file):
        if os.path.exists(config_file):
            with open(config_file, 'r') as file:
                file_config = json.load(file)
                self.config.update(file_config)  # Update defaults with file values
        else:
            print(f'Configuration file {config_file} not found. Using defaults.')  # Warn when file not found

    def get(self, key):
        return self.config.get(key, None)  # Provide a way to retrieve config values

    def set(self, key, value):
        self.config[key] = value  # Provide a way to set config values

    def __str__(self):
        return json.dumps(self.config, indent=4)  # Nicely format config for output