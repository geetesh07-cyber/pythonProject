#TODAY WEEE ARE GOING TO CRATE A PASSWORD GEMERATOR
#for loops
''''fruits = ["Apple","Peach","Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
    print(fruits)
print(fruits)'''
#CODING EXERCISE
'''
# student_heights = input("HOW MANY STUDENTS ARE THERE give height?").split()
# for n in range(0,len(student_heights)):
#     student_heights[n] = int(student_heights[n])
#     print(student_heights)
# for n in range(0,student_heights):
#     sumofheights += student_heights[n]
# actualsum = int(sumofheights)
# average = actualsum/len(student_heights)
# print(f"your average is {average}")'''
# for number in range(1,101):
#     if(number%15==0):
#         print("FIZZBUZZ")
#     elif(number%3==0):
#         print("FIZZ")
#     elif(number%5==0):
#         print("BUZZ")
#     else:
#         print(number)
#         '''student_heights = input("HOW MANY STUDENTS ARE THERE give height?").split()
# for n in range(0,len(student_heights)):
#     student_heights[n] = int(student_heights[n])
#     print(student_heights)
# for n in range(0,student_heights):
#     sumofheights += student_heights[n]
# actualsum = int(sumofheights)
# average = actualsum/len(student_heights)
# print(f"your average is {average}")'''
# for number in range(1,101):
#     if(number%15==0):
#         print("FIZZBUZZ")
#     elif(number%3==0):
#         print("FIZZ")
#     elif(number%5==0):
#         print("BUZZ")
#     else:
#         print(number)
#         '''student_heights = input("HOW MANY STUDENTS ARE THERE give height?").split()
# for n in range(0,len(student_heights)):
#     student_heights[n] = int(student_heights[n])
#     print(student_heights)
# for n in range(0,student_heights):
#     sumofheights += student_heights[n]
# actualsum = int(sumofheights)
# average = actualsum/len(student_heights)
# print(f"your average is {average}")'''
# for number in range(1,101):
#     if(number%15==0):
#         print("FIZZBUZZ")
#     elif(number%3==0):
#         print("FIZZ")
#     elif(number%5==0):
#         print("BUZZ")
#     else:
#         print(number)
#         '''
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level
# password = ""

# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)

# print(password)

#Hard Level
password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")