arr = [10, 324, 45, 90, 9808]

# print(arr[-3:])

y = iter(arr)

# while y:
#     print(next(y))
for x in arr:
    print(x)
for e in y:
    print(e)
#     if next(y):
#         x = next(y)
#         print(f"next y{x}")
#         if e > next(y):
#             print("bigger")
#         else:
#             print("smaller")


# for i in range(len(arr)):
#     print(next(y))

# a1 = arr.copy()
#
# a1[0] = 5
#
# print(a1)
#
# array = [10, 5, 20, 8, 15]
#
# largest_element = max(array, key=lambda x: x)
# print("Largest element in the array:", largest_element)
#
# le = max(array)
# print(f"le {le}")

stack = []

# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')

print('Initial stack')
print(stack)

xs = [1, 2, 3]
y = " ".join(str(x) for x in xs)
print(y)
s = "hello world"
# print("".join([c for c in "hello world" if c != " "]))
# print("\n".join([c for c in "hello world" if c != " "]))
y = [print(c) for c in "hello world" if c != " "]
print(type(y))
print(len(y))
it = iter(y)
while y:
    print(next(it))