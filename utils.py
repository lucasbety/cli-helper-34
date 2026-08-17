import json

class FileReadError(Exception):
    pass

class JSONDecodeError(Exception):
    pass


def read_json_file(file_path):
    """Reads a JSON file and returns its content as a Python dictionary."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        raise FileReadError(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise JSONDecodeError(f"JSON decode error in file: {file_path}")
    except Exception as e:
        raise FileReadError(f"An error occurred: {str(e)}")


def write_json_file(file_path, data):
    """Writes a Python dictionary to a JSON file."""
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except Exception as e:
        raise FileReadError(f"An error occurred while writing to {file_path}: {str(e)}")


def validate_data(data):
    """Validates that the data is a dictionary before processing."""
    if not isinstance(data, dict):
        raise ValueError("Data must be a dictionary.")

        