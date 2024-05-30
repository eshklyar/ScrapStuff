import math

# def fibonacci(n: int) -> int:
#     fib_values = [0, 1] + [0] * (n - 1)
#
#     for i in range(2, n + 1):
#         fib_values[i] = fib_values[i - 1] + fib_values[i - 2]
#
#     return fib_values[n]



from typing import Dict, Optional


# def fibonacci(n: int, recursive_hash: Optional[Dict[int, int]] = None) -> int:
#     if recursive_hash is None:
#         recursive_hash = {}
#
#     if n in recursive_hash:
#         return recursive_hash[n]
#
#     if n <= 1:
#         return n
#
#     recursive_hash[n] = fibonacci(n - 1, recursive_hash) + fibonacci(n - 2, recursive_hash)
#
#     return recursive_hash[n]
#
#
# n = 4
# f = fibonacci(n)
# print(f)  # Output: 3


def fibonacci(n: int, recursive_hash: dict = None) -> int:
    if recursive_hash is None:
        recursive_hash = {0:0,1:1}
    if n in recursive_hash:
        return recursive_hash[n]
    # if n <= 1:
    #     return n
    # for i in range(2,n):
    recursive_hash[n] = fibonacci(n-1,recursive_hash) + fibonacci(n-2, recursive_hash)
    return recursive_hash[n]


def find_prod(i: int) ->(int, int, bool):
    si = math.sqrt(i)
    n = 1
    fib_list = [0,1]


    while fib_list[n] <= si:
        n += 1
        fib_list.append(fibonacci(n))
        # print(fib_list[n], fib_list[n]**2)
    return fib_list[n-1], fib_list[n], fibonacci(n)*fibonacci(n-1) == i


# print(fibonacci(9))
print(find_prod(714))
print(find_prod(4895))
