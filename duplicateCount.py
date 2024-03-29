def duplicate_count(text):
    text = text.lower()
    print(text)
    # print(len(text.lower()))
    # print(len(set(text.lower())))
    ar = ([text.count(c) for c in text])
    print(ar)
    one = [n for n in ar if n==1]
    print(one)
    z = [(c, cc) for c in set(text) for cc in text ]
    print(z)
    counter = 0
    for s in set(text):
        if text.count(s) > 1:
            counter +=1
    print(counter)



def duplicate_count2(text):
    text = text.lower()
    counter = 0
    for s in set(text):
        if text.count(s) > 1:
            counter +=1
    return counter

def duplicate_count3(text):
    text = text.lower()
    return sum(1 for s in set(text) if text.count(s) > 1)

def duplicate_count4(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])


print(duplicate_count3("Indivisibilities"))