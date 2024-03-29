import math
def find_next_square(sq):
    print(math.sqrt(sq))
    print(type(math.sqrt(sq)))
    if math.sqrt(sq).is_integer():
        return int((math.sqrt(sq) +1) ** 2)
    else:
        return -1

print(find_next_square(121))

def sqr(x):
    if (x%1):
        return "sub"
    else:
        return "nope"


def sqr2(x):
    return "sub" if x % 1 else "nope"

print(sqr2(5.0))