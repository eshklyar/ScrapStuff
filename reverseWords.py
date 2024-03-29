def reverseWords(s: str) -> str:
    return " ".join(s.split()[::-1])
def productExceptSelf( nums: [int]) -> [int]:
    # for i, _ in enumerate (nums):
    #     print(f"i {nums[i]}")
    #     print(f"prev {nums[:i]}")
    #     print(f"post {nums[i+1:]}")
    res = []
    sum = 0
    for i, n in enumerate(nums):
        x = nums[:i] + nums[i+1:]
        # print(f" numbers {numbers}")
        # print(f"i of n is {i} and {n}")
        # print(f"x {x}")
        # print(f"prev {nums[:i]}")
        # print(f"post {nums[i+1:]}")

        for z in x:
            # print(f"z*n is {z*n}")
            sum += z * n
            # print(f"sum {sum}")
        res.append(sum)
        # print(f"res is {res}")
        sum = 0
    return res
# numbers = [2,5,4,7,8,4]


def productExceptSelf2( nums: [int]) -> [int]:
    res = []
    for i, n in enumerate(nums):
        sum = 0
        x = nums[:i] + nums[i+1:]
        for z in x:
            sum += z * n
        res.append(sum)
    return res

numbers = [1, 2, 3, 4, 5, 6]

print(productExceptSelf2(numbers))

def sol(num: int):
    # result = []
    # last = ""
    for i in range(0, len(num), 2):

        print(f"i is {i} and num is {num[i]}")
    # if len(num)%2 == 0:
    #     for i in range(0, len(num), 2):
    #     last = num[len(num) - 1]
    # else:
    #     last = "_"
    # print(num[i])


    # print(numbers[i+1])
    # print(last)

# print(len(numbers) -1)

numZ = []
numOne = [1]
numTwo = [1,2]
numOdd = [1, 2, 3, 4, 5]
numEv = [1, 2, 3, 4, 5, 6]


sol(numZ)
print("\n")
sol(numOne)
print("\n")
sol(numTwo)
print("\n")
sol(numOdd)
print("\n")
sol(numEv)

newnums = [1,2,3,4,5,6,7,8,9,10]

for i , n in enumerate(newnums):
    if i %2 ==0:
        print(f"this is i {i}, and this is n {n}")
    print(f"this is i {i}, and this is n {n}")
for i in range(len(newnums)):
    print(f"size is {len(newnums)}")
    print(f"this is i {i}, and this is n {n}")


num_list = [28, 27, 26, 25, 24, 23, 22]

for i in range(0,len(num_list) -1, 2):
    # if i % 2 ==0:
    print(i, num_list[i])

print(num_list[::2])
for i in num_list[::2]:
    print(i, num_list[i])

for i in range(len(num_list)):
    print(num_list[i])