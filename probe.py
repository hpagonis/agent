import os
print("CWD:", os.getcwd())
print("exists calculator.py:", os.path.exists("pkg/calculator.py"))
with open("pkg/calculator.py") as f:
    content = f.read()
print("has '+': 3 ->", "'+': 3" in content)
print("has '+': 1 ->", "'+': 1" in content)
