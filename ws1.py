v = [1, 2, 3]
print(v)
if not v:
    print("0")
else:
    print("1")

nums = [2, 5, 7, 2, 56, 4, 87]
nums.sort()
print(nums[-2:])


def stringDivisor(s):
    if len(s) > 1:
        for i in range(1, len(s)):
            if s[:i] * (len(s) // i) == s:
                return s[:i]
        return s
    elif len(s) == 1:
        return s
    else:
        return "empty string"
#
# def stringDivisor(s):
#     for i in range(1, len(s)):
#         print(s[:i])
#         print(len(s) // i)
#         # if s[:i] * (len(s) // i) == s:
#         #     return s[:i]
#         # else:
#         #     return s


my_string = "abcabcabcabc"

print(stringDivisor(my_string))

# def stringDivisor(s):
#     for i in range(1, len(s)):
#         print(s[:i])
#         print(len(s) // i)
#         if s[:i] * (len(s) // i) == s:
#             return s[:i]
#         else:
#             return s

m_list = ["one", "two", "three"]
print(m_list[-3])