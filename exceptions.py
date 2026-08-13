class CustomError(Exception):
    """Custom exception for handling specific errors in the application."""
    def __init__(self, message: str) -> None:
        """Initialize the CustomError with a message."""
        super().__init__(message)
        self.message = message


class ValidationError(CustomError):
    """Exception raised for validation errors."""
    def __init__(self, field: str, message: str) -> None:
        """Initialize the ValidationError with a field and message."""
        super().__init__(message)
        self.field = field


class DatabaseError(CustomError):
    """Exception raised for database related errors."""
    def __init__(self, db_message: str) -> None:
        """Initialize the DatabaseError with a database message."""
        super().__init__(db_message)
        self.db_message = db_message


class NotFoundError(CustomError):
    """Exception raised when a resource is not found."""
    def __init__(self, resource: str) -> None:
        """Initialize the NotFoundError with a resource name."""
        super().__init__(f'{resource} not found.')
        self.resource = resource
