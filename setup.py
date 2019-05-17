# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="python-status-resource",
    version="1.0.0",
    description="Python module for status management",
    author="Jhonny Bravo",
    author_email="sanfranceshika5@gmail.com",
    url="https://github.com/JhonnyBravo/python-status-resource.git",
    packages=find_packages(),
    install_requires=[],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ]
)
