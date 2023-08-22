#!\use\bin\python3
import os
from PyInstaller import __main__

__main__.run([
    'your_script.py',
    '--onefile',
    '--windowed'
])

#outo system py to exe
def outo():
    os.system('python -m PyInstaller your_file.py --onefile')