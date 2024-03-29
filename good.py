def square_sum2(numbers):
    return sum(x ** 2 for x in numbers)

def count_sheeps2(arrayOfSheeps):
  return arrayOfSheeps.count(True)

def no_space(x):
    return "".join(x.split())

def no_space(x):
    return x.replace(' ' ,'')

def count_sheep(n):
    return ''.join(f"{i} sheep..." for i in range(1,n+1))

def remove_char(s):
    return s[: -2]

print(remove_char("world"))

b = 37
x = ['Underweight', 'Normal', 'Overweight', 'Obese'][(b > 30) + (b > 25) + (b > 18.5)]


def check(seq, elem):
    return elem in seq

def check1(seq, elem):
    return True if elem in seq else False