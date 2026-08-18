import json
import os

class FileProcessor:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        try:
            if not os.path.exists(self.file_path):
                raise FileNotFoundError(f'File {self.file_path} does not exist.')
            with open(self.file_path, 'r') as file:
                return file.read()
        except FileNotFoundError as e:
            return json.dumps({'error': str(e)})
        except IOError as e:
            return json.dumps({'error': 'An I/O error occurred: ' + str(e)})

    def write_file(self, content):
        try:
            with open(self.file_path, 'w') as file:
                file.write(content)
        except IOError as e:
            return json.dumps({'error': 'Failed to write file: ' + str(e)})

# Usage example
if __name__ == '__main__':
    processor = FileProcessor('example.txt')
    print(processor.read_file())
    print(processor.write_file('Hello, World!'))
    print(processor.read_file())