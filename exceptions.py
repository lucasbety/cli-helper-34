class InvalidInputError(Exception):
    """Exception raised for invalid inputs in the application."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def validate_input(user_input):
    """Validates the user input for the application."""
    if not isinstance(user_input, str):
        raise InvalidInputError("Input must be a string.")
    if not user_input.strip():
        raise InvalidInputError("Input cannot be empty.")
    # Add additional validations as required


def main_processing_loop():
    """Main loop for processing user input with validation."""
    while True:
        user_input = input('Enter data: ')
        try:
            validate_input(user_input)
            # Process the validated input
            print(f'Processing input: {user_input}')
        except InvalidInputError as e:
            print(f'Error: {e.message}')

if __name__ == '__main__':
    main_processing_loop()