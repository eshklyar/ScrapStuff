import itertools as it

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# q = my_list[-2:-1] explains how to get the last element in a list   # [19]
# q = my_list[-2:] explains how to get the last two elements in a list # [19, 20]
# q = my_list[:-2] explains how to get all but the last two elements in a list # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
# # 10, 11, 12, 13, 14, 15, 16, 17]
# q = my_list[-1:] explains how to get the last element in a list # [19]
# q = my_list[-1] explains how to get the last element in a list # 19

# print(f"this is q: {q}")
print(my_list[-1])
print(my_list[-1:])
print(my_list[:-1])
print(my_list[-2:])
print(my_list[-2:-1])
print(my_list[-2:-2])
print(my_list[:2])


start_with_zero_list = [0, 3, 6, 9, 12, 15]
# zero_and_one_list = [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1]
zero_and_one_list = [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0]
print(f"this is zero_and_one_list: {zero_and_one_list}")




prev = 0
curr = 0
next = 0
count = 0
# l = len(my_list)-1
# e = my_list[l]
# sl = my_list[:l]
# s = my_list[:]

# print(f"this is sl: {sl}")
# print(f"this is s: {s}")
#
#
# print(f"this is l: {l}")
# print(f"this is e: {e}")

# if zero_and_one_list[0] == 0 and zero_and_one_list[1] == 0:
#     count += 1
#     zero_and_one_list[0] = 1
if zero_and_one_list[:2] == [0, 0]:
    count += 1
    zero_and_one_list[0] = 1

for i,n in it.islice(enumerate(zero_and_one_list), 1, len(zero_and_one_list)-1):
    # print(f"this is i: {i} and this is n: {n}"
    prev = zero_and_one_list[i-1]
    curr = zero_and_one_list[i]
    next = zero_and_one_list[i+1]
    # print(f"this is prev: {prev}")
    # print(f"this is curr: {curr}")
    # print(f"this is next: {next}")
    if [prev, curr, next] == [0, 0, 0]:
        count += 1
        zero_and_one_list[i] = 1

if zero_and_one_list[-3:] == [1, 0, 0]:
    count += 1

print(count)
print(f"this is zero_and_one_list: {zero_and_one_list}")

# for i,n in enumerate(zero_and_one_list):
#     # print(f"this is i: {i} and this is n: {n}")
#     prev = zero_and_one_list[i-1]
#     curr = zero_and_one_list[i]
#     next = zero_and_one_list[i+1]
#     print(f"this is prev: {prev}")
#     print(f"this is curr: {curr}")
#     print(f"this is next: {next}")
# y = my_list[:my_list[len(my_list) -1]]
# print(f"this is y: {y}")
# z = my_list[:2]
# print(f"this is z: {z}")


# x = len(start_with_zero_list) - 1
# print(f"this is x: {x} and the element at index x is: {start_with_zero_list[x]}")
#
# for i,n in enumerate(start_with_zero_list):
#     print(f"this is i: {i} and this is n: {n}")
