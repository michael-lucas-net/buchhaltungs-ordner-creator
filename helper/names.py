# Folder names to be found in each month
folderNames = ["Eingehend", "Ausgehend"]

# Each Quarter
quarters = [
    ["1 Quartal", ["1 Januar", "2 Februar", "3 Maerz"]],  
    ["2 Quartal", ["4 April", "5 Mai", "6 Juni"]], 
    ["3 Quartal", ["7 Juli", "8 August", "9 September"]], 
    ["4 Quartal", ["10 Oktober", "11 November", "12 Dezember"]],
]

# Called with e.g. findQuarter('1 Quartal')
def findQuarter(quarter):
    for qu in quarters:
        if quarter == qu[0]:
            return qu
