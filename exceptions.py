class CustomError(Exception):
    """Base class for exceptions in this module."""
    pass

class FileNotFound(CustomError):
    """Exception raised for errors in the file not found operations."""
    def __init__(self, filename):
        self.filename = filename
        self.message = f'File not found: {self.filename}'
        super().__init__(self.message)

class ValidationError(CustomError):
    """Exception raised for validation errors."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ConnectionError(CustomError):
    """Exception raised for connection related issues."""
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.message = f'Connection failed to {self.host}:{self.port}'
        super().__init__(self.message)
