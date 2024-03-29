def merge(l1,l2):
    if not l1:  return list(l2)
    if not l2:  return list(l1)

    # l2 will contain last element.
    if l1[-1] > l2[-1]:
        l1,l2 = l2,l1

    it = iter(l2)
    y = next(it)
    result = []

    for x in l1:
        while y < x:
            result.append(y)
            y = next(it)
        result.append(x)
    result.append(y)
    result.extend(it)
    return result

list1 = [1,3,5,7,9,11]
list2 = [2,4,6,8]

print(merge(list1,list2))