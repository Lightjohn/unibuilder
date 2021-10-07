import os
from os.path import join


def is_exe(path, binary):
    file_path = join(path, binary)
    return os.path.isfile(file_path) and os.access(file_path, os.X_OK)


def get_bins_from_path():
    available_binaries = list()
    for path in os.environ["PATH"].split(":"):
        try:
            for binary in os.listdir(path):
                if is_exe(path, binary):
                    available_binaries.append(binary)
        except FileNotFoundError:
            pass    # Path folder do not exist, can be ignored
    return available_binaries


