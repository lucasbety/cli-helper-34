def safe_divide(numerator, denominator):
    """
    Safely divide two numbers with error handling for edge cases.
    """
    try:
        if not isinstance(numerator, (int, float)) or not isinstance(denominator, (int, float)):
            raise TypeError('Both numerator and denominator must be numbers.')
        if denominator == 0:
            raise ZeroDivisionError('Denominator cannot be zero.')
        return numerator / denominator
    except TypeError as te:
        print(f'Error: {te}')
        return None
    except ZeroDivisionError as zde:
        print(f'Error: {zde}')
        return None


def parse_int(value):
    """
    Parse an integer from a string, handling edge cases.
    """
    try:
        return int(value)
    except ValueError:
        print(f'Error: Unable to convert {value} to an integer.')
        return None


def load_data(file_path):
    """
    Load data from a JSON file with error handling.
    """
    try:
        with open(file_path, 'r') as file:
            import json
            return json.load(file)
    except FileNotFoundError:
        print(f'Error: File {file_path} not found.')
        return None
    except json.JSONDecodeError:
        print('Error: File is not a valid JSON.')
        return None
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
        return None
