
import folders
import names

def showWelcome():
    divier = "=============================="

    print(divier)
    print("        # WILLKOMMEN #")
    print("       Ordner-Erstellung")
    print("    (c) 2020 Michael Lucas")
    print(divier)

def ask(what):
    return str(input(what));

def start():
    showWelcome()

    year = ask("Fuer welches Jahr sollen die Ordner erstellt werden? ")
    quarter = ask("Fuer welches Quartal sollen die Ordner erstellt werden? ")
    quarterFolder = year + "/" + names.quarterNames[int(quarter) - 1]

    folders.createFolder("./", year)
    folders.createFolder("./", quarterFolder)

    for fn in names.folderNames:
        folders.createFolder("./", quarterFolder + "/" + fn)


start()