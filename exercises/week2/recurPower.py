def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    result = base
    if exp == 0:
        return 1
    elif exp == 1:
        return result
    else:
        z = recurPower(base, exp-1)
        return result * z