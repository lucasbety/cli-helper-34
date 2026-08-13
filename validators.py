import re

# Compile patterns for performance
email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
phone_pattern = re.compile(r'^(\+?[1-9]{1,4})?[-.\s]?\(?[2-9][0-9]{2}\)?[-.\s]?[0-9]{3}[-.\s]?[0-9]{4}$')

def validate_email(email):
    """Validate if the input is a valid email address."""
    return bool(email_pattern.match(email))

def validate_phone(phone):
    """Validate if the input is a valid phone number."""
    return bool(phone_pattern.match(phone))

# Example test cases
if __name__ == '__main__':
    print(validate_email('test@example.com'))  # Expected: True
    print(validate_email('invalid-email'))      # Expected: False
    print(validate_phone('+123-456-7890'))      # Expected: True
    print(validate_phone('123-45-6789'))        # Expected: False