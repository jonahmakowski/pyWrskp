# Documentation for src/helpfulPackage/setup.py

# pyWrkspPackage Setup Script

This document provides a comprehensive overview of the setup script for the `pyWrkspPackage` Python package. The script is written using `setuptools`, which is a library in Python that facilitates packaging Python projects.

## Table of Contents

- [Overview](#overview)
- [Dependencies](#dependencies)
- [Setup Configuration](#setup-configuration)
  - [Package Metadata](#package-metadata)
  - [Package Description](#package-description)
  - [Package Dependencies](#package-dependencies)
  - [Extras Dependencies](#extras-dependencies)
  - [Python Version Requirement](#python-version-requirement)
- [Example Usage](#example-usage)

## Overview

The `pyWrkspPackage` is a collection of helpful functions designed to assist Python developers. This setup script is used to package the `pyWrkspPackage` for distribution, making it easy to install and use in other projects.

## Dependencies

The setup script relies on the following dependencies:

- `setuptools`: A library for packaging Python projects.
- `python-dotenv`: A library to load environment variables from a `.env` file.
- `openai`: A library to interact with the OpenAI API.

## Setup Configuration

The setup script is configured with various metadata and dependencies to ensure the package is correctly packaged and installed.

### Package Metadata

The package metadata includes:

- **Name**: `pyWrkspPackage`
- **Version**: `0.4.4`
- **Description**: `A group of helpful functions for Python`
- **URL**: `https://github.com/jonahmakowski/pyWrskp`
- **Author**: `Jonah Makowski`
- **Author Email**: `jonah@makowski.ca`
- **License**: `MIT`
- **Classifiers**: Specifies the license, programming language, and operating system compatibility.

### Package Description

The package description is read from the `README.md` file located in the `app` directory. This file provides a detailed overview of the package, its features, and how to use it.

### Package Dependencies

The package depends on the following libraries:

- `python-dotenv`: For loading environment variables.
- `openai`: For interacting with the OpenAI API.

### Extras Dependencies

Additional dependencies for development purposes are specified under the `extras_require` key:

- `twine>=4.0.2`: A utility for publishing Python packages to PyPI.

### Python Version Requirement

The package requires Python version `>=3.10`.

## Example Usage

To use the setup script, follow these steps:

1. Ensure you have `setuptools` installed:

```bash
pip install setuptools
```

2. Navigate to the directory containing the setup script.

3. Run the setup script to install the package:

```bash
python setup.py install
```

4. To upload the package to PyPI, use `twine`:

```bash
pip install twine
python setup.py sdist bdist_wheel
twine upload dist/*
```

This setup script ensures that the `pyWrkspPackage` is correctly packaged and can be easily installed and distributed.