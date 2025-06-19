# Documentation for src/voiceAssistants/voiceAssistant/commands/webBrowser.py

# Python Script Documentation

## Program Overview

The provided Python script is designed to open webpages and perform Google searches using the default web browser. It includes two main functions: `open_webpage` and `google_search`.

## Table of Contents

- [open_webpage](#open_webpage)
  - Description: Opens a webpage in the default web browser.
  - Parameters: `page` (str), `https` (bool)
  - Returns: None

- [google_search](#google_search)
  - Description: Performs a Google search using the provided query and opens the results in the default web browser.
  - Parameters: `query` (str)
  - Returns: The final URL used for the Google search (str)

## Detailed Function Descriptions

### open_webpage

Description: Opens a webpage in the default web browser. The function can handle both HTTP and HTTPS URLs.

Parameters:
- `page` (str): The URL of the webpage to open. This should be a string without the protocol (e.g., "www.example.com").
- `https` (bool): A boolean flag indicating whether to use HTTPS. If `True`, the function will prepend "https://" to the URL. If `False`, it will use the provided URL as-is.

Returns: None

### google_search

Description: Performs a Google search using the provided query and opens the results in the default web browser.

Parameters:
- `query` (str): The search query to use. This should be a string containing the search terms.

Returns: The final URL used for the Google search (str).

## Example Usage

### Example Usage for `open_webpage`

Usage example for `open_webpage`:

```python
# Open a webpage using HTTPS
open_webpage("www.example.com", https=True)

# Open a webpage without HTTPS
open_webpage("http://www.example.com", https=False)
```

### Example Usage for `google_search`

Usage example for `google_search`:

```python
# Perform a Google search for "Python programming"
final_url = google_search("Python programming")
print("Search URL:", final_url)
```

This script leverages the `webbrowser` module to open webpages and the `urllib.parse` module to handle URL encoding for the Google search query. The `open_webpage` function allows for flexibility in opening both HTTP and HTTPS URLs, while the `google_search` function simplifies performing Google searches directly from the script.