# -*- coding: utf-8 -*-
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gotowebinar",
    version="0.0.1",
    author="Veit Rückert",
    author_email="veit@blueshoe.de",
    description="A wrapper around the GoToWebinar REST API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/schwobaseggl/python-gotowebinar",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests>=2',
        'dataclasses-json>=0.3.3',
    ]
)
