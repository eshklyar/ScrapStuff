"""Top-down approach (Memoization)"""
def fibonacci_top_down(n, dict_to_recall_values={}):
    if n in dict_to_recall_values:
        return dict_to_recall_values[n]
    if n <= 1:
        return n
    dict_to_recall_values[n] = fibonacci_top_down(n - 1, dict_to_recall_values) + fibonacci_top_down(n - 2, dict_to_recall_values)
    print(dict_to_recall_values)

    return dict_to_recall_values[n]
print(fibonacci_top_down(5))
print("the end of Memoization \n")


"""Bottom-up approach (Tabulation)"""
def fibonacci_bottom_up(n):
    if n <= 1:
        return n
    dict_to_recall_values = [0] * (n+1)  #init dict to the size of n with zero values
    dict_to_recall_values[1] = 1
    for i in range(2, n+1):
        dict_to_recall_values[i] = dict_to_recall_values[i-1] + dict_to_recall_values[i-2]
    return dict_to_recall_values[n]

print(fibonacci_bottom_up(2))  # Output: 5


print(fibonacci_top_down(5))
print("the end of Tabulation \n")


