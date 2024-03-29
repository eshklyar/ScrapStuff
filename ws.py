def sum_array(a):
    return sum(x for x in a)

input = [1, 5.2, 4, 0, -1]

print(sum_array(input))


def high_and_low(numbers):
    print(x for x in numbers)
    z = " ".split(numbers)
    x = " ".split(numbers).sort()

    y = sorted(" ".split(numbers))
    print(z)
    return numbers
def high_and_low2(num):
    # count = 0
    # for c in num:
    #     print(c)
    #     count += 1
    # print(count)

    print(f"{sorted(num.split()).pop()} {sorted(num.split(), reverse=True).pop()}")


    sp = num.split()
    print(sp)

    # spi = (int(x), x for c in sp)
    spd = list(dict.fromkeys(sp))
    print(f"this is spd {spd}")
    # sr = int(sorted(sp))

    spi = [int(x) for x in sp]
    spi2 = [int(x) for x in num.split()]
    print(f"this is spi {spi}")
    sr = sorted(spi)

    print((sr))

    srr = sorted(spi, reverse= True)
    print(srr)

    l = sr.pop()
    print(f"this is l {l}")

    f = srr.pop()
    print(f)
    # sp2 = "".split(num)   ???
    # print(sp2)            ???
high_and_low("1 2 3 4 5")
high_and_low2("8 3 -5 42 -1 0 0 -9 4 7 4 -4")

x = int (5)

y = int(7)
print(x)
print(type(x))

zz= "zz"
yy = "yy"

xx = " ".join([zz, yy])
print(xx)

def high_and_low3(numbers):
    li = [int(x) for x in numbers.split()]
    # sortedLi = sorted(li)
    last = str(sorted(li).pop())
    first = str(sorted(li, reverse=True).pop())
    r = " ".join([first, last])
    print(r)
    return (" ".join(str(sorted([int(x) for x in numbers.split()]).pop)), str(sorted([int(x) for x in numbers.split()], reverse= True).pop))

x = high_and_low3("8 3 -5 42 -1 0 0 -9 4 7 4 -4")

print(x)


def lovefunc( flower1, flower2 ):
    # if ((flower1 + flower2 +1 ) % 2):
    #     return False
    # else:
    #     return True
    return (flower1 + flower2) % 2 ==1
print(lovefunc(1,4))

def duplicate_count(text):
    print(len(text.lower()))
    print(len(set(text.lower())))

duplicate_count("Indivisibilities")