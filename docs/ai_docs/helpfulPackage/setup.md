# Documentation for src/helpfulPackage/setup.py

# pyWrkspPackage Setup Script

This script is used to set up and configure the `pyWrkspPackage` package. It leverages `setuptools` to define package metadata, dependencies, and other configurations.

## Table of Contents

*   [Setup Configuration](#setup-configuration)
    *   [Name](#name)
    *   [Version](#version)
    *   [Description](#description)
    *   [Package Directory](#package-directory)
    *   [Packages](#packages)
    *   [Long Description](#long-description)
    *   [URL](#url)
    *   [Author](#author)
    *   [Author Email](#author-email)
    *   [License](#license)
    *   [Classifiers](#classifiers)
    *   [Install Requires](#install-requires)
    *   [Extras Require](#extras-require)
    *   [Python Requires](#python-requires)

## Setup Configuration

### Name

```python
name="pyWrkspPackage"
```

The name of the package. This is the name that will be used to install the package.

### Version

```python
version="0.4.0"
```

The version of the package. This follows semantic versioning.

### Description

```python
description="A group of helpful functions for Python"
```

A brief description of the package.

### Package Directory

```python
package_dir={"": "app"}
```

Specifies the directory where the package is located. In this case, the package is located in the `app` directory.

### Packages

```python
packages=find_packages(where="app")
```

Finds all packages in the `app` directory. This dynamically discovers all sub-packages and modules within the `app` directory.

### Long Description

```python
with open("app/README.md", "r") as f:
    long_description = f.read()
```

Reads the long description of the package from the `README.md` file located in the `app` directory. This provides a more detailed description of the package.

### URL

```python
url="https://github.com/jonahmakowski/pyWrskp"
```

The URL of the package's repository or homepage.

### Author

```python
author="Jonah Makowski"
```

The name of the package's author.

### Author Email

```python
author_email="jonah@makowski.ca"
```

The email address of the package's author.

### License

```python
license="MIT"
```

The license under which the package is distributed.

### Classifiers

```python
classifiers=[
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.10",
    "Operating System :: OS Independent",
]
```

Classifiers help users find the package by categorizing it. These classifiers indicate that the package is licensed under the MIT License, is written in Python 3.10, and is OS independent.

### Install Requires

```python
install_requires=['python-dotenv', 'openai']
```

A list of dependencies that are required to install the package. In this case, the package requires `python-dotenv` and `openai`.

### Extras Require

```python
extras_require={
    "dev": ["twine>=4.0.2"],
}
```

Additional dependencies that are optional. In this case, the `dev` extra includes `twine>=4.0.2`, which is useful for developers.

### Python Requires

```python
python_requires=">=3.10"
```

Specifies the Python version required to run the package. In this case, Python 3.10 or higher is required.

## Example Usage

To use this setup script, you would typically run it from the command line in the root directory of your package:

```sh
python setup.py sdist bdist_wheel
```

This command will create source and wheel distributions of your package, which can then be uploaded to the Python Package Index (PyPI) or another package repository.

```sh
twine upload dist/*
```

This command will upload the distributions to PyPI, making them available for installation by other users.

By following these steps, you can easily set up and distribute your `pyWrkspPackage` package.