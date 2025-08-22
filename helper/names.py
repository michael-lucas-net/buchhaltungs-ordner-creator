from typing import List, Tuple, Optional

# Folder names to be found in each month
folder_names: List[str] = ["Eingehend", "Ausgehend"]

# Each Quarter
quarters: List[Tuple[str, List[str]]] = [
    ["1 Quartal", ["1 Januar", "2 Februar", "3 Maerz"]],  
    ["2 Quartal", ["4 April", "5 Mai", "6 Juni"]], 
    ["3 Quartal", ["7 Juli", "8 August", "9 September"]], 
    ["4 Quartal", ["10 Oktober", "11 November", "12 Dezember"]],
]

def find_quarter(quarter: str) -> Optional[Tuple[str, List[str]]]:
    """Findet ein Quartal basierend auf dem Quartalnamen.
    
    Args:
        quarter: Der Name des Quartals (z.B. "1 Quartal")
        
    Returns:
        Ein Tuple mit (Quartalname, Liste der Monate) oder None wenn nicht gefunden
    """
    for qu in quarters:
        if quarter == qu[0]:
            return qu
    return None
