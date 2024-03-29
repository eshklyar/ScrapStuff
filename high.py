import string
def high(x):
    l = []
    # question - is there a better way to make dict from string/list???
    d = {k: v+1 for v, k in enumerate(string.ascii_lowercase)}
    for word in x.split():
        word_value = sum(d[char] for char in word)
        l.append(word_value)
    return x.split()[l.index(max(l))]

# explain this code ???
def high1(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))

mystr = 'aa b'
print(high(mystr))
