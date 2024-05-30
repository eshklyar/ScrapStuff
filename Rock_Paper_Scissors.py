import itertools

def rps2(p1, p2):
    rps_list = ["rock", "paper", "scissors"]
    p1_index = rps_list.index(p1)
    p2_index = rps_list.index(p2)
    if (p2_index - p1_index) % 3 == 1:
        return "Player 2 won!"
    elif (p2_index - p1_index) % 3 == 2:
        return "Player 1 won!"
    else:
        return "Draw!"

rps_list = ["rock", "paper", "scissors"]
def rps(p1, p2):
    rps_list = ["rock", "paper", "scissors"]
    res_list = ["Draw!","Player 1 won!", "Player 2 won!"]
    res = (rps_list.index(p1) - rps_list.index(p2)) % 3
    return res_list[res]

def rps(p1, p2):
    hand = {'rock':0, 'paper':1, 'scissors':2}
    results = ['Draw!', 'Player 1 won!', 'Player 2 won!']
    return results[hand[p1] - hand[p2]]

# Generate all permutations of two choices
permutations = list(itertools.permutations(rps_list, 2))

# Calculate the game result for each permutation
for p1, p2 in permutations:
    result = rps(p1, p2)
    print(f"Choices: {p1} (index {rps_list.index(p1)}) vs {p2} (index {rps_list.index(p2)}), Result: {result}")

rps_list = ["rock", "paper", "scissors"]
message = "Player 1 won!"

# for i in range(1,4):
#     print(i)

def sub(a:int, b:int) -> int:
    print(a,b)
    return (b-a)%3

# print(sub(1,2))

for i in range(-2,3,1):
    print(i, i%3)


# def sub2() -> int:
#     a = int(input("Enter the first number: "))
#     b = int(input("Enter the second number: "))
#     print(a, b)
#     return (b - a) % 3


def sub2() -> int:
    # a = b = 0
    while True:
        a = input("Enter the first number (or 'z' to exit): ")
        if a.lower() == 'z':
            break
        b = input("Enter the second number: ")
        a, b = int(a), int(b)
        print(a, b)
        print((b - a) % 3)
print(sub2())

a = 0
if not a:
    print(0)
else:
    print(1)