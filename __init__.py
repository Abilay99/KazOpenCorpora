from sys import platform
OS = "unknown"
if platform == "linux" or platform == "linux2":
    OS = "Linux"
elif platform == "darwin":
    OS = "MacOS"
elif platform == "win32" or platform == "win64":
    OS = "Windows"