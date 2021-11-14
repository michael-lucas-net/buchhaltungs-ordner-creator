
# ask user for input
# and return the input
def ask(what):
    return str(input(what))

# Checks if the given value is a number and a year
def validateYear(val):

    # return false if val is none or not a string
    if val is None or not isinstance(val, str):
        return False

   # checks if given val is a number and a year
    return val.isdigit() and int(val) > 1900 and int(val) < 2100
    
