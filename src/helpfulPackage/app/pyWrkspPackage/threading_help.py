import threading


def run_in_thread(func, *args, **kwargs):
    """
    Run a function in a separate thread.

    Args:
        func (callable): The function to run.
        *args: Positional arguments to pass to the function.
        **kwargs: Keyword arguments to pass to the function.

    Returns:
        threading.Thread: The thread object running the function.
    """
    thread = threading.Thread(target=func, args=args, kwargs=kwargs)
    thread.start()
    return thread


def run_in_thread_with_return(func, *args, **kwargs):
    """
    Run a function in a separate thread and return the result.

    Args:
        func (callable): The function to run.
        *args: Positional arguments to pass to the function.
        **kwargs: Keyword arguments to pass to the function.

    Returns:
        threading.Thread, threading.Event: The thread object running the function and an event to wait for the result.
    """
    result_container = {"result": None}
    event = threading.Event()

    def wrapper():
        result_container["result"] = func(*args, **kwargs)
        event.set()

    thread = threading.Thread(target=wrapper)
    thread.start()
    return result_container, thread
