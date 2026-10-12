import random

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols=['!','#','$','%','&','(',')','+','*']
numbers=['0','1','2','3','4','5','6','7','8','9']

print("Welcome to Password Generator!")
letter_in=int(input("How many letters would you like in your password?"))
symbol_in=int(input("How many symbols would you like in your password?"))
number_in=int(input("How many numbers would you like in your password?"))

# password=""
#
# for letter in range(0,letter_in):
#     password += random.choice(letters)
# for symbol in range(0,symbol_in):
#     password += random.choice(symbols)
# for number in range(0,number_in):
#     password += random.choice(numbers)
#
# print(password)
password=[]
for letter in range(0,letter_in):
    password += random.choice(letters)
for symbol in range(0,symbol_in):
    password += random.choice(symbols)
for number in range(0,number_in):
    password += random.choice(numbers)

print(password)

random.shuffle(password)
print(password)

final_password=""
for final in password:
    final_password += final
print(final_password)