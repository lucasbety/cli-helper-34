import re

class InputValidator:
    @staticmethod
    def validate_email(email: str) -> bool:
        """
        Validate an email address using a regex pattern.
        """
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    @staticmethod
    def validate_phone(phone: str) -> bool:
        """
        Validate a phone number format (e.g., (123) 456-7890).
        """
        pattern = r'^\(\d{3}\) \d{3}-\d{4}$'
        return re.match(pattern, phone) is not None

    @staticmethod
    def validate_username(username: str) -> bool:
        """
        Validate a username with specific rules: between 3-20 characters,
        only alphanumeric characters and underscores allowed.
        """
        pattern = r'^[a-zA-Z0-9_]{3,20}$'
        return re.match(pattern, username) is not None

# Example usage of validators
if __name__ == '__main__':
    print(InputValidator.validate_email('test@example.com'))  # True
    print(InputValidator.validate_phone('(123) 456-7890'))  # True
    print(InputValidator.validate_username('user_name123'))  # True
    