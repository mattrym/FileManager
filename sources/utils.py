import os.path

def get_basename(path):
    return os.path.basename(path)

def get_parent(path):
    return os.path.dirname(path)

def get_abspath(relpath, rootpath):
    return os.path.join(rootpath, relpath)

def get_relpath(relpath, parent_relpath = ""):
    return os.path.join(parent_relpath, relpath)

def get_subitems(relpath, rootpath):
    abspath = get_abspath(relpath, rootpath)
    result = [get_relpath(subitem, relpath) for subitem in os.listdir(abspath)]
    return result

def get_subdirs(relpath, rootpath):
    return [path for path in get_subitems(relpath, rootpath)
            if os.path.isdir(get_abspath(path, rootpath))]

def get_subfiles(relpath, rootpath):
    return [path for path in get_subitems(relpath, rootpath) 
            if not os.path.isdir(get_abspath(path, rootpath))]
