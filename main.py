
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

            # Eingang, Ausgang- Ordner erstellen
            for folderName in names.folderNames:
                folders.createFolder(quarterFolder + month + "/", folderName)

start()