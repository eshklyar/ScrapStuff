def square_sum(numbers):
    res = 0
    for i in numbers:
        res += i*i
    return res

def square_sum1(numbers):
    res = 0
    sq = [x*x for x in numbers]
    for s in sq:
        res += s
    return res

def square_sum2(numbers):
    return sum(x ** 2 for x in numbers)

nums = [1,2,3]

print(square_sum(nums))
print(square_sum1(nums))