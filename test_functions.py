from functions.get_file_content import *
from functions.write_file import *
from functions.run_python_file import *
from functions.get_files_info import *

file_path = "calculator"
print(get_file_content({'file_path': 'main.py'}))
print(write_file({'file_path': 'main.txt', 'content': 'hello'}))
print(run_python_file({'file_path': 'main.py'}))
print(get_files_info({'directory': 'pkg'}))