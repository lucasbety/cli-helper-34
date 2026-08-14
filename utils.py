import os
import json

def read_json(file_path):
    """Read a JSON file and return its content."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} not found")
    with open(file_path, 'r') as file:
        return json.load(file)


def write_json(file_path, data):
    """Write Python dictionary to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def create_directory(dir_path):
    """Create a directory if it doesn’t exist."""
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def list_files(directory):
    """List all files in a given directory."""
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]


def current_timestamp():
    """Return the current timestamp as a string."""
    from datetime import datetime
    return datetime.now().isoformat()