
from helper import names, folders, functions

def showWelcome():
    divier = "=============================="

    print(divier)
    print("        # WILLKOMMEN #")
    print("       Ordner-Erstellung")
    print("    (c) 2020 Michael Lucas")
    print(divier)


# Läuft alle Quartale durch und erstellt Ordner (Struktur: Sehe folders.py)
def createFolders(year):
    for i in range(1,5):
        quarter = names.findQuarter(str(i) + " Quartal")
        quarterFolder = year + "/" + quarter[0] + "/"
        months = quarter[1]

        # Jahr, Quartal und Konto erstellen
        folders.createFolder("./", year)
        folders.createFolder("./", quarterFolder)
        folders.createFolder(quarterFolder,"Konto")

        # Monate erstellen
        for month in months:
            folders.createFolder(quarterFolder, month)            

            # Eingang- und Ausgang- Ordner erstellen
            for folderName in names.folderNames:
                folders.createFolder(quarterFolder + month + "/", folderName)

def start():
    showWelcome()

    year = "0"
    while not functions.validateYear(year):
        year = functions.ask("Fuer welches Jahr sollen die Ordner erstellt werden? ")
    
    createFolders(year)

start()
