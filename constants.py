import json
import os

DEFAULT_CONFIG = {
    'setting1': 'value1',
    'setting2': 'value2',
    'setting3': True,
}

CONFIG_FILE = 'config.json'


def load_config():
    """Load configuration from a JSON file.
    If the file does not exist, use default values.
    """
    if os.path.isfile(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            try:
                config = json.load(f)
                return {**DEFAULT_CONFIG, **config}
            except json.JSONDecodeError:
                print('Error decoding JSON, using default config.')
                return DEFAULT_CONFIG
    else:
        print('Config file not found, using default config.')
        return DEFAULT_CONFIG
