import threading
from importlib import import_module

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

def run_imports_in_thread(packages: list, aliases: list|None = None) -> None:
    """
    Imports Python modules or submodules in separate threads and updates the global namespace 
    with the imported modules using specified aliases.
    Args:
        packages (list): A list of packages to import. Each element can be:
            - A string representing the package name (e.g., "os").
            - A tuple where the first element is the package name and the second element is 
              the submodule name (e.g., ("os", "path")).
        aliases (list | None, optional): A list of aliases corresponding to the `packages` list. 
            Each alias can be:
            - A string representing the alias for the package (e.g., "os_alias").
            - A tuple where the second element is the alias for the submodule 
              (e.g., ("os", "path_alias")).
            Defaults to None, in which case the package names are used as aliases.
    Behavior:
        - Each package or submodule is imported in a separate thread.
        - The imported modules or submodules are added to the global namespace with the 
          specified aliases.
        - Prints a message for each imported module or submodule in the format:
          "Imported <alias> as <package_name>".
    Raises:
        IndexError: If the length of `aliases` does not match the length of `packages`.
    Example:
        packages = ["os", ("os", "path")]
        aliases = ["os_alias", ("os", "path_alias")]
        run_imports_in_thread(packages, aliases)
        # Imports the `os` module as `os_alias` and the `os.path` submodule as `path_alias`.
    """
    def import_packages(alias: str, package: str|tuple):
        """
        Dynamically imports a module or submodule and associates it with an alias.

        Args:
            alias (str): The alias to associate with the imported module or submodule.
            package (str | tuple): The name of the module to import as a string, or a tuple where the first element is the 
                                    module name and the second element is the submodule name.

        Returns:
            dict: A dictionary containing the alias and the imported module or submodule. The dictionary has the following structure:
                    {
                        "alias": <alias>,
                        "package": <imported module or submodule>
                    }

        Raises:
            ImportError: If the specified module or submodule cannot be imported.
            AttributeError: If the specified submodule does not exist in the module.
        """
        if isinstance(package, str):
            return {"alias": alias, "package": import_module(package)}
        elif isinstance(package, tuple):
            module = import_module(package[0])
            submodule = getattr(module, package[1])
            return {"alias": alias, "package": submodule}
    
    threads = []
    results = []
    aliases = aliases if aliases else packages
    for index, package in enumerate(packages):
        if isinstance(aliases[index], tuple):
            alias = aliases[index][1]
        else:
            alias = aliases[index]
        result, thread = run_in_thread_with_return(import_packages, alias, package)
        threads.append(thread)
        results.append(result)
    
    for thread in threads:
        thread.join()
    
    for result in results:
        print(f"Imported {result['result']['alias']} as {result['result']['package'].__name__}")
    globals().update({result["result"]["alias"]: result["result"]["package"] for result in results})
