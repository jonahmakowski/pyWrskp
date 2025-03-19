# Documentation for src/helpfulPackage/setup.py

# pyWrkspPackage Setup Script

This script is used to set up the `pyWrkspPackage` Python package. It configures package metadata, dependencies, and other settings required for distribution and installation.

## Table of Contents

* [Setup Function](#setup-function)
    * Description: Configures the package metadata and dependencies.
    * Parameters: Lists the parameters used to configure the package.
    * Returns: None.

## Detailed Function Descriptions

### Setup Function

Description: The `setup` function from the `setuptools` module is used to configure the package metadata and dependencies. This function sets up the package name, version, description, and other details required for distribution.

Parameters:
    * `name` (str): The name of the package.
    * `version` (str): The version of the package.
    * `description` (str): A brief description of the package.
    * `package_dir` (dict): A dictionary mapping package names to directories.
    * `packages` (list): A list of all packages to be included in the distribution.
    * `long_description` (str): A longer description of the package, typically read from a README file.
    * `long_description_content_type` (str): The content type of the long description (e.g., "text/markdown").
    * `url` (str): The URL of the package's homepage.
    * `author` (str): The name of the package author.
    * `author_email` (str): The email address of the package author.
    * `license` (str): The license under which the package is distributed.
    * `classifiers` (list): A list of classifiers that describe the package.
    * `install_requires` (list): A list of dependencies required for the package to function.
    * `extras_require` (dict): A dictionary of additional dependencies required for different environments (e.g., development).
    * `python_requires` (str): The Python version required to use the package.

Returns: None.

## Example Usage

Usage example for the setup script:

```python
from setuptools import find_packages, setup

with open("app/README.md", "r") as f:
    long_description = f.read()

setup(
    name="pyWrkspPackage",
    version="0.4.3",
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

This script reads the long description from a README file, configures the package metadata, and sets up the dependencies required for the package. The `setup` function is called with various parameters to configure the package, including its name, version, description, and dependencies. The `install_requires` parameter specifies the dependencies required for the package to function, while the `extras_require` parameter specifies additional dependencies required for different environments. The `python_requires` parameter specifies the Python version required to use the package.