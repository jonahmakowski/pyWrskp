# Documentation for src/newVoiceAssistant/llama_ai.py

# Python Script Documentation

## Program Overview

The provided Python script is designed to interact with an AI model hosted at a specified URL using the OpenAI API. The script utilizes environment variables for configuration and includes a function to generate responses based on user prompts. This document will provide an overview of the script's functions and classes, along with explanations and examples.

## Table of Contents

- [llama_result](#llama_result)
  - Description: Generates a response from an AI model based on a user prompt.
  - Parameters: List any input parameters required by the function.
  - Returns: Describe any output or return values produced by the function.

## Detailed Function Descriptions

### llama_result

**Description:** This function generates a response from an AI model based on a user prompt. The function initializes an OpenAI client with a specified API key and base URL, constructs a message payload, and sends a request to the AI model to generate a response.

**Parameters:**
- `prompt` (str): The user's input prompt that the AI model will respond to.
- `model` (str, optional): The AI model to use for generating the response. Defaults to 'mistral-large-latest'.

**Returns:**
- `result` (str): The generated response from the AI model.

## Example Usage

Usage example for `llama_result`:

```python
import dotenv
import os
import openai
import helpers

dotenv.load_dotenv()
token = os.getenv('API_TOKEN')

def llama_result(prompt, model='mistral-large-latest'):
    client = openai.Client(api_key=token,
                           base_url='http://192.168.86.4:4001')

    messages = [
        {"role": "system", "content": "You are an assistant that is running on someone's computer. You have the ability to open an app if you say \"APP\" followed by the app's name. You have the ability to open a file if you say \"FILE\" followed by the filename. You have the ability to play music if you say \"PLAY\". You have the ability to pause music if you say \"PAUSE\". You have the ability to open a website if you say \"WEBSITE\" followed by the url (without the https:// part). You have the ability to google something if you say \"GOOGLE\" followed by what to google. Any command should be between $s. You HAVE TO say something other than just a command. You should not use a $ unless it is for a command. A command(s) should be at the end of your response. Don't run a command unless prompted by the user. Your name is " + helpers.get_details()[2] + ", the user is called " + helpers.get_details()[0]},
        {"role": "user", "content": prompt}
    ]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.7,
        max_tokens=1000
    )

    result = response.choices[0].message.content

    return result

# Example usage
prompt = "What is the weather like today?"
response = llama_result(prompt)
print(response)
```

This example demonstrates how to use the `llama_result` function to generate a response from the AI model based on a user prompt. The function initializes the OpenAI client with the API key and base URL, constructs the message payload, and sends a request to the AI model to generate a response. The generated response is then printed to the console.