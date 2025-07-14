import os

def get_files_info(working_directory, directory=None):
    if directory is None:
        directory = "."
    full_target_path = os.path.abspath(os.path.join(working_directory, directory))
    
    abs_working_dir = os.path.abspath(working_directory)
    
    if not full_target_path.startswith(abs_working_dir):
        return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')

    if not os.path.isdir(full_target_path):
        return (f'Error: "{directory}" is not a directory')
    
    try:
        contents = os.listdir(full_target_path)
        output_lines = []
        for content in contents:
            content_full_path = os.path.join(full_target_path, content)
            content_size = os.path.getsize(content_full_path)
            content_is_dir = os.path.isdir(content_full_path)
            output_lines.append(f'- {content}: file_size={content_size} bytes, is_dir={content_is_dir}')
        return '\n'.join(output_lines)
    except Exception as e:
        return (f"Error: {e}")

#- README.md: file_size=1032 bytes, is_dir=False
#- src: file_size=128 bytes, is_dir=True
#- package.json: file_size=1234 bytes, is_dir=False


    #os.path.abspath(): Get an absolute path from a relative path
    #os.path.join(): Join two paths together safely (handles slashes)
    #.startswith(): Check if a string starts with a substring
    #os.path.isdir(): Check if a path is a directory
    #os.listdir(): List the contents of a directory
    #os.path.getsize(): Get the size of a file
    #os.path.isfile(): Check if a path is a file
    #.join(): Join a list of strings together with a separator
