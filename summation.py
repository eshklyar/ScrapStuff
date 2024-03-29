def summation(num):
    s = sum(n for n in range(1,num + 1))
    nums = [str(n) for n in range(1, num +1)]


    print(nums)

    nums1 = str([n for n in range(1, num + 1)])
    print((nums))

    string = " + ".join(nums)
    r = f"{s} ({string})"
    print(r)
    print(string)
    print(type(string))

    string1 = "+".join(nums1)
    print(string1)
    print(type(string1))

    print(string == string1)

summation(5)
