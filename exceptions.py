class CustomError(Exception):
    """Base class for exceptions in this module."""
    pass

class ValidationError(CustomError):
    """Exception raised for validation errors."""
    def __init__(self, message, field):
        self.message = message
        self.field = field
        super().__init__(self.message)

    def __str__(self):
        return f'ValidationError: {self.message} for field: {self.field}'

class ConfigurationError(CustomError):
    """Exception raised for configuration errors."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'ConfigurationError: {self.message}'

class ProcessingError(CustomError):
    """Exception raised for processing errors."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'ProcessingError: {self.message}'