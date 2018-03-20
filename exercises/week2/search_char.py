def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) == 0:
        return False
    midchar = aStr[int(len(aStr)/2)]
    if char == midchar:
        return True
    elif len(aStr) == 1:
        return False
    elif char > midchar:
        return isIn(char, aStr[int(len(aStr)/2):])
    elif char < midchar:
        return isIn(char, aStr[:int(len(aStr)/2)])