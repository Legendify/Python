import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()'

number=int(input("Number of Passwords You want to Generate:"))
length=int(input("Enter length of password:"))


for i in range (number):
    password=''
    for k in range(length):
        password += random.choice(chars)
    print(password)
    
