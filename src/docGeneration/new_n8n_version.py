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
            print("❌ Webhook returned an error.")
            print(f"Status Code: {response.status_code}")
            print(f"Response body:\n{response.text}")
