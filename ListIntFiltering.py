def filter_list_incuding_str(l):
    numbers = []
    for i in range(10):
        numbers.append(str(i))

    li = []
    for st in l:
        if type(st) is str:
            count = 0
            for c in st:
                if c in numbers:
                    count += 1
            if count == len(st):
                li.append(int(st))
        else:
            li.append(st)
    return list(dict.fromkeys(li))

def filter_list(l):
    li = []
    for n in l:
        if type(n) == int:
            li.append(n)
    return li

def f_l(l):
    return [x for x in l if type(x) == int]


aList = [1,2,'aasf','1','123',123]
print(filter_list(aList))

print(f_l(aList))
