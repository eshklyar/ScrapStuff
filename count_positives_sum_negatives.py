def count_positives_sum_negatives(arr):
    p = sum(x >0 for x in arr)
    n = sum(x for x in arr if x < 0)
    return [p,n] if len(arr) > 0 else []


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
b = None
c = []

print(count_positives_sum_negatives(a))
print(count_positives_sum_negatives(c))

