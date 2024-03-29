def high_and_low(numbers: str) -> str:
    # li = [int(x) for x in numbers.split()]
    # highestN = sorted(li).pop()
    # lowestN = sorted(li, reverse=True).pop()
    # highest = str(sorted(li).pop())
    # lowest = str(sorted(li, reverse=True).pop())

    return f"{sorted([int(x) for x in numbers.split()]).pop()} {sorted([int(x) for x in numbers.split()], reverse=True).pop()}"
    # return f"{sorted(li).pop()} {sorted(li, reverse=True).pop()}"
    # return f"{highestN} {lowestN}"
    # return " ".join([highest, lowest])


print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
