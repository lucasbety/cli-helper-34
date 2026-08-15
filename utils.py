import json
from typing import Any, Dict, Union

class ValidationError(Exception):
    pass

def safe_json_loads(data: str) -> Union[Dict[str, Any], None]:
    try:
        return json.loads(data)
    except json.JSONDecodeError:
        print('Error: Invalid JSON input.')
        return None
    except Exception as e:
        print(f'Unexpected error: {e}')
        return None

def safe_divide(numerator: float, denominator: float) -> float:
    try:
        if denominator == 0:
            raise ValueError('Denominator cannot be zero.')
        return numerator / denominator
    except ValueError as ve:
        print(ve)
        return float('inf')  # Return infinity for division by zero
    except Exception as e:
        print(f'Unexpected error during division: {e}')
        return None

def validate_and_parse_config(config: Dict[str, Any]) -> Dict[str, Any]:
    required_keys = ['host', 'port', 'username']
    for key in required_keys:
        if key not in config:
            raise ValidationError(f'Missing required key: {key}')
    return config

# Example use of safe_json_loads and safe_divide
data = '{"key": "value"}'
parsed_data = safe_json_loads(data)
result = safe_divide(10, 0)

if parsed_data:
    print(parsed_data)
if result != float('inf'):
    print(f'Result: {result}')