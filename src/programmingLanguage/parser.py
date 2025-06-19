from inspect import getmembers, isclass
import commands
import errors
from pyWrkspPackage import load_from_file, run_in_thread

commands_avalible_direct = classes_in_module = [
    {"exec": obj, "name": obj.__name__}
    for _, obj in getmembers(commands, isclass)
    if obj.__module__ == commands.__name__ and obj.__name__ != "Command"
]

commands_avalible = {}

for command in commands_avalible_direct:
    command_name = command["name"]
    command_class = command["exec"]
    commands_avalible[command_name] = command_class

variables = {}
"""
In format of:
{
    'var_name': {
        'value': value,
        'type': type
    }
}
"""


def get_tokens(line: str) -> list:
    # Remove comments
    line = line.split("#")[0]
    # Split by whitespace
    tokens = line.split()
    # Remove empty tokens
    tokens = [token for token in tokens if token]
    return tokens


def parse_line(line: str):
    global variables
    tokens = get_tokens(line)
    if tokens == []:
        return None

    reconsturcted_line = []

    for token in tokens:
        if token in variables.keys():
            reconsturcted_line.append(variables[token]["value"])
        else:
            reconsturcted_line.append(token)

    prev = []

    for index in range(len(reconsturcted_line) - 1, -1, -1):
        cur_token = reconsturcted_line[index]
        if "!" in cur_token:
            if cur_token.index("!") != 0:
                errors.SyntaxError(
                    "Syntax error, ! must be at the start of the variable"
                )
            var_name = cur_token[1:]
            if var_name not in variables.keys():
                errors.VariableNotFoundError(var_name)
            else:
                prev.append(variables[var_name]["value"])
        elif ":" not in cur_token:
            if isinstance(cur_token, str):
                if cur_token.isnumeric():
                    prev.append(int(cur_token))
                elif cur_token.replace(".", "", 1).isdigit():
                    prev.append(float(cur_token))
                else:
                    prev.append(cur_token)
            else:
                raise errors.UnkownError(
                    f"Unknown value {cur_token} of type {type(cur_token)}"
                )
        elif cur_token.replace(":", "") in commands_avalible.keys():
            command = commands_avalible[cur_token.replace(":", "")]()
            command.load_params(*prev)
            command.impo()
            prev = []
            output = command.execute()
            if output is not None:
                prev.append(output)
        else:
            if len(prev) == 1:
                value = prev[0]
                if isinstance(value, int):
                    variables[cur_token.replace(":", "")] = {
                        "value": value,
                        "type": "int",
                    }
                elif isinstance(value, float):
                    variables[cur_token.replace(":", "")] = {
                        "value": value,
                        "type": "float",
                    }
                elif isinstance(value, str):
                    variables[cur_token.replace(":", "")] = {
                        "value": value,
                        "type": "str",
                    }
                else:
                    raise errors.SyntaxError(
                        f"Syntax error, cannot assign {cur_token} to {value}"
                    )
            elif len(prev) > 1:
                variables[cur_token.replace(":", "")] = {"value": prev, "type": "list"}
            else:
                raise errors.SyntaxError(
                    f"Syntax error, cannot assign {cur_token} to nothing"
                )
            prev = []


def parse_file(file_path: str):
    file = load_from_file(file_path)

    file = file.split("\n")

    threads = []

    for line in file:
        for command in commands_avalible:
            if command in line:
                # Check if the command is preceded by a comment
                comment_index = line.find("#")
                command_index = line.find(command)
                if comment_index != -1 and comment_index < command_index:
                    continue  # Skip if the command is commented out
                if (
                    command not in commands.Command.imported.keys()
                    or not commands.Command.imported[command]
                ):
                    print(f"Command {command} found in file, importing...")
                    threads.append(run_in_thread(commands_avalible[command]().impo()))

    for thread in threads:
        thread.join()

    for line in file:
        parse_line(line)


if __name__ == "__main__":
    parse_file("example.jonahscript")
    print(variables)
