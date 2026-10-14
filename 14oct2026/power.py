def power(a,b):
    if b <=0:
        return
    return a*power(a,b-1)
    