import json
from typing import Any, Dict, List


def load_json(file_path: str) -> Dict[str, Any]:
    """Load JSON data from a file."""
    with open(file_path, 'r') as f:
        return json.load(f)


def save_json(data: Dict[str, Any], file_path: str) -> None:
    """Save data as JSON to a file."""
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)


def filter_data(data: List[Dict[str, Any]], key: str, value: Any) -> List[Dict[str, Any]]:
    """Filter a list of dictionaries by a key-value pair."""
    return [item for item in data if item.get(key) == value]


def merge_dicts(*dicts: Dict[str, Any]) -> Dict[str, Any]:
    """Merge multiple dictionaries into one."""
    merged = {}
    for d in dicts:
        merged.update(d)
    return merged


def pretty_print_json(data: Dict[str, Any]) -> None:
    """Print formatted JSON data to the console."""
    print(json.dumps(data, indent=4))
