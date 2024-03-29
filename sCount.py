def count_sheep(n):
    arr = []
    for i in range(1, n+1):
        s = str(1) + " sheep..."
        arr.append(s)
    return "".join(arr)

print(count_sheep(5))