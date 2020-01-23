import os

def createFolder(path, name):
    folderName = path + "/" + name;
    if not folderExists(folderName):
        os.makedirs(folderName)

def folderExists(path):
    return os.path.exists(path) and os.path.isdir(path)