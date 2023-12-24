# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from functools import reduce
from operator import add

reduce(add, [1, 2, 3, 4, 5])

# reduce(add, [])

reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
def main():
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    print(sum(3,5))

def sum(x,y):
    return x+y

def sum_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

sum_numbers([1, 2, 3, 4, 5])

# Use a list
sum([1, 2, 3, 4, 5])


# Use a tuple
sum((1, 2, 3, 4, 5))


# Use a set
sum({1, 2, 3, 4, 5})


# Use a range
sum(range(1, 6))


# Use a dictionary
sum({1: "one", 2: "two", 3: "three"})

sum({1: "one", 2: "two", 3: "three"}.keys())