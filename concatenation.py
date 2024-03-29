import itertools


list1 = [10, 11, 12, 13, 14]
list2 = [20, 30, 42]

print("list1 before concatenation:\n" + str(list1))
list1.extend(list2)
print ("Concatenated list i.e ,ist1 after concatenation:\n"+ str(list1))


res = [*list1, *list2]
print("Concatenated list:\n " + str(res))


res = [j for i in [list1, list2] for j in i]
print ("Concatenated list:\n"+ str(res))


res = list(itertools.chain(list1, list2))
print("Concatenated list:\n " + str(res))