import os

def read(path):
    to_read = open(path, "r")
    content = to_read.read()
    to_read.close()
    return content

def save(path, content)
    to_write = open(path, "w")
    to_write.write(content)
    to_write.close()

def create_folder_if_not_exist(path):
    if not os.path.exists(directory):
        os.makedirs(directory)