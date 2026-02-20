while True:
    try:
        temp = float(input("Enter the temperature: "))
        in_unit = input("The entered temperature is it in Celsius, Fahrenheit, Kelvin (C/F/K): ").upper()
        out_unit = input("The convert temperature will be  in Celsius, Fahrenheit, Kelvin (C/F/K): ").upper()

        if in_unit == 'C':
            if out_unit == 'F':
                print(f"The temperature is: {(9 / 5 * temp) + 32:.1f} °F")  #alt + 0176 for the °
                break
            elif out_unit == 'K':
                print(f"The temperature is: {temp + 273.15:.1f} K")
                break
            elif out_unit == 'C':
                print(f"The temperature is: {temp:.1f} °C")
                break
            else:
                print(f'{out_unit} is an invalid unit')
        elif in_unit == 'F':
            if out_unit == 'C':
                print(f"The temperature is: {5 / 9 * (temp - 32):.1f} °C")  #alt + 0176 for the °
                break
            elif out_unit == 'K':
                print(f"The temperature is: {(5 / 9 * (temp - 32)) + 273.15:.1f} K")
                break
            elif out_unit == 'F':
                print(f"The temperature is: {temp:.1f} °F")
                break
            else:
                print(f'{out_unit} is an invalid unit')

        elif in_unit == 'K':
            if out_unit == 'C':
                print(f"The temperature is: {temp - 273.15:.1f} °C")  #alt + 0176 for the °
                break
            elif out_unit == 'F':
                print(f"The temperature is: {((temp - 273.15) * 9 / 5) + 32:.1f} °F")
                break
            elif out_unit == 'K':
                print(f"The temperature is: {temp:.1f} K")
                break
            else:
                print(f'{out_unit} is an invalid unit')
        else:
            print(f'{in_unit} is an invalid unit')
    except ValueError:
        print('You have entered invalid temperature. Try again.')