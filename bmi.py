def bmi(weight, height):
    # b = weight / height ** 2
    b = 37
    x = ['Underweight', 'Normal', 'Overweight', 'Obese'][(b > 30) + (b > 25) + (b > 18.5)]
    print(x)
    bmiVar = weight / (height ** 2)
    if bmiVar <= 18.5:
        return "Underweight"

    if bmiVar <= 25.0:
        return "Normal"

    if bmiVar <= 30.0:
        return "Overweight"

    if bmiVar > 30:
        return "Obese"


print(bmi(50, 1.50))
print(bmi(50, 1.80))
