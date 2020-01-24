
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
    

    quarterNumber = ask("Fuer welches Quartal sollen die Ordner erstellt werden? ")
    quarter = names.findQuarter(quarterNumber + " Quartal")

    quarterFolder = year + "/" + quarter[0]

    folders.createFolder("./", year)
    folders.createFolder("./", quarterFolder)

    months = quarter[1]

    for month in months:
        currentFolder = quarterFolder + "/" + month
        folders.createFolder(quarterFolder, "/" + month)
        folders.createFolder(quarterFolder, "/" + "Konto")

        for folderName in names.folderNames:
            folders.createFolder(currentFolder + "/", folderName)


start()