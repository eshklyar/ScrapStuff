import random


# def productExceptSelf( nums: [int]) -> [int]:
#     # li = []
#     # for i, n in enumerate(nums):
#     #     a = nums[:i]
#     return [1,2,3]
#
#
#
# numbers = [1,2,3,4]
# print(productExceptSelf(numbers))

# nums = []
# for i in range(20):
#     nums.append(random.randint(0, 9))
# # print(nums)
#
# for i in range(len(nums)):
#     print(nums[:i] + nums[:i])

# print(nums[:i], len(nums[:i]))
# print(nums[i:], len(nums[i:]))
# print(len(nums), len(nums[:i])+len(nums[i:]))


# [x*j for x in nums for j in nums[:nums.index(x)]]

def sq(n):
    li = []
    for j in nums:
        i = nums.index(j)
        su = 1
        for k in nums[:i] + nums[i + 1:]:
            su *= k
        li.append(su)
    return li


nums = [x for x in range(1, 5)]
print(nums)
print(sq(nums))

#
# def sq1(nums):
#     return [sum(j * k for k in nums[:i] + nums[i + 1:]) for i, j in enumerate(nums)]


# Test the function
# nums1 = [1, 2, 3, 4]
# result = sq(nums1)
# print(result)
# print(f" i is {i}, j is {j}")
# print(f" j is {j}  {nums[:i] + nums[i+1:]}")
# print(nn)
# x = [nums.index(i) for i in nums[nums.index(i)]]
# print(nums)
# print(x)

# x = [j*i for j in nums for i in nums[:nums.index(j)] + nums[nums.index(j)+1:]]
# x = [i for i in nums[:nums.index(j)] + nums[nums.index(j)+1:]]
# print(x)
