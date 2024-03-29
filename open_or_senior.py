def open_or_senior(data):
    li= []
    for x in data:
        if x[0] >= 55 and x[1] >7:
            li.append("Senior")
        else:
            li.append("Open")
    return li

def open_or_senior2(data):
    return ["Senior" if age >= 55 and handicap > 7 else "Open" for age, handicap in data]



input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]

print(open_or_senior(input))