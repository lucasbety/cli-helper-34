import re

class InputValidationError(Exception):
    pass

class Processor:
    def __init__(self):
        pass
    
    def process_input(self, user_input):
        self.validate_input(user_input)
        # Process the input if validation is successful
        print(f"Processing input: {user_input}")

    def validate_input(self, user_input):
        if not user_input:
            raise InputValidationError("Input cannot be empty.")
        if not re.match(r'^[A-Za-z0-9_ ]+$', user_input):
            raise InputValidationError("Input contains invalid characters.")
        # You can add more validation rules as needed

    def main_loop(self):
        while True:
            user_input = input("Enter your input (or 'q' to quit): ")
            if user_input.lower() == 'q':
                print("Exiting program.")
                break
            try:
                self.process_input(user_input)
            except InputValidationError as e:
                print(f"Error: {e}")

if __name__ == '__main__':
    processor = Processor()
    processor.main_loop()