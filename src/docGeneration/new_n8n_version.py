import requests
import pyWrkspPackage

# The target URL for the webhook
url = "http://192.168.86.2:5678/webhook-test/6a1ebb89-46f0-4716-9f6f-a655eaf98359"

# Define the custom headers as a Python dictionary.
# The key is the header name, and the value is the header's content.
custom_headers = {
    "host": "192.168.86.2:5678",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:140.0) Gecko/20100101 Firefox/140.0",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "accept-language": "en-CA,en-US;q=0.7,en;q=0.3",
    "accept-encoding": "gzip, deflate",
    "dnt": "1",
    "sec-gpc": "1",
    "connection": "keep-alive",
    "upgrade-insecure-requests": "1",
    "priority": "u=0, i",
}

payload = {
    "file_contents": pyWrkspPackage.load_from_file("./generate.py"),
    "path": "src/docGeneration/generate.py",
}

try:
    # Send a POST request to the URL with the specified headers.
    # A POST request is common for webhooks that receive data.
    response = requests.get(url, headers=custom_headers, json=payload, timeout=1000)

    # Check if the request was successful (status code 200-299)
    if response.ok:
        print("✅ Webhook hit successfully!")
        print(f"Status Code: {response.status_code}")

        print("\n--- Response Headers ---")
        if response.headers:
            # response.headers is a dictionary-like object. We can iterate through it.
            for key, value in response.headers.items():
                print(f"{key}: {value}")
        else:
            print("[No headers were returned in the response]")
        print(response.json().keys())

    else:
        print(f"❌ Failed to hit webhook.")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")

except requests.exceptions.RequestException as e:
    # Handle potential network errors (e.g., no internet connection)
    print(f"An error occurred: {e}")
