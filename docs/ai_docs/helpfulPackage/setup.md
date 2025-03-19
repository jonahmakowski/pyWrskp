# Documentation for src/helpfulPackage/setup.py

# pyWrkspPackage Documentation
=====================================

## Overview

The `pyWrkspPackage` is a Python package designed to provide a collection of helpful functions. This package is intended to simplify common tasks and enhance productivity for Python developers. Below is a detailed documentation of the setup script used to create and distribute this package.

## Table of Contents

* [Setup Script](#setup-script)
    * [Description](#description)
    * [Parameters](#parameters)
    * [Returns](#returns)

## Detailed Function Descriptions

### Setup Script

The setup script is used to configure the package distribution. It specifies metadata about the package, such as its name, version, description, and dependencies. This script is essential for packaging and distributing the `pyWrkspPackage`.

#### Description

The setup script configures the package distribution for `pyWrkspPackage`. It reads the long description from a README file, specifies the package name, version, description, and other metadata. It also defines the dependencies required for the package.

#### Parameters

The setup script uses several parameters to configure the package distribution. Here are the key parameters:

* `name`: The name of the package.
* `version`: The version of the package.
* `description`: A brief description of the package.
* `package_dir`: The directory where the package is located.
* `packages`: The list of packages to include in the distribution.
* `long_description`: The long description of the package, read from a README file.
* `long_description_content_type`: The content type of the long description.
* `url`: The URL of the package's repository.
* `author`: The author of the package.
* `author_email`: The email address of the author.
* `license`: The license under which the package is distributed.
* `classifiers`: A list of classifiers that describe the package.
* `install_requires`: A list of dependencies required for the package.
* `extras_require`: Additional dependencies required for development.
* `python_requires`: The Python version required for the package.

#### Returns

The setup script does not return any values. Its primary purpose is to configure the package distribution.

## Example Usage

Here is an example of how to use the setup script to configure and distribute the `pyWrkspPackage`:

```python
from setuptools import find_packages, setup

with open("app/README.md", "r") as f:
    long_description = f.read()

setup(
    name="pyWrkspPackage",
    version="0.4.6",
    description="A group of helpful functions for Python",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jonahmakowski/pyWrskp",
    author="Jonah Makowski",
    author_email="jonah@makowski.ca",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=['python-dotenv', 'openai'],
    extras_require={
        "dev": ["twine>=4.0.2"],
    },
    python_requires=">=3.10",
)
```

This setup script reads the long description from the `README.md` file located in the `app` directory. It then configures the package distribution with the specified metadata and dependencies. The `install_requires` parameter specifies the dependencies required for the package, while the `extras_require` parameter specifies additional dependencies required for development. The `python_requires` parameter specifies the Python version required for the package.