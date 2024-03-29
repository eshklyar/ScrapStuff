# need to find repeating substring in a string
# explain code line by line
from math import gcd


def stringDivisor(s):
    try:
        n = len(s)
        for i in range(1, n):
            if s[:i] * (n // i) == s:
                return s[:i]
    except Exception as e:
        print(f"An error occurred: {e}")
    return s

# my_string = "abcabcabcabc"
keep_going = True
while keep_going:
     my_string = input("Enter a string: ")
     print(stringDivisor(my_string))
     if my_string == "quit":
        keep_going = False

# print(stringDivisor(my_string))

# need to find greatest commmon denominator for two strings
# def gcdOfStrings(str1, str2):
#     if len(str1) < len(str2):
#         str1, str2 = str2, str1
#     if str1[:len(str2)] == str2:
#         return gcdOfStrings(str1[len(str2):], str2)
#     if str2 == "":
#         return str1
#     return ""
#
# # need to rewrite above method using while loop
# def gcdOfStrings2(str1, str2):
#     if len(str1) < len(str2):
#         str1, str2 = str2, str1
#     while str1[:len(str2)] == str2:
#         str1 = str1[len(str2):]
#     if str2 == "":
#         return str1
#     return ""

# need to find greatest common denominator for two strings using a for loop
# def gcdOfStrings3(str1, str2):
#     if len(str1) < len(str2):
#         str1, str2 = str2, str1
#     for i in range(len(str2)):
#         if str1[i] != str2[i]:
#             return ""
#     if str2 == "":
#         return str1
#     return ""
# in the above method with the strings initialized below, explain how do we get to "abc"?
# def gcdOfStrings4(str1, str2) -> str:
#     len1, len2 = len(str1), len(str2)
#     gcd_len = gcd(len1, len2)
#     pattern = str1[:gcd_len]
#
#     if str1 + str2 == str2 + str1:
#         return pattern
#     else:
#         return ""
#
# my_string1 = "ab"
# my_string2 = "a"
# my_result = gcdOfStrings4(my_string1, my_string2)
# print(f"my result is {my_result}")
# # print(gcdOfStrings4(my_string1, my_string2))