def count_bounces(h, b, o):
    num_bounces = 0
    seen = 0

    while h > o:
        num_bounces += 1
        seen += 1  # Ball is seen on the way down
        h = b * h   # Ball bounces back up

        if h > o:
            seen += 1  # Ball is seen on the way up

    return seen

# Example usage
h = 10  # Initial height
b = 0.6  # Bounce rate
o = 5  # Observer's height
result = count_bounces(h, b, o)
print("Number of times the observer sees the ball:", result)