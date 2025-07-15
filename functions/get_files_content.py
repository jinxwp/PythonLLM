import os
from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    if file_path is None:
       file_path = "."
    full_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    
    abs_working_dir = os.path.abspath(working_directory)
    
    if not full_file_path.startswith(abs_working_dir):
        return (f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')

    if not os.path.isfile(full_file_path):
        return (f'Error: File not found or is not a regular file: "{file_path}"')

    try:
        with open(full_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if len(file_content_string) >= MAX_CHARS:
                return (f'{file_content_string} [...File "{file_path}" truncated at 10000 characters]')
            return file_content_string
    except Exception as e:
        return (f"Error: {e}")













