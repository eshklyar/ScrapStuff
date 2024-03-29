import itertools as it


def merge_arrays(arr1, arr2):
    x = []
    for i in it.chain(arr1, arr2):
        x.append(i)
    z = list(set(x))
    z.sort(reverse=False)
    return z


arr1 = [1, 2, 3, 4, 5]
arr2 = [6, 7, 8, 9, 9]
print(merge_arrays(arr1, arr2))
