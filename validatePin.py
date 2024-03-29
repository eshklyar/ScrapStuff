# def validate_pin1(pin):
#     nums = [str(x) for x in range(10)]
#     d = True
#     for c in pin:
#         if c in nums:
#             print(c)
#         else:d = False
#     return d and (len(pin) == 4 or len(pin)==6)


def validate_pin2(pin):
    nums = [str(x) for x in range(10)]
    char = [c for c in pin if c in nums]
    string = "".join(char)
    return (string == pin) and (len(pin) == 4 or len(pin) == 6)


def validate_pin3(pin):
    return len(pin) in (4, 6) and pin.isdigit()

# print(validate_pin("-12345"))
# print(validate_pin("12345"))
print(validate_pin2("2345"))