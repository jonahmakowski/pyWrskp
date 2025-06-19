# Documentation for src/voiceAssistants/newVoiceAssistant/actions.py

# Python Script Documentation

## Program Overview

This Python script provides a set of utility functions to interact with macOS applications and system settings. It includes functionalities to hide applications, find and open applications and files, control Spotify playback, open webpages, search queries on Google, terminate the program, quit applications, and set/get system volume.

## Table of Contents

* [hide_app](#hide_app)
* [find_path_app](#find_path_app)
* [open_directory_in_finder](#open_directory_in_finder)
* [open_app](#open_app)
* [find_path](#find_path)
* [open_file](#open_file)
* [pause](#pause)
* [play](#play)
* [open_webpage](#open_webpage)
* [search](#search)
* [terminate](#terminate)
* [quit_app](#quit_app)
* [set_volume](#set_volume)
* [get_current_volume](#get_current_volume)

## Detailed Function Descriptions

### hide_app

**Description:** Hide the specified application using AppleScript.

**Parameters:**
* `app_name` (str): The name of the application to hide.

**Returns:** None

### find_path_app

**Description:** Find the path of an application using the `mdfind` command.

**Parameters:**
* `app` (str): The name of the application to find.

**Returns:**
* `str|bool`: The path of the application if found, False otherwise.

### open_directory_in_finder

**Description:** Open a directory in Finder.

**Parameters:**
* `directory` (str): The path of the directory to open.

**Returns:**
* `bool`: True if the directory was successfully opened, False otherwise.

### open_app

**Description:** Open an application by its name.

**Parameters:**
* `app` (str): The name of the application to open.

**Returns:**
* `bool`: True if the application was successfully opened, False otherwise.

### find_path

**Description:** Find the path of a file using the `mdfind` command.

**Parameters:**
* `file` (str): The name of the file to find.

**Returns:**
* `str|bool`: The path of the file if found, False otherwise.

### open_file

**Description:** Open a file using the default application.

**Parameters:**
* `file` (str): The name of the file to open.

**Returns:**
* `bool`: True if the file was successfully opened, False otherwise.

### pause

**Description:** Pause the music on Spotify.

**Parameters:** None

**Returns:** None

### play

**Description:** Play music on Spotify.

**Parameters:**
* `open_spotify` (bool): If True, open the Spotify application before playing music. Defaults to True.

**Returns:** None

### open_webpage

**Description:** Open a webpage in the default web browser.

**Parameters:**
* `page` (str): The URL or page to open.
* `https` (bool): If True, prepend 'https://' to the page URL. Defaults to True.

**Returns:** None

### search

**Description:** Search for a query on Google.

**Parameters:**
* `query` (str): The search query.

**Returns:**
* `str`: The final URL used for the search.

### terminate

**Description:** Terminate the program.

**Parameters:** None

**Returns:** None

### quit_app

**Description:** Quit an application using AppleScript.

**Parameters:**
* `app` (str): The name of the application to quit.

**Returns:** None

### set_volume

**Description:** Set the system volume to a specified percentage.

**Parameters:**
* `percentage` (int): The desired volume level as a percentage (0-100).

**Returns:** None

### get_current_volume

**Description:** Get the current system volume level.

**Parameters:** None

**Returns:**
* `int`: The current volume level as a percentage (0-100).

## Example Usage

### hide_app

```python
hide_app('Safari')
```

### find_path_app

```python
app_path = find_path_app('Terminal')
if app_path:
    print(f'Terminal found at: {app_path}')
else:
    print('Terminal not found')
```

### open_directory_in_finder

```python
open_directory_in_finder('/Users/username/Documents')
```

### open_app

```python
open_app('Calculator')
```

### find_path

```python
file_path = find_path('example.txt')
if file_path:
    print(f'File found at: {file_path}')
else:
    print('File not found')
```

### open_file

```python
open_file('example.txt')
```

### pause

```python
pause()
```

### play

```python
play