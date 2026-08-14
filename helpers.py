def read_file(file_path):
    """Read the contents of a file and return as string."""
    with open(file_path, 'r') as file:
        return file.read()


def write_file(file_path, content):
    """Write the given content to a file."""
    with open(file_path, 'w') as file:
        file.write(content)


def append_to_file(file_path, content):
    """Append the given content to a file."""
    with open(file_path, 'a') as file:
        file.write(content)


def read_json(file_path):
    """Read a JSON file and return the data as a Python dictionary."""
    import json
    with open(file_path, 'r') as file:
        return json.load(file)


def write_json(file_path, data):
    """Write a Python dictionary to a JSON file."""
    import json
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def list_files_in_directory(directory_path):
    """Return a list of files in the specified directory."""
    import os
    return [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
