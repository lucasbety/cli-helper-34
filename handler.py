import json
from typing import Any, Dict


def load_json(file_path: str) -> Dict[str, Any]:
    """Load JSON data from a file and return as a dictionary."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Could not decode JSON from file: {file_path}")


def save_json(data: Dict[str, Any], file_path: str) -> None:
    """Save a dictionary as JSON to a file."""
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError:
        raise IOError(f"Could not write to file: {file_path}")


def update_json(file_path: str, new_data: Dict[str, Any]) -> None:
    """Update a JSON file with new data while preserving existing data."""
    data = load_json(file_path)
    data.update(new_data)
    save_json(data, file_path)
