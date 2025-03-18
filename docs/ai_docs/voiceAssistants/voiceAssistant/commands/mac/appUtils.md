# Documentation for src/voiceAssistants/voiceAssistant/commands/mac/appUtils.py

# Python Script Documentation

## Program Overview

This Python script provides a function to hide an application on macOS using AppleScript. The script utilizes the `subprocess` module to run an AppleScript command that activates the specified application and sends a keystroke to hide it.

## Table of Contents

*   [hide_app](#hide_app)
    *   Description: Hides the specified application on macOS.
    *   Parameters: `app_name` (str, name of the application to hide)
    *   Returns: None

## Detailed Function Descriptions

### hide_app

Description: This function takes the name of an application as input and hides it on macOS. It uses AppleScript to activate the application and send a keystroke to hide it.

Parameters:
    *   `app_name` (str): The name of the application to hide.

Returns: None

## Example Usage

Usage example for `hide_app`:

```python
# Hide the "Safari" application
hide_app("Safari")
```