import errors

class Command:
    imported = {}
    def __init__(self, description: str, name: str, imp: bool):
        self.description = description
        self.imp = imp
        self.name = name
        Command.imported[self.name] = imp
    def __str__(self):
        return f"Command(name={self.name}, description={self.description})"
    def __repr__(self):
        return f"Command(name={self.name}, description={self.description})"
    def impo(self):
        if Command.imported[self.name]:
            return
        else:
            raise errors.NotImplementedError(f"Import of {self.name}")
    

class LoadFile(Command):
    def __init__(self):
        super().__init__(description="Load a file from the filesystem", name='LoadFile', imp=False)
    def load_params(self, file_path: str):
        self.file_path = file_path
    def execute(self):
        if not Command.imported:
            raise errors.NotImportedError("load_from_file")
        try:
            load_from_file = globals().get('load_from_file')
            return load_from_file(self.file_path)
        except FileNotFoundError:
            errors.FileNotFoundError(self.file_path)
    def impo(self):
        if not Command.imported[self.name]:
            Command.imported[self.name] = True
            from pyWrkspPackage import load_from_file
            globals()['load_from_file'] = load_from_file

class Print(Command):
    def __init__(self):
        super().__init__(description="Print a message to the console", name='Print', imp=True)
    def load_params(self, *args, sep: str = ' ', newline: bool = True):
        self.args = args
        self.sep = sep
        self.newline = newline
    def execute(self):
        print(*self.args, sep=self.sep, end='\n' if self.newline else '')

class Say(Command):
    def __init__(self):
        super().__init__(description="Say a message", name='Say', imp=False)
    def load_params(self, message: str):
        self.message = message
    def execute(self):
        if not Command.imported:
            raise errors.NotImportedError("say")
        speak = globals().get('speak')
        speak(self.message)
    def impo(self):
        if not Command.imported[self.name]:
            Command.imported[self.name] = True
            from pyWrkspPackage.audio import speak
            globals()['speak'] = speak

class Add(Command):
    def __init__(self):
        super().__init__(description="Add numbers", name='Add', imp=True)
    def load_params(self, *args):
        self.args = args
    def execute(self):
        try:
            return sum(self.args)
        except TypeError:
            errors.SyntaxError("Invalid arguments for addition")

class Sub(Command):
    def __init__(self):
        super().__init__(description="Subtract numbers", name='Subtract', imp=True)
    def load_params(self, *args):
        self.args = args
    def execute(self):
        try:
            return self.args[0] - sum(self.args[1:])
        except TypeError:
            errors.SyntaxError("Invalid arguments for subtraction")

class Mult(Command):
    def __init__(self):
        super().__init__(description="Multiply numbers", name='Multiply', imp=True)
    def load_params(self, *args):
        self.args = args
    def execute(self):
        try:
            result = 1
            for arg in self.args:
                result *= arg
            return result
        except TypeError:
            errors.SyntaxError("Invalid arguments for multiplication")

class Div(Command):
    def __init__(self):
        super().__init__(description="Divide numbers", name='Divide', imp=True)
    def load_params(self, *args):
        self.args = args
    def execute(self):
        try:
            result = self.args[0]
            for arg in self.args[1:]:
                result /= arg
            return result
        except TypeError:
            errors.SyntaxError("Invalid arguments for division")
