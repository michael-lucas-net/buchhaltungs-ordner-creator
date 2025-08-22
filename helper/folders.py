import os
from pathlib import Path
from typing import List
import helper.names

# Structure
"""
2020
├── 1 Quartal
│   ├── 1 Januar
│   │   ├── Ausgehend
│   │   └── Eingehend
│   ├── 2 Februar
│   │   ├── Ausgehend
│   │   └── Eingehend
│   ├── 3 Maerz
│   │   ├── Ausgehend
│   │   └── Eingehend
│   └── Konto
"""

def folder_exists(path: str) -> bool:
    """Überprüft, ob ein Ordner existiert.
    
    Args:
        path: Der Pfad zum zu überprüfenden Ordner
        
    Returns:
        True wenn der Ordner existiert, False sonst
    """
    if path is None or not isinstance(path, str):
        return False
    return os.path.exists(path) and os.path.isdir(path)

def create_folder(path: str, name: str) -> bool:
    """Erstellt einen Ordner.
    
    Args:
        path: Der Basis-Pfad
        name: Der Name des zu erstellenden Ordners
        
    Returns:
        True wenn der Ordner erfolgreich erstellt wurde, False sonst
    """
    try:
        if path is None or name is None or not isinstance(path, str) or not isinstance(name, str):
            return False
            
        # Check for empty or whitespace-only strings
        if not path.strip() or not name.strip():
            return False
            
        folder_path = Path(path) / name
        if not folder_exists(str(folder_path)):
            folder_path.mkdir(parents=True, exist_ok=True)
            return True
        return True
    except Exception as e:
        print(f"Fehler beim Erstellen des Ordners {name}: {e}")
        return False

def delete_folder(path: str) -> bool:
    """Löscht einen Ordner.
    
    Args:
        path: Der Pfad zum zu löschenden Ordner
        
    Returns:
        True wenn der Ordner erfolgreich gelöscht wurde, False sonst
    """
    try:
        if path is None or not isinstance(path, str):
            return False
            
        if folder_exists(path):
            os.rmdir(path)
            return True
        return False
    except Exception as e:
        print(f"Fehler beim Löschen des Ordners {path}: {e}")
        return False

def create_bh_folders(year: str) -> bool:
    """Erstellt die Buchhaltungs-Ordnerstruktur für ein Jahr.
    
    Args:
        year: Das Jahr für das die Ordner erstellt werden sollen
        
    Returns:
        True wenn alle Ordner erfolgreich erstellt wurden, False sonst
    """
    try:
        if year is None or not isinstance(year, str) or year.strip() == "":
            return False
            
        for i in range(1, 5):
            quarter = helper.names.find_quarter(f"{i} Quartal")
            if quarter is None:
                print(f"Fehler: Quartal {i} nicht gefunden")
                return False
                
            quarter_name, months = quarter
            quarter_folder = Path(year) / quarter_name

            # Create year, quarter and account folders
            if not create_folder(".", year):
                return False
            if not create_folder(year, quarter_name):
                return False
            if not create_folder(str(quarter_folder), "Konto"):
                return False

            # Create months
            for month in months:
                month_folder = quarter_folder / month
                if not create_folder(str(quarter_folder), month):
                    return False

                # Create inbox and outbox folders
                for folder_name in helper.names.folder_names:
                    if not create_folder(str(month_folder), folder_name):
                        return False

        print("Fertig!")
        return True
        
    except Exception as e:
        print(f"Fehler beim Erstellen der Ordnerstruktur: {e}")
        return False
