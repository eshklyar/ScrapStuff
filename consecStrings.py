def longest_consec(strarr, k):
    tempStr = ""
    li = []
    for i in range(len(strarr)-1):
        for j in range(k):
            tempStr += strarr[i+j]
        li.append(tempStr)
        tempStr = ""
    print(li)


    # w = ["".join([strarr[i] for i in range(k)]) for i in range(len(strarr)-1)]
    # print(w)
    # w.append()
    # newstrarr = [strarr[i]+strarr[i+1] for i in range(len(strarr)-1)]
    # newstrarr = [strarr[i]+strarr[i+1] for i in range(len(strarr)-1)]

    # j = sum(strarr[i] for i in range(k) for w in strarr)

    # print(j)

    # print(newstrarr)
    # num = max([len(x) for x in newstrarr])
    # print(num)
    # for a in newstrarr:
    #     if len(a) == num:
    #         return a
            # print(a)
    # for i in range(0,len(strarr),2):
    #     print(strarr[i]+strarr[i+1])



strarrtest = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"]

anotherstrarrtest = ["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"]

numberstrarrtest = [1,2,3,4,5,6,7,8]

# print(longest_consec(numberstrarrtest,2))
print(longest_consec(strarrtest,2))

def consecutive_substrings(strarr, k):
    result = []
    for i in range(len(strarr) - k + 1):
        substring = "".join(strarr[i:i+k])
        result.append(substring)
    return result

# Example usage
strarr = ["a", "b", "c", "d", "e"]
k = 3
print(consecutive_substrings(strarr, k))