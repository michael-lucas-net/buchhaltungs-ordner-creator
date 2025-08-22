# Buchhaltungs-Ordner-Creator

Ein Python-Tool zur automatischen Erstellung von Buchhaltungs-Ordnern für ein bestimmtes Jahr.

## Features

- Automatische Erstellung einer vollständigen Buchhaltungs-Ordnerstruktur
- Validierung der Jahreszahl (1901-2099)
- Fehlerbehandlung und Benutzerfreundlichkeit
- Plattformunabhängig (Windows, macOS, Linux)

## Ordnerstruktur

Das Tool erstellt folgende Struktur für das eingegebene Jahr:

```
2024/
├── 1 Quartal/
│   ├── 1 Januar/
│   │   ├── Ausgehend/
│   │   └── Eingehend/
│   ├── 2 Februar/
│   │   ├── Ausgehend/
│   │   └── Eingehend/
│   ├── 3 Maerz/
│   │   ├── Ausgehend/
│   │   └── Eingehend/
│   └── Konto/
├── 2 Quartal/
│   ├── 4 April/
│   │   ├── Ausgehend/
│   │   └── Eingehend/
│   ├── 5 Mai/
│   │   ├── Ausgehend/
│   │   └── Eingehend/
│   ├── 6 Juni/
│   │   ├── Ausgehend/
│   │   └── Eingehend/
│   └── Konto/
├── 3 Quartal/
│   ├── 7 Juli/
│   │   ├── Ausgehend/
│   │   └── Eingehend/
│   ├── 8 August/
│   │   ├── Ausgehend/
│   │   └── Eingehend/
│   ├── 9 September/
│   │   ├── Ausgehend/
│   │   └── Eingehend/
│   └── Konto/
└── 4 Quartal/
    ├── 10 Oktober/
    │   ├── Ausgehend/
    │   └── Eingehend/
    ├── 11 November/
    │   ├── Ausgehend/
    │   └── Eingehend/
    ├── 12 Dezember/
    │   ├── Ausgehend/
    │   └── Eingehend/
    └── Konto/
```

## Installation

1. Stelle sicher, dass Python 3.7 oder höher installiert ist
2. Klone oder lade das Repository herunter
3. Keine zusätzlichen Abhängigkeiten erforderlich

## Verwendung

```bash
python main.py
```

Das Programm wird Sie nach dem Jahr fragen, für das die Ordner erstellt werden sollen.

## Tests ausführen

```bash
python tests.py
```

## Code-Qualität

Der Code folgt den PEP 8 Style Guidelines und verwendet:
- Typisierung (Type Hints)
- Umfassende Dokumentation
- Fehlerbehandlung
- Unit Tests
- Moderne Python-Features (pathlib, f-strings)

## Lizenz

(c) 2020-2021 Michael Lucas
