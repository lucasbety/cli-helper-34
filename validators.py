def validate_positive_integer(value):
    """Validates if the provided value is a positive integer."""
    if not isinstance(value, int):
        raise ValueError("Input must be an integer.")
    if value <= 0:
        raise ValueError("Input must be a positive integer.")
    return True


def validate_non_empty_string(value):
    """Validates if the provided value is a non-empty string."""
    if not isinstance(value, str):
        raise ValueError("Input must be a string.")
    if not value.strip():
        raise ValueError("Input must be a non-empty string.")
    return True


def validate_email_format(email):
    """Validates if the provided email has a valid format."""
    import re
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not isinstance(email, str):
        raise ValueError("Input must be a string.")
    if not re.match(email_regex, email):
        raise ValueError("Input must be a valid email address.")
    return True


# Example usage
if __name__ == '__main__':
    try:
        validate_positive_integer(-5)
    except ValueError as e:
        print(e)

    try:
        validate_non_empty_string('  ')
    except ValueError as e:
        print(e)

    try:
        validate_email_format('invalid-email')
    except ValueError as e:
        print(e)