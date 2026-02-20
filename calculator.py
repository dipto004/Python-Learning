print("The operation whould be like this: Number1 operator Number2 = result")
num1 = float(input("Enter Number 1: "))
num2 = float(input("Enter Number 2: "))
operator = input("What operation would you like to do (+, -, *, /, %, **: ")
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = round(num1 / num2, 4)
elif operator == '%':
    result = num1 % num2
elif operator == '**':
    result = num1 ** num2
else:
    result = 'no'
if result == 'no':
    print(f'You have enter "{operator}" which is an invalid operator.')
else:
    print(f"The result of {num1} {operator} {num2} = {result}")