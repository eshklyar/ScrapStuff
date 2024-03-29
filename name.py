def abbrev_name(name):
    n = name.split(" ")
    return f"{str.upper(n[0][0])}.{str.upper(n[1][0])}"
    # return '.'.join(w[0] for w in name.split()).upper()
print(abbrev_name("patrick feeney"))