DATA_TYPE_INTEGER = 'integer'
DATA_TYPE_STRING = 'string'
DATA_TYPE_FLOAT = 'float'

# Default configurations for data handling
default_config = {
    'max_length': 255,
    'min_length': 1,
    'allowed_types': [DATA_TYPE_STRING, DATA_TYPE_INTEGER, DATA_TYPE_FLOAT],
}

# Common error messages for validation
ERROR_MESSAGES = {
    'type_error': 'Invalid data type',
    'length_error': 'Data length out of bounds',
}

# Status codes for data processing
STATUS_SUCCESS = 0
STATUS_FAILURE = 1
STATUS_PENDING = 2

# Function to get default configurations

def get_default_config():
    return default_config

# Function to retrieve error message by key

def get_error_message(key):
    return ERROR_MESSAGES.get(key, 'Unknown error')

# Function to validate data type

def validate_data_type(data, expected_type):
    actual_type = type(data).__name__
    if actual_type == expected_type:
        return True
    return False