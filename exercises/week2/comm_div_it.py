def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a == b:
        return a
    elif a > b:
        test = b
        while a%test != 0 or b%test != 0:
            test -= 1
        return test
    else:
        test = a
        while a%test != 0 or b%test != 0:
            test -= 1
        return test