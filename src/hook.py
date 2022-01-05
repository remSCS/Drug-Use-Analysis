import os

def find_file(fullname, extension, path=""):
    name = fullname.rsplit(".", 1)[-1]
    FILE_PATH = file_path(name, extension, path=path)
    if os.path.isfile(FILE_PATH):
        return FILE_PATH
    name = name.replace("_", " ")
    FILE_PATH = file_path(name, extension, path=path)
    if os.path.isfile(FILE_PATH):
        return FILE_PATH

def file_path(name, extension, path=""):
    fullpath = path + "%s" % (name + extension)
    ROOT_PATH = os.path.dirname(os.path.abspath(fullpath))
    print(os.path.join(ROOT_PATH, name + extension))
    return os.path.join(ROOT_PATH, name + extension)