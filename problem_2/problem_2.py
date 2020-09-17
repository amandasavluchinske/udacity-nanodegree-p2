import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    suffix_ext = f'.{suffix}'

    if not os.path.exists(path):
        return None

    path_list = os.listdir(path)

    # Case 1: is file

    files = [f"{path}/{file}" for file in path_list if file.endswith(suffix_ext)]

    # Case 2: is folder

    folders = [folder for folder in path_list if "." not in folder]

    # Traverses folder recursively in search for file
    for folder in folders:
        files.extend(find_files(suffix, f"{path}/{folder}"))

    return files


find_files("c", "./testdir")