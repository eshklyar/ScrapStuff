def duplicate_encode1(word):
    w = ""
    for char in word:
        if word.lower().count(char.lower()) > 1:
            w += ")"
        else:
            w += "("
    return w

def duplicate_encode(word):
    return "".join(["(" if word.lower().count(char.lower()) == 1 else ")" for char in word])

# Test the function
print(duplicate_encode("Success"))  # Output: ")())())"


# print(duplicate_encode("Success"))
