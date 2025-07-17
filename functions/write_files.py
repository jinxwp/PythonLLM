import os

def write_file(working_directory, file_path, content):
    if file_path is None:
           file_path = "."
    
    full_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    abs_working_dir = os.path.abspath(working_directory)

    if not full_file_path.startswith(abs_working_dir):
        return (f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')

    try:

        directory = os.path.dirname(full_file_path)
        os.makedirs(directory, exist_ok=True)
        with open(full_file_path, "w") as f:
            f.write(content)
        return (f'Successfully wrote to "{file_path}" ({len(content)} characters written)')
    except Exception as e:
        return (f"Error: {e}")






