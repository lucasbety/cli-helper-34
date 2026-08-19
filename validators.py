import re

class ValidationError(Exception):
    pass

def validate_email(email):
    if not isinstance(email, str):
        raise ValidationError('Email must be a string')
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(regex, email):
        raise ValidationError('Invalid email format')
    return True


def validate_age(age):
    if not isinstance(age, int):
        raise ValidationError('Age must be an integer')
    if age < 0 or age > 120:
        raise ValidationError('Age must be between 0 and 120')
    return True


def validate_username(username):
    if not isinstance(username, str):
        raise ValidationError('Username must be a string')
    if len(username) < 3 or len(username) > 20:
        raise ValidationError('Username must be between 3 and 20 characters')
    return True