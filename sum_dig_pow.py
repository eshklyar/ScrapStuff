def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    ans = []
    for n in range(a, b+1):
        s_list = []
        # l = len(str(n))
        word = str(n)
        for i,c in enumerate(word):
            print(f"i is {i+1}, c is {c}")
            s_list.append(int(c)**(i+1))
            print(f" s_list is {s_list}")
        print(f" n is {n} and s_list is {s_list}")
        j_list = "".join(str(s_list))
        print(f" j_list is {j_list}")
        if str(n) == ".join(s_list)":

            ans.append(n)

    return [ans]

print(sum_dig_pow(1, 10)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

def sums(a: int, b:int) -> list[int]:
    ans = []
    for i in range(a, b+1):
        x = sum(int(c)**(i+1) for i, c in enumerate(str(i)))
        if i == x:
            ans.append(i)
    return ans
print(sums(1,100))