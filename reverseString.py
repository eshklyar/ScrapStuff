def reverse_words(text):
    y = [w[::-1] for w in text.split()]
    print(y)
    return text [::-1]

# print(reverse_words('apple'))
print(reverse_words('The quick brown fox jumps over the lazy dog.'))