def tribonacci1(signature, n):
    li = signature
    x = sum(signature)
    for i in range(len(signature),n):
        print(i)
        win = li[i - 3:i]
        print(win)
        li.append(sum(win))
        print(li)
        # li[i]= sum(x for x in li)
        # print(li[i-3])
        # print(li[i-1])
        # print(sum(li[i-3, i-1]))
        # li.append(sum(x for x in li[i - 3:i - 1]))
    # return (li)

# def tribonacci2(signature, n):
#     li = signature
#     l = len(signature)
#     # for i in range(len(signature),n):
#     #     li.append(sum(li[i-3:i]))
#     # return (li)
#     [li.append(sum(li[i-l:i])) for i in range(l,n)]
#     return li

def tribonacci(signature, n):
    li = signature
    l = len(signature)
    [li.append(sum(li[i-l:i])) for i in range(l,n)]
    return li[:n]

# r = [1, 1 ,1, 3, 5, 9, 17, 31]
# a = [0, 1, 2]
# b = [1 ,2 ,3 ,4]
arr = [1, 1, 1]

print(tribonacci(arr,0))
# print(r[:2])
# print(a[len(a)-1])
# print(a[len(a) -4:len(a)-1])