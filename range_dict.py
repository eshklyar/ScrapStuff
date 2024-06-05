def people_with_age_drink(age):
    drinks = {range(0, 14): "toddy", range(14, 18) : "coke", range(18, 21) : "beer", range(21, 100) : "whisky"}
    for key in drinks.keys():
        if age in key:
            return f"{age} --> drink {drinks[key]}"

print(people_with_age_drink(18))