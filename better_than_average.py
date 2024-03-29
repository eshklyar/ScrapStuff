def better_than_average(class_points, your_points):
    return sum(class_points)/len(class_points) < your_points


print(better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75))