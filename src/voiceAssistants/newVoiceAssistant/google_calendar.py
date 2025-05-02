import datetime
import os.path
from dateutil.parser import parse as date_parser
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dotenv import load_dotenv
from os import getenv
from pyWrkspPackage import ai_response

load_dotenv()
AI_KEY = getenv("AI_TOKEN")
AI_MODEL = getenv("AI_MODEL")
AI_URL = getenv("AI_URL")

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar"]


def get_credentials() -> Credentials:
    """
    Obtains Google API credentials for the user.

    This function handles the authentication process for accessing Google APIs.
    It checks for existing credentials stored in a file, refreshes them if they
    are expired, or initiates a new authorization flow if no valid credentials
    are found. The credentials are saved locally for future use.

    Returns:
        Credentials: An authorized Google API credentials object.

    Raises:
        FileNotFoundError: If the required client secrets file
                           (".secret-credentials.json") is not found.

    Notes:
        - The file ".secret-token.json" is used to store the user's access and
          refresh tokens.
        - The file ".secret-credentials.json" must contain the client secrets
          for the Google API project.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(".secret-token.json"):
        creds = Credentials.from_authorized_user_file(".secret-token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                ".secret-credentials.json", SCOPES
            )
        creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(".secret-token.json", "w") as token:
            token.write(creds.to_json())
    return creds


def get_events(amount: int) -> tuple[list, str]:
    """
    Fetches a specified number of upcoming events from the user's primary Google Calendar.
    Args:
        amount (int): The maximum number of events to retrieve.
    Returns:
        tuple[list, str]: A tuple containing:
            - A list of dictionaries, where each dictionary represents an event with the following keys:
                - 'title' (str): The title of the event.
                - 'location' (str or None): The location of the event, if available.
                - 'start' (datetime): The start time of the event.
                - 'end' (datetime): The end time of the event.
            - A formatted string summarizing the events, including their start and end times, titles, and locations.
    Raises:
        HttpError: If an error occurs while accessing the Google Calendar API.
    """
    creds = get_credentials()
    try:
        service = build("calendar", "v3", credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.now(
            datetime.timezone.utc
        ).isoformat()  # 'Z' indicates UTC time
        events_result = (
            service.events()
            .list(
                calendarId="primary",
                timeMin=now,
                maxResults=amount,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )
        events = events_result.get("items", [])

        if not events:
            print("No upcoming events found.")
            return [], "No upcoming events found."

        # Prints the start and name of the next 10 events
        output = []
        out_str = ""
        for index, event in enumerate(events):
            start = date_parser(
                event["start"].get("dateTime", event["start"].get("date"))
            )
            end = date_parser(event["end"].get("dateTime", event["start"].get("date")))
            location = (
                event["location"].replace("\n", " ")
                if "location" in event.keys()
                else None
            )
            title = event["summary"]
            output.append(
                {"title": title, "location": location, "start": start, "end": end}
            )
            out_str += f"{index + 1}.\t{start.strftime('%d/%m/%Y, %H:%M')} - {end.strftime('%d/%m/%Y, %H:%M')} -- {title} at {location}"

        return output, out_str

    except HttpError as error:
        print(f"An error occurred: {error}")
        return False, "An error occurred while fetching events."


def make_event(start: str, end: str, title: str) -> None:
    """
    Creates a new event in the user's primary Google Calendar.

    Args:
        start (str): The start date and time of the event in ISO 8601 format
                     (e.g., '2023-03-15T10:00:00').
        end (str): The end date and time of the event in ISO 8601 format
                   (e.g., '2023-03-15T11:00:00').
        title (str): The title or summary of the event.

    Returns:
        None: The function does not return a value but inserts the event into
              the user's Google Calendar.

    Raises:
        google.auth.exceptions.GoogleAuthError: If there is an issue with
                                                authentication.
        googleapiclient.errors.HttpError: If there is an error with the
                                          Google Calendar API request.

    Note:
        Ensure that the `get_credentials` function is implemented to provide
        valid Google API credentials, and the `googleapiclient.discovery.build`
        function is available for creating the Calendar API service.
    """
    creds = get_credentials()
    service = build("calendar", "v3", credentials=creds)
    service.events().insert(
        calendarId="primary",
        body={
            "summary": title,
            "start": {"dateTime": start, "timeZone": "America/Toronto"},
            "end": {"dateTime": end, "timeZone": "America/Toronto"},
        },
    ).execute()


def do_make_event(prompt: str) -> bool:
    """
    Creates a calendar event based on the user's prompt.

    This function interacts with an AI model to extract the event title, start time,
    and end time from the user's input. It also retrieves the user's next five events
    to provide context for relative time parsing. The event is then created in the
    user's calendar.

    Args:
        prompt (str): The user's input describing the event to be created.

    Returns:
        bool: True if the event was successfully created, False otherwise.

    Raises:
        Exception: If an error occurs during the event creation process, it is caught
        and logged, and the function returns False.
    """
    try:
        get_credentials()
        title_prompt = "What is the title of the event? Include only the title, based off of the user's prompt."
        start_time_prompt = "What is the start time of the event? The user will provide their next ten events in order to help you with relative information. Write it in HH:MM format. Include only the start time, based off of the user's prompt."
        end_time_prompt = "What is the end time of the event? The user will provide their next ten events in order to help you with relative information. Write it in HH:MM format. Include only the end time, based off of the user's prompt."

        events = get_events(10)[0]

        title = ai_response(
            [
                {"role": "system", "content": title_prompt},
                {"role": "user", "content": prompt},
            ],
            AI_MODEL,
            AI_URL,
            AI_KEY,
        )[0]
        start_time_str = ai_response(
            [
                {"role": "system", "content": start_time_prompt},
                {"role": "user", "content": events},
                {"role": "user", "content": prompt},
            ],
            AI_MODEL,
            AI_URL,
            AI_KEY,
        )[0]
        end_time_str = ai_response(
            [
                {"role": "system", "content": end_time_prompt},
                {"role": "user", "content": events},
                {"role": "user", "content": prompt},
            ],
            AI_MODEL,
            AI_URL,
            AI_KEY,
        )[0]

        start_time = date_parser(start_time_str)
        end_time = date_parser(end_time_str)

        make_event(start_time.isoformat(), end_time.isoformat(), title)
        return True
    except Exception as e:
        print(f"Error creating event: {e}")
        return False


if __name__ == "__main__":
    do_make_event(
        "Schedule a meeting with Jonah and the team on Friday at 3 PM for 1 hour"
    )  # Example usage
