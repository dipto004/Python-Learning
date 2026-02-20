# name = input("Enter your name: ")
# length = len(name)
# print(f"The length of the name is: {length}")


# print(help(str))      #learn the str method and all


# name = 'yukinoshita yukino'
# name2 = 'AkAnE12'
# name3 = 'mikasa'
# num = '345'
# print(name.find('i'))   #if it finds the character, then return the index number. if not, then return -1 ; also it only count the first occurrence
# print(name.rfind('i'))  #same as find(), just check the character reverse
# print(name.capitalize())    #only capitalized the first character
# print(name.upper())     #capitalized all the characters
# print(name2.lower())    #lower all the characters
# print(name2.isdigit())   #check if string contains only digit and return True / False
# print(num.isdigit())
# print(name.isalpha())       #check if the string contains only alphabetic character ; even the space is not consider alphabetic so it will return False
# print(name2.isalpha())
# print(name3.isalpha())
# print(name.count('i'))      #count the number of times a character appear in the string
# print(name3.replace('a', 'A'))      #replace a character with another character


# username can't be more than 12 character, can't contain any spaces or digit
# username = input("Enter your username: ")
# if len(username) <= 12 and username.isalpha():
#     print("The username is valid")
# else:
#     print("The username is invalid")





# string indexing
# num = '123-45-678-90'
# print(num[0])
# print(num[3])
# print(num[1:4])     #don't count the end index ; mainly [x,y] -> (x,y-1)
# print(num[:3])
# print(num[5:])
# print(num[::2])
# print(num[0:8:2])
# print(num[-1])        #the last digit is count as -1
# print(num[-3:-1])
# print(num[-6: -3])      #if [-x:-y] and y>x, then it don't show anything as slicing generally go from left to right
# print(num[-6: -8])      #return empty string
# print(num[-6:-9:-1])        #this will work
# print(num[::-1])        #reverse the string