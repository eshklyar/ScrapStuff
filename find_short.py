def find_short(s):
    return sorted([len(w) for w in s.split()])[0]
    l = ([len(w) for w in s.split()])
    l.sort()
    print(l[0])


str = "bitcoin take over the world maybe who knows perhaps"

print(find_short(str))

def sum_two_smallest_numbers1(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]

def sum_two_smallest_numbers2(numbers):
    numbers.sort()
    return sum(numbers[:2])

def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])


nums = [19, 5, 42, 2, 77]

print(sum_two_smallest_numbers(nums))