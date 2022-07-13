import random

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
              'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
              'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
              'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
              'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
              'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
              'Z']

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']

chars = int(input("enter no of charecters to be included in password : "))

nums = int(input("enter no of numbers to be included in password : "))

spe_chars = int(
    input("enter no of special charecters to be included in password : "))


# created a empty list to store the password.
password = []

# created a loop to add the charecters to the password list.
for i in range(0, chars):
    password += random.choice(CHARACTERS)

# created a loop to add the numbers to the password list.
for i in range(0, nums):
    password += random.choice(DIGITS)

# created a loop to add the special characters to the password list.
for i in range(0, spe_chars):
    password += random.choice(SYMBOLS)

# shuffle the password list.
random.shuffle(password)

# convert the password list to a string.
newpass = ""
for i in password:
    newpass += i

# print the password.
print(newpass)
