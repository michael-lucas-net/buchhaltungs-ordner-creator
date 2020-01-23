
import folders

def showWelcome()   :
    divier = "=============================="

    print(divier)
    print("        # WILLKOMMEN #")
    print("       Ordner-Erstellung")
    print("    (c) 2020 Michael Lucas")
    print(divier)

    folders.createFolder("../", "yehaw")

showWelcome()