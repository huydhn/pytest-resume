#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import find_packages, setup

version = os.getenv("PACKAGE_VERSION", default="0.0.1")

setup(
    name="pytest-resume",
    version=version,
    author="Huy Do",
    author_email="huydhn@gmail.com",
    license="MIT",
    url="https://github.com/huydhn/pytest-resume",
    description="A Pytest plugin to resuming from the last run test",
    long_description=open("README.md").read(),
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=["pytest>=7.0"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={
        "pytest11": [
            "resume = pytest_resume.plugin",
        ],
    },
)
