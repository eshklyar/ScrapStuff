def between(a,b):
    return [x for x in range(a,b+1)]

print(between(2,8))

print(13 // 10)

print(len(str(222)))

def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    n = len(str(b))
    x = 10**(n-1)
    print(list(range(n)))
    ten_list = [10**x for x in range(n-1,-1,-1)]

    return []

sum_dig_pow(1,345)