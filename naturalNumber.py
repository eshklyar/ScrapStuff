def solution(number):
    sum = 0
    if number > 0:
        for i in range(1, number+1):
            # print(i, end='')
            if i % 3 == 0 or i % 5 == 0:
                sum += i
            print(sum)
    else:
        sum = 0
    return sum


print(solution(14))
# print(solution(9))