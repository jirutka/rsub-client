#!/usr/bin/env python

# Fix encoding problem.
import sys
reload(sys)
sys.setdefaultencoding('utf8')

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()

setup(
    name="rsub",
    version="1.0.0",
    url="https://github.com/jirutka/rsub-client",
    description="Open and edit files from a remote machine in your local Sublime Text or TextMate 2.",
    long_description=read_md("README.md"),
    author="Jakub Jirutka",
    author_email="jakub@jirutka.cz",
    license="MIT",
    scripts=["bin/rsub"],
    install_requires=['docopt>=0.5.0'],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ]
)
