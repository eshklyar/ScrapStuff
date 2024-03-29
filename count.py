l = ["a","b","b"]

z = [[x,l.count(x)] for x in set(l)]
print(z)
# [['a', 1], ['b', 2]]

zz = dict((x,l.count(x)) for x in set(l))
print(zz)
# {'a': 1, 'b': 2}