from helper import folders, functions

def showWelcome():
    divier = "=============================="

    print(divier)
    print("        # WILLKOMMEN #")
    print("       Ordner-Erstellung")
    print("    (c) 2020-2021 Michael Lucas")
    print(divier)

def main():
    showWelcome()

    year = "0"
    while not functions.validateYear(year):
        year = functions.ask("Fuer welches Jahr sollen die Ordner erstellt werden? ")
    
    folders.createBhFolders(year)

main()
