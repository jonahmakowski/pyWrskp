# Documentation for src/claudeAPI/main.py

**Script Overview**
==================

The provided Python script is designed to automate interactions with Claude's webUI using Selenium WebDriver. The script allows users to log in using their Google account and send messages to Claude.

**Table of Contents**
-------------------

### Function Descriptions

#### `login_to_claude(webui_url, google_email, google_password)`

*   **Description**: This function logs into Claude's webUI using a Google account.
*   **Parameters**:
    *   `webui_url` (str): The URL of Claude's webUI.
    *   `google_email` (str): The user's Google email address.
    *   `google_password` (str): The user's Google password.
*   **Returns**: The WebDriver object if the login is successful, otherwise None.

#### `send_message_to_claude(driver, message)`

*   **Description**: This function sends a message to Claude using the provided WebDriver and message text.
*   **Parameters**:
    *   `driver` (WebDriver): The WebDriver object used for navigation.
    *   `message` (str): The message to be sent to Claude.
*   **Returns**: The response from Claude, if any.

### Example Usage

#### Logging in using Google

```python
claude_webui_url = "https://claude.ai"
google_email = "jonahmakowski@gmail.com"
google_password = "WhiteSwine545"

# Login using Google
driver = login_to_claude(claude_webui_url, google_email, google_password)
```

#### Sending a message

```python
message = "Hello, how are you?"

if driver:
    # Send the message
    response = send_message_to_claude(driver, message)

    # Print the response
    print(response)
else:
    print("Login failed")
```

**Code Snippets**
-----------------

Here is a code snippet demonstrating how to use these functions:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

# ...

def login_to_claude(webui_url, google_email, google_password):
    # Set up the WebDriver
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)

    try:
        # Navigate to Claude's webUI
        driver.get(webui_url)

        # Wait for and click the "Continue with Google" button
        google_login_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Continue with Google')]"))
        )
        sleep(4)
        google_login_button.click()

        # Switch to the Google sign-in window if it opens in a new tab
        main_window_handle = driver.current_window_handle
        windows = driver.window_handles
        if len(windows) > 1:
            google_window_handle = windows[1]
            driver.switch_to.window(google_window_handle)

        google_email_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="identifierId"]'))
        )
        google_email_input.send_keys(google_email)

        continue_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        continue_button.click()

        # ...

    except TimeoutException as e:
        print(f"Timed out waiting for element: {e}")
        return None

    return driver
```

```python
def send_message_to_claude(driver, message):
    try:
        # Wait for the message input box to load
        input_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input.message-input"))
        )

        # Send the message
        input_box.send_keys(message)

        # Click the send button
        send_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.send-button"))
        )
        send_button.click()

        # Wait for response to appear
        response_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.response"))
        )

        # Extract the response text
        response = response_element.text
        print("Claude's response:", response)

        return response

    except TimeoutException as e:
        print(f"Timed out waiting for element: {e}")
        return None
```