import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Sloths",
    version = "0.1.0",
    author = "Pierre Padrixe",
    author_email = "pierre.padrixe@gmail.com",
    description = ("Api REST for NoSQL DocumentStore auto-managed."),
    license = "GPLv3",
    url = "https://github.com/pierre--/sloths",
    packages=['sloths', 'sloths.connector'],
    scripts = [
        'bin/sloths'
    ],
    long_description=read('README.md')
)
