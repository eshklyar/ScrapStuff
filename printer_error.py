import string
def printer_error(s):
    letters = string.ascii_letters[:int(len(string.ascii_letters) / 2)]
    reLetters = letters[letters.index("m")+1:]
    x = sum([1 for c in s if c in reLetters])
    print(x)
    return f"{sum([1 for c in s if c in reLetters])}/{len(s)}"


s1 = "aaabbbbhaijjjm"
s2 = "aaaxbbbbyyhwawiwjjjwwm"

printer_error(s1)
printer_error(s2)

print(printer_error(s1))
print(printer_error(s2))


print(string.ascii_letters)
print(len(string.ascii_letters) / 2)
print(string.ascii_letters[:int(len(string.ascii_letters) / 2)])
letters = string.ascii_letters[:int(len(string.ascii_letters) / 2)]
print(letters.index("a"))
print(letters[letters.index("m")+1:])