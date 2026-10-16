from functions.get_file_content import *
from functions.write_file import *
from functions.run_python_file import *
from functions.get_files_info import *

working_directory = "calculator"
print(get_file_content(**{'working_directory': working_directory, 'file_path': 'main.py'}))
print(write_file(**{'working_directory': working_directory,'file_path': 'main.txt', 'content': 'hello'}))
print(run_python_file(**{'working_directory': working_directory,'file_path': 'main.py', 'args': []}))
print(get_files_info(**{'working_directory': working_directory,'directory': 'pkg'}))