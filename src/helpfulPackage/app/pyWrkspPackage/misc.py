import time
from subprocess import run
from openai import OpenAI

def int_input(prompt: str) -> int:
    """
    Prompt the user to enter an integer value.

    This function repeatedly prompts the user with the given prompt string until
    a valid integer is entered. If the user enters a non-integer value, an error
    message is displayed and the prompt is shown again.

    Args:
        prompt (str): The message to display when asking for input.

    Returns:
        int: The integer value entered by the user.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a number.")

def float_input(prompt: str) -> float:
    """
    Prompt the user to enter a floating-point number.

    This function repeatedly prompts the user with the given prompt until a valid
    floating-point number is entered. If the user enters an invalid value, an error
    message is displayed and the prompt is shown again.

    Args:
        prompt (str): The message to display when asking for input.

    Returns:
        float: The floating-point number entered by the user.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number.")

def timer(func):
    """
    A decorator that prints the execution time of the decorated function.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: The wrapped function that prints its execution time.
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

def timestamp_print(*args, sep=' ', end='\n') -> None:
    """
    Prints the given arguments with a timestamp.

    Args:
        *args: Variable length argument list to be printed.
        sep (str, optional): Separator between arguments. Defaults to a single space.
        end (str, optional): String appended after the last value. Defaults to a newline.

    Example:
        timestamp_print("Hello", "world")
        # Output: [2023-10-05 14:23:45] Hello world
    """
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] ",end='')
    for arg in args:
        print(arg, end=sep)
    print(end, end='')

def run_terminal_command(command: str) -> str|None:
    """
    Run a terminal command and capture its output.

    Parameters:
    command (str): The terminal command to run.

    Returns:
    str|None: The output of the command if it was successful, None otherwise.
    """
    result = run(str(command), shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        return result.stdout.strip()
    else:
        return None

def ai_response(messages: list, model: str, url: str, key: str, stream=False):
    """
    Get a response from the OpenAI API.

    Args:
        messages (list): A list of message dictionaries to send to the API.
        model (str): The model to use for the completion.
        url (str): The base URL for the OpenAI API.
        key (str): The API key for authentication.
        stream (bool, optional): Whether to stream the response. Defaults to False.

    Returns:
        tuple: The content of the response and the updated messages list.
    """
    client = OpenAI(api_key=key, base_url=url)
    completion = client.chat.completions.create(model=model, messages=messages, stream=stream)
    if not stream:
        messages.append({"role": "assistant", "content": completion.choices[0].message.content})
        return completion.choices[0].message.content, messages
    else:
        return completion
