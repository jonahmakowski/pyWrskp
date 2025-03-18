import os


def open_directory_in_files(directory):
    if os.path.isdir(directory):
        os.system("open {}".format(directory))
        return True
    else:
        return False
