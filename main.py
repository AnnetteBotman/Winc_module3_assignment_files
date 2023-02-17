__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
from zipfile import ZipFile

# 1


def clean_cache():
    current_dir = os.getcwd()
    new_dir = os.path.join(current_dir, r'cache')
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
    else:
        for f in os.listdir(new_dir):
            os.remove(os.path.join(new_dir, f))


# 2
path = os.getcwd()
cachedir_path = os.path.join(path, 'cache')
datadir_path = os.path.join(path, 'data.zip')


def cache_zip(datadir_path, cachedir_path):
    clean_cache()
    with ZipFile(datadir_path, "r") as zip_ref:
        zip_ref.extractall(cachedir_path)


# 3


def cached_files():
    return [os.path.join(cachedir_path, file) for file in os.listdir(cachedir_path)]

# 4


file_list = cached_files()


def find_password(file_list):
    text = "password"
    for file in file_list:
        with open(file) as search_file:
            for line in (search_file):
                if text in line:
                    searched_line = line.split(" ", 1)
                    password = searched_line[1].strip()
                    return (password)


print(find_password(file_list))
