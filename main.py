
import folders
import names
import sys

def showWelcome():
    divier = "=============================="

    print(divier)
    print("        # WILLKOMMEN #")
    print("       Ordner-Erstellung")
    print("    (c) 2020 Michael Lucas")
    print(divier)

def ask(what):
    return str(input(what));

# Prüft, ob die eingegebene Zahl legal ist
def validate(val):
    length = len(val)

    if (length != 4):
        print("Illegaler Längenwert!")
        return False

    if (not val.isdigit()):
        print("Keine Zahl!")
        return False

    return True

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

        for month in months:
            folders.createFolder(quarterFolder, month)            

            # Eingang- und Ausgang- Ordner erstellen
            for folderName in names.folderNames:
                folders.createFolder(quarterFolder + month + "/", folderName)

def start():
    showWelcome()

    year = ask("Fuer welches Jahr sollen die Ordner erstellt werden? ")

    # Prüfen, ob zahl valide ist
    if (not validate(year)):
        sys.exit(1)
    
    createFolders(year)

start()