while True:
    try:
        principal = float(input("Enter your principle amount: ৳ "))
        while principal <= 0:
            print("Principle can't be zero or less than zero(0).")
            principal = float(input("Enter your principal amount: ৳ "))

        interest = float(input("Enter yearly interest rate: "))
        while interest <= 0:
            print("Interest rate can't be zero or less than zero(0).")
            interest = float(input("Enter your interest rate(monthly): "))

        time = int(input("Enter your time(in years): "))
        while time <= 0:
            print("Time can't be zero or less than zero(0).")
            time = int(input("Enter your time(in months): "))
        break

    except ValueError:
        print("Principal/Interest rate/Time can only be number. ")


total = principal * pow((1 + interest/100),time)
print(f"Your final amount on {interest}% interest after {time} years will be: ৳ {total:.2f} ")