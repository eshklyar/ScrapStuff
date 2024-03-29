def array_diff(a, b):
    return [x for x in a if x not in b]

arrA = [1,2,2]
arrB = [1]

print(array_diff(arrA,arrB))

def find_it(seq):
    # y = max([seq.count(x) for x in seq])
    # z = [x for x in seq if (seq.count(x)%2 != 0)]
    return set([(x) for x in seq if (seq.count(x)%2 != 0)]).pop()

li =[1,2,2,3,3,3,4,3,3,3,2,2,1]
print(f"find it {find_it(li)}")




l = [x for x in range(10) if x%2 == 0]
print(l)



tup = ('a', 'b', 'c', 'd', 'e')

# creating an iterator from the tuple
tup_iter = iter(tup)

print("Inside loop:")
# iterating on each item of the iterator object
# for index, item in enumerate(tup_iter):
for index, item in enumerate(tup):

    print(item)

    # break outside loop after iterating on 3 elements
    if index == 2:
        break

# we can print the remaining items to be iterated using next()
# thus, the state was saved
print("Outside loop:")
print(next(tup_iter))
print(next(tup_iter))

li1 = ["a", "b", "b"]
print(f"printing li1 {[[x,li1.count(x)] for x in set(li1)]}")

def longest_consec(strarr, k):
    count = 0
    for i in strarr:
        if count < 3:
            print(f"loop {i}")
            count =+ 1
        count = 0
        print("out")


con_list = ["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"]
longest_consec(con_list, 2)

def print_numbers_in_chunks(numbers):
    for i in range(0, len(numbers), 3):
        print(' '.join(str(num) for num in numbers[i:i+3]))

# Test the function with an array of numbers from 0 to 10
numbers = list(range(11))
print_numbers_in_chunks(numbers)


def count_bounces(h, b, o):
    num_bounces = 0
    seen = 0

    while h > o:
        num_bounces += 1
        seen += 1  # Ball is seen on the way down
        h = b * h   # Ball bounces back up

        if h > o:
            seen += 1  # Ball is seen on the way up

    return seen

# Example usage
h = 10  # Initial height
b = 0.6  # Bounce rate
o = 5  # Observer's height
result = count_bounces(h, b, o)
print("Number of times the observer sees the ball:", result)

