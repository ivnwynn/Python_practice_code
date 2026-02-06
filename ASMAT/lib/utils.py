import os

def get_os():
    if os.name == 'nt':
        return "Windows"
    elif os.name == 'posix':
        return "Linux or MacOS"
    else:
        return "Unknown"