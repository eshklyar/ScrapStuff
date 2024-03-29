def century(year):
    return year / 100 if (year / 100).is_integer() else int(year / 100) +1

# print (int(1799/100))
# print((float(2000) / 100).is_integer())
# print(float(2001) / 100)


def century2(year):
    return (year + 99) // 100


print(century(781))