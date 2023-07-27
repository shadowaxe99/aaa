```python
import subprocess

def execute_code(code, language):
    if language == 'python':
        return execute_python_code(code)
    # Add more elif conditions here for other languages
    else:
        return "Unsupported language"

def execute_python_code(code):
    try:
        output = subprocess.check_output(["python", "-c", code], universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return str(e)
```