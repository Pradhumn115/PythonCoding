from setuptools import setup

APP = ['Guess the number game.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,

}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)