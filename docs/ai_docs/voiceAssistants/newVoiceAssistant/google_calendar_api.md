# Documentation for src/voiceAssistants/newVoiceAssistant/google_calendar_api.py

# Google Calendar API Script Documentation

## Program Overview

This Python script interacts with the Google Calendar API to fetch upcoming events and create new events. The script uses OAuth 2.0 for authentication and requires user authorization to access the calendar data.

## Table of Contents

- [get_credentials](#get_credentials)
  - Description: Retrieves the user's credentials for accessing the Google Calendar API.
  - Parameters: None
  - Returns: `Credentials` object

- [get_events](#get_events)
  - Description: Fetches upcoming events from the user's primary calendar.
  - Parameters:
    - `amount` (int): The number of events to fetch.
  - Returns:
    - `output` (list): A list of dictionaries containing event details.
    - `out_str` (str): A formatted string summarizing the events.

- [make_event](#make_event)
  - Description: Creates a new event in the user's primary calendar.
  - Parameters:
    - `start` (str): The start time of the event in ISO 8601 format.
    - `end` (str): The end time of the event in ISO 8601 format.
    - `title` (str): The title of the event.
  - Returns: None

## Detailed Function Descriptions

### get_credentials

**Description**: This function retrieves the user's credentials for accessing the Google Calendar API. It checks for an existing token file and refreshes the token if necessary. If no valid credentials are found, it initiates the OAuth 2.0 flow to obtain new credentials.

**Parameters**: None

**Returns**:
- `Credentials` object: The user's credentials for accessing the Google Calendar API.

### get_events

**Description**: This function fetches upcoming events from the user's primary calendar. It retrieves the specified number of events starting from the current time.

**Parameters**:
- `amount` (int): The number of events to fetch.

**Returns**:
- `output` (list): A list of dictionaries containing event details, including title, location, start time, and end time.
- `out_str` (str): A formatted string summarizing the events.

### make_event

**Description**: This function creates a new event in the user's primary calendar. It takes the start time, end time, and title of the event as input and inserts the event into the calendar.

**Parameters**:
- `start` (str): The start time of the event in ISO 8601 format.
- `end` (str): The end time of the event in ISO 8601 format.
- `title` (str): The title of the event.

**Returns**: None

## Example Usage

### get_events

Usage example for `get_events`:

```python
events, summary = get_events(10)
print(summary)
```

### make_event

Usage example for `make_event`:

```python
make_event("2023-10-01T10:00:00-05:00", "2023-10-01T12:00:00-05:00", "Meeting with Team")
```

### Main Function

Usage example for the main function:

```python
if __name__ == "__main__":
    events, summary = get_events(200)
    print(summary)
```