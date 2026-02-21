# while loop
# name = input("Enter your name: ")
# while not name:
#     print("You didn't enter your name.")
#     name = input("Enter your name: ")
# print(f"Welcome to our town, {name}")


# is_student = input("Are you a student(Y/N): ").upper()
# while is_student != 'N' and is_student != 'Y':
#     print("You entered a wrong input.")
#     is_student = input("Are you a student(Y/N): ").upper()
# print("You have successfully confirmed your identity.")


# num = int(input("Enter a number between 1 to 10: "))
# while not 1<=num<=10:
#     print(f"{num} is not valid. Try again.")
#     num = int(input("Enter a number between 1 to 10: "))
# print(f"You have entered {num}")





# for loop
# for i in range(1,10):       # range(a,b,c) -> initiate with a, end at b-1, step c
#     print(i)


# for i in range(2,18,4):
#     print(i)


# for i in reversed(range(1,5)):      # It just reverse the printing
#     print(i)


# name = 'yukinoshita'
# for a in name:
#     print(a, end=" ")


for i in range(1,21):
    if i == 13:
        continue
    print(i, end=" ")