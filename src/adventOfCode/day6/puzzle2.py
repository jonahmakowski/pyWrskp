import pyWrkspPackage
import multiprocessing


def find_guard(data):
    """
    Finds the position of the guard in the puzzle grid.

    Args:
        data (list): The current state of the puzzle grid.

    Returns:
        tuple: The (x, y) position of the guard.

    Raises:
        Exception: If no guard is found in the puzzle grid.
    """
    for y, row in enumerate(data):
        for x, item in enumerate(row):
            if item == "^":
                return x, y
    raise Exception("No guard found")


def mainloop(data: list, direc: tuple, was: any):
    """
    Executes the main loop of the puzzle, updating the data based on the current direction and position.

    Args:
        data (list): The current state of the puzzle grid.
        direc (tuple): The current direction of movement as a tuple (dirx, diry).
        was (any): The previous state of the cell.

    Returns:
        tuple: Updated data, new direction, whether the guard reached 9, and the previous state of the cell.
    """
    on_nine = False
    x, y = find_guard(data)
    dirx, diry = direc
    if (
        data[y + diry][x + dirx] == "." or data[y + diry][x + dirx] == "X"
    ) or isinstance(data[y + diry][x + dirx], int):
        data[y][x] = 1 if was == "." else was + 1
        was = data[y + diry][x + dirx]
        if data[y][x] >= 10:
            on_nine = True
        data[y + diry][x + dirx] = "^"
        return data, direc, on_nine, was
    if data[y + diry][x + dirx] == "#" or data[y + diry][x + dirx] == "B":
        if direc == (0, -1):
            direc = (1, 0)
        elif direc == (1, 0):
            direc = (0, 1)
        elif direc == (0, 1):
            direc = (-1, 0)
        else:
            direc = (0, -1)
        return data, direc, on_nine, was
    raise Exception("Invalid data")


def find_all_options(data, solved):
    """
    Finds all possible options for placing 'B' in the puzzle grid.

    Args:
        data (list): The current state of the puzzle grid.
        solved (list): The solved state of the puzzle grid.

    Returns:
        list: A list of dictionaries containing the new data state and the location of 'B'.
    """
    options = []
    for y, row in enumerate(data):
        print("Running row {}, {} options so far".format(y, len(options)))
        for x, _ in enumerate(row):
            data_copy = pyWrkspPackage.recursive_copy(data)
            if data_copy[y][x] == "." and solved[y][x] == "X":
                data_copy[y][x] = "B"
                if data_copy not in options:
                    options.append({"data": data_copy, "location": (x, y)})
    return options


def check_valid(data, options, index, required_count=1):
    """
    Checks if a given option is valid by running the main loop and counting the number of active steps.

    Args:
        data (dict): A dictionary containing the 'data' and 'location' keys.
        options (multiprocessing.Array): An array to store the validity of each option.
        index (int): The index of the current option in the options array.
        required_count (int, optional): The number of consecutive active steps required to consider the option valid. Defaults to 1.

    Returns:
        bool: True if the option is valid, False otherwise.
    """
    data = data["data"]
    data, direc, active, was = mainloop(data, (0, -1), ".")
    active_count = 0
    while True:
        try:
            data, direc, active, was = mainloop(data, direc, was)
            if active:
                active_count += 1
            else:
                active_count = 0

            if active_count >= required_count:
                options[index] = True
                return True
        except IndexError:
            options[index] = False
            return False


def count(items):
    """
    Counts the number of truthy items in the given iterable.

    Args:
        items (iterable): An iterable of items to be counted.

    Returns:
        int: The count of truthy items in the iterable.
    """
    return sum(1 for item in items if item)


def main():
    """
    data = pyWrkspPackage.load_from_file("input.txt").split("\n")
    data = [list(item) for item in data]

    solved = pyWrkspPackage.recursive_copy(data)
    solved, direc = mainloop(solved, (0, -1))
    while True:
        try:
            solved, direc = mainloop(solved, direc)
        except IndexError:
            player_x, player_y = find_gaurd(solved)
            solved[player_y][player_x] = 'X'
            break

    options = find_all_options(data, solved)
    pyWrkspPackage.json_write_file("options_cache.json", options)
    """
    options = pyWrkspPackage.json_load_file("options_cache.json")

    valid_options = multiprocessing.Array("i", len(options))

    threads = []

    for index, option in enumerate(options):
        threads.append(
            multiprocessing.Process(
                target=check_valid, args=(option, valid_options, index)
            )
        )
        threads[-1].start()
        if index % 40 == 0:
            for thread in threads:
                print("Joining thread...", end=" ")
                thread.join()
                print("Done")
            threads = []
            print(
                "So far {} valid options. Started threads up to {} of {}".format(
                    count(valid_options), index, len(options)
                )
            )

    print("-" * 20, "All threads started, waiting for finish", "-" * 20)
    for thread in threads:
        print("Joining thread...", end=" ")
        thread.join()
        print("Done")

    return count(valid_options)


if __name__ == "__main__":
    print(main())
