class CustomError(Exception):
    """Base class for custom exceptions."""
    pass

class NotFoundError(CustomError):
    """Exception raised when a resource is not found."""
    def __init__(self, resource):
        self.resource = resource
        self.message = f'Resource {resource} was not found.'
        super().__init__(self.message)

class ValidationError(CustomError):
    """Exception raised for validation errors."""
    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(self.message)

class DatabaseError(CustomError):
    """Exception raised for database related errors."""
    def __init__(self, error_code, message):
        self.error_code = error_code
        self.message = message
        super().__init__(self.message)

class AuthenticationError(CustomError):
    """Exception raised for authentication failures."""
    pass

class PermissionDeniedError(CustomError):
    """Exception raised when access is denied."""
    pass