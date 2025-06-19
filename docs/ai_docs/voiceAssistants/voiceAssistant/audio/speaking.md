# Documentation for src/voiceAssistants/voiceAssistant/audio/speaking.py

# Python Script Documentation

## Program Overview

The provided Python script is designed to replace placeholders in text with actual usernames and then speak the modified text using the system's text-to-speech functionality. This document will provide an overview of the script's functions and classes, along with explanations and examples.

## Table of Contents

*   [replace_with_username](#replace_with_username)
    *   Description: Replaces placeholders in text with actual usernames.
    *   Parameters: text (str)
    *   Returns: new_write (str), new_speak (str)

*   [speak](#speak)
    *   Description: Speaks the modified text using the system's text-to-speech functionality.
    *   Parameters: text (str)
    *   Returns: None

## Detailed Function Descriptions

### replace_with_username

Description: This function replaces placeholders in the input text with actual usernames. It uses the `helpers.get_details()` function to fetch the usernames for speaking and writing.

Parameters:
    *   text (str): The input text containing placeholders.

Returns:
    *   new_write (str): The modified text with placeholders replaced for writing.
    *   new_speak (str): The modified text with placeholders replaced for speaking.

### speak

Description: This function speaks the modified text using the system's text-to-speech functionality. It calls the `replace_with_username` function to get the modified text and then uses the `subprocess_run` function to execute the `say` command.

Parameters:
    *   text (str): The input text containing placeholders.

Returns: None

## Example Usage

### Example Usage for replace_with_username

```python
text = "Hello {{USERNAME}}! How are you?"
write, speak = replace_with_username(text)
print("Write:", write)
print("Speak:", speak)
```

### Example Usage for speak

```python
text = "Hello {{USERNAME}}! How are you?"
speak(text)
```

This will replace the `{{USERNAME}}` placeholder with the actual username and then speak the modified text using the system's text-to-speech functionality.