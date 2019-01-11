def convert(lf,symb):
    a = 0
    lf0 = ""
    b = str(symb)
    while a < len(lf):
        lf0 = lf0 + b + lf[a]
        a = a + 1
    return lf0
