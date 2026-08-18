class CustomError(Exception):
    """Base class for other exceptions."""
    pass


class ValidationError(CustomError):
    """Raised when validation of input fails."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ProcessingError(CustomError):
    """Raised when processing encounters an error."""
    def __init__(self, details):
        self.details = details
        super().__init__(f'Processing error: {self.details}')

class FileNotFoundError(CustomError):
    """Raised when the specified file is not found."""
    def __init__(self, filename):
        self.filename = filename
        super().__init__(f'File not found: {self.filename}')

class PermissionError(CustomError):
    """Raised when permission is denied for an operation."""
    def __init__(self, operation):
        self.operation = operation
        super().__init__(f'Permission denied for operation: {self.operation}')