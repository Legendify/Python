from random import *
import os

your_pwd=input("Enter a password: ")

pwd= [
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    '0','1','2','3','4','5','6','7','8','9','10'
    ]
pw=""
while (pw!=your_pwd):
    pw=""
    for letter in range (len(your_pwd)):
        guess_pwd=pwd[randint(0)]
        pw=str(guess_pwd)+str(pw)
        print(pw)
        print("cracking password ... please wait")
        os.system("cls")
    
print("your password is:",pw)    

