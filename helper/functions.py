from typing import Optional

def ask(what: str) -> str:
    """Fragt den Benutzer nach einer Eingabe und gibt diese zurück.
    
    Args:
        what: Die Frage, die dem Benutzer gestellt wird
        
    Returns:
        Die Benutzereingabe als String
    """
    return str(input(what))

def validate_year(val: Optional[str]) -> bool:
    """Überprüft, ob der gegebene Wert eine gültige Jahreszahl ist.
    
    Args:
        val: Der zu überprüfende Wert
        
    Returns:
        True wenn es sich um eine gültige Jahreszahl zwischen 1901 und 2099 handelt,
        False sonst
    """
    # Return false if val is None or not a string
    if val is None or not isinstance(val, str):
        return False

    # Checks if given val is a number and a year
    return val.isdigit() and 1901 <= int(val) <= 2099
    
