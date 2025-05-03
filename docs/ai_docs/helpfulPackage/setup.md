# Documentation for src/helpfulPackage/setup.py

# Python Documentation for `setup.py`

## Program Overview

The provided `setup.py` script is used to configure and package the `pyWrkspPackage` Python package. This script utilizes the `setuptools` library to define the package's metadata, dependencies, and other configuration options. The package includes a collection of helpful functions for Python, and this documentation will provide an overview of the script's configuration and usage.

## Table of Contents

- [Setup Configuration](#setup-configuration)
  - [Description](#description)
  - [Parameters](#parameters)
  - [Returns](#returns)

## Detailed Function Descriptions

### Setup Configuration

**Description**: The `setup` function from `setuptools` is used to configure the `pyWrkspPackage` package. This includes defining the package name, version, description, author information, license, classifiers, dependencies, and other metadata.

**Parameters**:
- `name` (str): The name of the package.
- `version` (str): The version of the package.
- `description` (str): A short description of the package.
- `package_dir` (dict): A dictionary mapping package names to directories.
- `packages` (list): A list of all Python import packages that should be included in the distribution package.
- `long_description` (str): A long description of the package, read from `README.md`.
- `long_description_content_type` (str): The content type of the long description.
- `url` (str): The URL of the package's homepage.
- `author` (str): The name of the package's author.
- `author_email` (str): The email address of the package's author.
- `license` (str): The license under which the package is distributed.
- `classifiers` (list): A list of classifiers that provide additional metadata about the package.
- `install_requires` (list): A list of dependencies required to install the package.
- `extras_require` (dict): A dictionary of optional dependencies for the package.
- `python_requires` (str): The Python version required to install the package.

**Returns**: This function does not return any value. It configures the package for distribution.

## Example Usage

Below is an example of how to use the `setup.py` script to configure and package the `pyWrkspPackage`.

```python
from setuptools import find_packages, setup

# Read the long description from the README.md file
with open("app/README.md", "r") as f:
    long_description = f.read()

# Configure the package using the setup function
setup(
    name="pyWrkspPackage",
    version="0.6.0",
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
    install_requires=["python-dotenv", "openai"],
    extras_require={
        "dev": ["twine>=4.0.2"],
    },
    python_requires=">=3.10",
)
```

This script configures the `pyWrkspPackage` package with the specified metadata and dependencies. It reads the long description from the `README.md` file and includes it in the package configuration. The `install_requires` parameter specifies the dependencies required to install the package, while the `extras_require` parameter specifies optional dependencies for development purposes.