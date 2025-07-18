import os
import subprocess
import sys

def run_python_file(working_directory, file_path, args=None):
    
    full_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    abs_working_dir = os.path.abspath(working_directory)
    
    if not full_file_path.startswith(abs_working_dir):
        return (f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')

    if not os.path.isfile(full_file_path):
        return (f'Error: File "{file_path}" not found.')
    
    if not full_file_path.endswith(".py"):
        return (f'Error: "{file_path}" is not a Python file.')
    
    try:
        result = subprocess.run([sys.executable, file_path, *args], cwd=working_directory, timeout=30, capture_output=True, text=True)
        output = []
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")
        if result.returncode != 0:
            output.append(f'Process exited with code {result.returncode}')
        if not output:
            return "No output produced."
        return "\n".join(output)

    except Exception as e:
        return (f"Error: executing Python file: {e}")
    
    
