from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep


def login_to_claude(webui_url, google_email, google_password):
    # Set up the WebDriver
    options = webdriver.FirefoxOptions()
    # Optional: Run headless
    # options.add_argument('headless')
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
            EC.element_to_be_clickable((By.XPATH, '//*[@id="identifierNext"]'))
        )
        continue_button.click()

        google_password_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@name="password"]'))
        )
        google_password_input.send_keys(google_password)

        continue_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="identifierNext"]'))
        )
        continue_button.click()

        continue_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='passwordNext']/div/button"))
        )
        continue_button.click()

        return driver

    except TimeoutException as e:
        print(f"Timed out waiting for element: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        # You can close the driver here if you don't want to use it further
        # driver.quit()
        pass


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


# Example usage
claude_webui_url = "https://claude.ai"
google_email = "jonahmakowski@gmail.com"
google_password = "WhiteSwine545"

# Login using Google
driver = login_to_claude(claude_webui_url, google_email, google_password)

# If login is successful, send a message
if driver:
    message = "Hello, how are you?"
    response = send_message_to_claude(driver, message)
    print(response)
    driver.quit()  # Close the browser after you're done