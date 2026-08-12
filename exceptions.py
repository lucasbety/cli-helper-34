class CustomError(Exception):
    """Base class for custom exceptions."""
    pass

class InvalidInputError(CustomError):
    """Raised when the input is invalid."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ResourceNotFoundError(CustomError):
    """Raised when a requested resource is not found."""
    def __init__(self, resource_name):
        self.message = f'Resource {resource_name} was not found.'
        super().__init__(self.message)

class OperationFailedError(CustomError):
    """Raised when an operation fails."""
    def __init__(self, operation_name):
        self.message = f'Operation {operation_name} failed.'
        super().__init__(self.message)