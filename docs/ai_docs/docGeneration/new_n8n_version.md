# Documentation for src/docGeneration/new_n8n_version.py

# AI Summary
The code defines a function to send file contents to a webhook and retrieve a summary. It uses the `pyWrkspPackage` library to load file contents and the `requests` library to interact with the webhook. The function includes error handling for network issues and webhook errors, and prints appropriate messages based on the response.
The AI gave it a general rating of 8/10
The AI gave it a conventions rating of 7/10
# Functions

##get_summary
### Explanation
This function sends the contents of a file to a webhook URL and retrieves a summary of the file's contents. It uses the `pyWrkspPackage` library to load the file contents and the `requests` library to send the data to the webhook. The function handles potential network errors and prints appropriate messages based on the response from the webhook.
### Code
```python
def get_summary(path: str):
    payload = {
        "file_contents": pyWrkspPackage.load_from_file(path),
        "path": path,
    }

    try:
        response = requests.post(
            WEBHOOK_URL,
            headers=CUSTOM_HEADERS,
            json=payload,
            timeout=300,
        )
    except requests.exceptions.RequestException as exc:
        print(f"❌ Network error while calling the webhook: {exc}")
    else:
        if response.ok:
            print("✅ Webhook hit successfully!")
            print(f"Status Code: {response.status_code}")

            try:
                data = response.json()
                print("\n--- Response Body (JSON) ---")
                print(json.dumps(data, indent=2, ensure_ascii=False))

                return data["output"]["summary"]
            except ValueError:
                print("\n--- Response Body (raw) ---")
                print(response.text)
        else:
            print(f"❌ Webhook returned an error.")
            print(f"Status Code: {response.status_code}")
            print(f"Response body:\n{response.text}")
```
# Overall File Contents
```python
import json
import requests
import pyWrkspPackage

WEBHOOK_URL = "http://192.168.86.2:5678/webhook/6a1ebb89-46f0-4716-9f6f-a655eaf98359"

CUSTOM_HEADERS = {"User-Agent": "python-requests/2.32.0", "Accept": "application/json"}


def get_summary(path: str):
    payload = {
        "file_contents": pyWrkspPackage.load_from_file(path),
        "path": path,
    }

    try:
        response = requests.post(
            WEBHOOK_URL,
            headers=CUSTOM_HEADERS,
            json=payload,
            timeout=300,
        )
    except requests.exceptions.RequestException as exc:
        print(f"❌ Network error while calling the webhook: {exc}")
    else:
        if response.ok:
            print("✅ Webhook hit successfully!")
            print(f"Status Code: {response.status_code}")

            try:
                data = response.json()
                print("\n--- Response Body (JSON) ---")
                print(json.dumps(data, indent=2, ensure_ascii=False))

                return data["output"]["summary"]
            except ValueError:
                print("\n--- Response Body (raw) ---")
                print(response.text)
        else:
            print(f"❌ Webhook returned an error.")
            print(f"Status Code: {response.status_code}")
            print(f"Response body:\n{response.text}")

```
