import os
from config import *

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": f"Retrieves the content (at most {MAX_CHARS} characters) of a specified file within the working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to read, relative to the working directory",
                },
            },
            "required": ["file_path"],
        },
    },
}

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
            working_dir_abs = os.path.abspath(working_directory)
            target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))
            # Will be True or False
            valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
            if not valid_target_dir:
                return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
            if not os.path.isfile(target_dir):
                return f'Error: File not found or is not a regular file: "{file_path}"'
            file = open(target_dir)
            content: str = file.read(MAX_CHARS)
            if file.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return content
    except Exception as e:
        return f"Error: {e}"