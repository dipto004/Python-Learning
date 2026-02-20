while True:
    try:
        weight = float(input("Enter weight: "))
        unit = input("The weight you enter is it in kg/lb(K/L): ")
        if unit.upper() == 'K':
            print(f"Your weight is: {weight * 2.205:.2f} lbs")
            break
        elif unit.upper() == 'L':
            print(f"Your weight is: {weight / 2.205:.2f} kgs")
            break
        else:
            print(f"You have entered '{unit}' which is not a valid input. Choose only K or L")
    except ValueError:
        print(f'Your input weight is not a number.')