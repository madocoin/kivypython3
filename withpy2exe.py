#!\use bin\python 3.11
import py2exe
from distitls import setup

freeze(
    console=[],
    windows=[],
    data_files=None,
    zipfile='library.zip',
    options={},
    version_info={}
)