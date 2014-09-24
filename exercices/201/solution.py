def alpha(x):
    y = list(str(x))
    import string
    alphaa = string.ascii_letters
    for i in range(len(y)):
        if y[i] in alphaa:
            return(True)
    return(False)
