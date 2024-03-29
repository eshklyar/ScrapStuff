# def stringDivisor(s):
#     try:
#         if len(s) > 0:
#             n = len(s)
#             for i in range(1, n):
#                 if s[:i] * (n // i) == s:
#                     return s[:i]
#         else:
#             return "Empty String"
#         if len(s) == 1:
#             return s
#     except Exception as e:
#         print(f"An error occurred: {e}")
#     return s
#
# # my_string = "abcabcabcabc"
#
# keep_going = True
# while keep_going:
#      my_string = input("Enter a string: ")
#      print(stringDivisor(my_string))
#      if my_string == "quit":
#         keep_going = False

def stringDivisor(s):
    if len(s) > 1:
        for i in range(1, len(s)):
            if s[:i] * (len(s) // i) == s:
                return s[:i]
            else:
                return s
    elif len(s) == 1:
        return s
    else:
        return "empty string"

# my_string = "abcabcabcabc"

keep_going = True
while keep_going:
     my_string = input("Enter a string: ")
     print(stringDivisor(my_string))
     if my_string == "quit":
        keep_going = False
