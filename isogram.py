def is_isogram(string):
    my_string = string.lower()
    res = True
    for index, char in enumerate(my_string):
        if char in my_string[index+1:]:
            res = False
    return res


# print(is_isogram ("Dermatoglyphics"))
print(is_isogram ("moOse"))