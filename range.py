num_list = [28, 27, 26, 25, 24, 23, 22, 21]

res = []

for i in range(0,len(num_list), 2):
    # if i % 2 ==0:
    # print(i, num_list[i])
    res.append([num_list[i], num_list[i+1]])

print(res)

print(num_list[::2])

for i in num_list[::2]:
    print(i)

for i, n in enumerate(num_list):
    print(i,n)

print("\n")

for i, n in enumerate(num_list[::2]):
    print(i,n)

def solution(s):
    sol = []
    if len(s)%2 != 0:
        s += "_"
    for i in range(0,len(s) -1 ):
#         res = "".join(s[i],s[i+1])
        if i % 2 != 0:
            pass
        else:
            sol.append(s[i] + s[i+1])
    return sol

mystr = "abc"

print(solution(mystr))

