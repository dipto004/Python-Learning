# Start New
print("Hello, my name is Dipto Chakraborty")





# Variable - string, integer, float, boolean
# string
# first_name = 'Dipto'
# last_name = 'Chakraborty'
# print(first_name + last_name)
# print(f"Hello, This is using f-string. Like this {first_name} {last_name}")


# interger /float
# age = 25
# cgpa = 3.95
# print(f"You are {age} years old.")
# print(f"You have {cgpa} CGPA")


# boolean
# In boolean, every number including negative except 0 is considered True.
# is_student = True
# is_homesick = 0.1
# print(f"Are you a student: {is_student}")
# print(f"Are you homesick: {is_homesick}")
# if is_homesick:
#     print("Go to Home")
# else:
#     print("Continue with your work")





# Typecasting
# print(type(first_name))
# print(type(age))
# print(type(cgpa))
# print(type(is_student))


# t_cgpa = int(cgpa)
# t_name = int(first_name)  #str to int not possible
# t_age = float(age)
# t_isStudent = str(is_student)
# t_isStudent2 = int(is_student)
# t_isStudent3 = float(is_student)
# t_name2 = bool(first_name)
# name3 = " "
# name4 = ""
# t_name3 = bool(name3)   #This will return True
# t_name4 = bool(name4)   #This will return False


# print(t_cgpa)
# print(t_age)
# print(t_isStudent)
# print(t_isStudent2)
# print(t_isStudent3)
# print(t_name2)
# print(t_name3)
# print(t_name4)





# Enter input
#Always return the input as a str
# name = input("What is your name: ")
# quantity = int(input("How many item do you need: "))
# print(f"Hello, {name}. Welcome to our shop.")
# print(f"You have chosen {quantity} items. But we will give you {quantity+3} as we have an offer")


# length = float(input("What is the length of the rectangle: "))
# width = float(input("What is the width of the rectangle: "))
# area = length*width
# print(f"The area of the rectangle is : {area} unit²")   #For the superscript squart, alt+0178





# Math Operation
# age += 1
# print(age)
# friend = 6
# friend -= 2
# print(friend)
# age **= 2
# print(age)
# friend /= 2
# print(friend)
# cgpa *= 1.5
# print(cgpa)
# remainder = 50 % 24
# print(remainder)


# x = 3.3
# y = 3.8
# z = -4
# print(round(x))
# print(round(y))
# print(abs(z))
# print(pow(3,4))
# print(max(x,y,z))
# print(min(x,y,z))


# import math
# print(math.pi)
# print(math.e)
# print(math.floor(x))
# print(math.floor(y))
# print(math.ceil(x))
# print(math.ceil(y))
# print(math.sqrt(9))


# radius = float(input("What is the radius of the circle: "))
# print(f"The circumference of the circle is: {2*math.pi*radius :.4} unit")   #This will show first 4 number.
# print(f"The circumference of the circle is: {2*math.pi*radius:.4f} unit")   #This will show first 4 number after decimal
# print(f"The circumference of the circle is: {round(2*math.pi*radius, 5)} unit")   #This will show first 5 number after decimal
# print(f"The area of the circle is: {math.pi*pow(radius,2):.2f} unit²")


# width = float(input("Enter the width: "))
# length = float(input("Enter the length: "))
# print(f"The diagonal of the rectangular is: {math.sqrt(pow(length,2)+pow(width,2)):.3f} unit")





# if-else statement
# age = int(input("Enter your age: "))
# if 18 <= age < 100:
#     print("You are eligible for vote.")
# elif age >=100:
#     print(f"You may have enter an incorrect age as you enter {age}. But if you have enter the correct one, You are eligible for vote.")
# elif age <= 0:
#     print("You have enter an incorrect age.")
# else:
#     print(f"You are not eligible for vote. Try again in {18-age} year/s")


# f_response = input("Would you like to go to Bangladesh(Y/N): ").upper()
# if f_response == "Y":
#     print("Hurrah !!! Let's go.")
# elif f_response == "N" :
#     print("Ohh !!! I would like to go with you.")
# else:
#     print("You have enter a wrong answer")


# name = input("Enter your name: ")
# if name:
#     print(f"Welcome to our place, Mr./Ms. {name}.")
# else:
#     print("You have not enter your name.")