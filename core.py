import json
import os

class ConfigLoader:
    def __init__(self, defaults=None):
        if defaults is None:
            defaults = {}
        self.defaults = defaults
        self.config = self.defaults.copy()  # Start with defaults

    def load(self, filepath):
        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                file_config = json.load(file)
                self.config.update(file_config)  # Update with file settings
        else:
            print(f'Configuration file {filepath} not found. Using defaults.')  

    def get(self, key, default=None):
        return self.config.get(key, default)

    def __str__(self):
        return json.dumps(self.config, indent=4)

# Example usage
if __name__ == '__main__':
    defaults = {
        'host': 'localhost',
        'port': 8080,
        'debug': False
    }
    config_loader = ConfigLoader(defaults)
    config_loader.load('config.json')  # Assumes config.json is defined
    print(config_loader)