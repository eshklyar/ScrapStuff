def xo(s):
    for x in s:
        print(x.upper())
    y = [c for c in s]
    print(y)
    print(type(y))
    print("".join(y))
    print(s.count("x".upper()))
    print(s.count("o".upper()))

    print(s.upper().count("x")
    return s.count("x".upper()) == s.count("o".upper())

print(xo("xooxx"))