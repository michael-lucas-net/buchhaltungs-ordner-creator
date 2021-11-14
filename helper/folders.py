import os
import helper.names

# structure
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

# Checks if a folder exists
def folderExists(path):
    return os.path.exists(path) and os.path.isdir(path)

# Creates a folder
def createFolder(path, name):
    folderName = path + "/" + name
    if not folderExists(folderName):
        os.makedirs(folderName)

# Deletes a folder
def deleteFolder(path):
    if folderExists(path):
        os.rmdir(path)

        
# Runs through all quarters and creates folders 
# (structure: See folders.py)
def createBhFolders(year):
    for i in range(1,5):
        quarter = helper.names.findQuarter(str(i) + " Quartal")
        quarterFolder = year + "/" + quarter[0] + "/"
        months = quarter[1]

        # Create year, quarter and account
        createFolder("./", year)
        createFolder("./", quarterFolder)
        createFolder(quarterFolder,"Konto")

        # Create months
        for month in months:
            createFolder(quarterFolder, month)            

            # Create inbox and outbox folder
            for folderName in helper.names.folderNames:
                createFolder(quarterFolder + month + "/", folderName)

    print("Fertig!")
