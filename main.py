from helper import folders, functions

def show_welcome():
    """Zeigt die Willkommensnachricht an."""
    divider = "=============================="

    print(divider)
    print("        # WILLKOMMEN #")
    print("       Ordner-Erstellung")
    print("    (c) 2020-2021 Michael Lucas")
    print(divider)

def main():
    """Hauptfunktion des Programms."""
    try:
        show_welcome()

        year = "0"
        while not functions.validate_year(year):
            year = functions.ask("Fuer welches Jahr sollen die Ordner erstellt werden? ")
        
        folders.create_bh_folders(year)
        print("Ordner erfolgreich erstellt!")
        
    except KeyboardInterrupt:
        print("\nProgramm wurde abgebrochen.")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")

if __name__ == "__main__":
    main()
