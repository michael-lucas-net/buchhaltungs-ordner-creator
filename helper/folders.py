import os

# Ordnerstruktur
"""
2020
├── 1 Quartal
│   ├── 1 Januar
│   │   ├── Ausgehend
│   │   └── Eingehend
│   ├── 2 Februar
│   │   ├── Ausgehend
│   │   └── Eingehend
│   ├── 3 Maerz
│   │   ├── Ausgehend
│   │   └── Eingehend
│   └── Konto
"""

def createFolder(path, name):
    folderName = path + "/" + name
    if not folderExists(folderName):
        os.makedirs(folderName)

def folderExists(path):
    return os.path.exists(path) and os.path.isdir(path)
