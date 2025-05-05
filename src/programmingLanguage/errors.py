# User Issues:
class UserError:
    """Base class for user-related errors."""
    def __init__(self, type, message):
        print(f"{type}: {message}")
        exit(1)

class FileNotFoundError(UserError):
    """Exception raised when a file is not found."""
    def __init__(self, filename):
        super().__init__("FileNotFoundError", f"File '{filename}' not found.")

class CommandNotFoundError(UserError):
    """Exception raised when a command is not found."""
    def __init__(self, command):
        super().__init__("CommandNotFoundError", f"Command '{command}' not found.")

class VariableNotFoundError(UserError):
    """Exception raised when a variable is not found."""
    def __init__(self, variable):
        super().__init__("VariableNotFoundError", f"Variable '{variable}' not found.")

class SyntaxError(UserError):
    """Exception raised for syntax errors."""
    def __init__(self, message):
        super().__init__("SyntaxError", message)

# Language Issues:
class LanguageError(Exception):
    """Exception raised for language-related errors."""
    def __init__(self, message):
        self.message = 'Language Limitation Error: ' + message
        super().__init__(message)

class NotImplementedError(LanguageError):
    """Exception raised when a feature is not implemented."""
    def __init__(self, feature):
        self.feature = feature
        super().__init__(f"Feature '{feature}' is not implemented.")

class NotImportedError(LanguageError):
    """Exception raised when a feature is not imported."""
    def __init__(self, feature):
        self.feature = feature
        super().__init__(f"Feature '{feature}' is not imported.")

class UnkownError(LanguageError):
    """Exception raised for unknown errors."""
    def __init__(self, message):
        super().__init__(f"Unknown error: {message}")
