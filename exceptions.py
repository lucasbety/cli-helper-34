class CustomError(Exception):
    """Base class for other exceptions"""
    pass

class NotFoundError(CustomError):
    """Raised when a requested resource is not found"""
    def __init__(self, resource):
        self.resource = resource
        self.message = f'Resource {self.resource} not found'
        super().__init__(self.message)

class ValidationError(CustomError):
    """Raised when validation fails"""
    def __init__(self, field, message):
        self.field = field
        self.message = f'Validation error on {self.field}: {message}'
        super().__init__(self.message)

class PermissionError(CustomError):
    """Raised when permission is denied"""
    def __init__(self, action):
        self.action = action
        self.message = f'Permission denied for action: {self.action}'
        super().__init__(self.message)

# Example usage

try:
    raise NotFoundError('User')
except CustomError as e:
    print(e.message)

try:
    raise ValidationError('email', 'Invalid format')
except CustomError as e:
    print(e.message)

try:
    raise PermissionError('delete data')
except CustomError as e:
    print(e.message)