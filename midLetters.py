def get_middle(s):
    index, odd = divmod(len(s), 2)
    print(index,odd)
    # if len(s) %2:
    #     print("odd")
    #     return s[len(s)//2]
    # else:
    #     print("even")
    #     return s[len(s)//2 -1] + s[len(s)//2]

    return s[len(s)//2] if len(s) %2 else s[len(s)//2 -1] + s[len(s)//2]

print(get_middle("middle"))
print(get_middle("123"))
# y = ([str(x) for x in range(6)])
# print(y)
# print(len(y))
# print(len(y)//2)
# print(y[len(y)//2])
# z = 5
# if z%2:
#     print("odd")
# else:
#     print("even")

i, j = divmod(5,2)
print(i,j)
z = divmod(5,2)
print(z[0])