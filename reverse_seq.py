def reverse_seq(n):
    i = [x for x in range(1, n+1)]
    i.sort(reverse=True)
    print(i)

    y = list(range(n, 0, -1))
    print(y)

    z = [(range(n, 0, -1))]
    print(type(z))
    print(z[0])


    return sorted([num for num in range(1,n+1)], reverse=True)
    # return range(n, 0, -1)




print(reverse_seq(5))