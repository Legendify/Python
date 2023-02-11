# Artin Moghadasi
# @Artin.Projets
import random

RPS= ["rock","paper","scissor"]
round=int(input("Enter number of rounds:"))

for i in range(round):

    UserChoice=input("Enter your choice(rock-paper-scissor):")
    AIChoice=random.choice(RPS)

    print('User Choice:' , UserChoice )
    print('AI Choice:' , AIChoice)

    AIPoint=0
    UserPoint=0

    #Draw
    if AIChoice=='rock' and UserChoice=='rock':
        print("Draw")
    elif AIChoice=='paper' and UserChoice=='paper':
        print('Draw')
    elif AIChoice=='scissor' and UserChoice=='scissor':
        print('Draw')
    #AI Wins
    if AIChoice=='scissor' and UserChoice=='paper':
        print('AI Wins')
        AIPoint+=1
    elif AIChoice=="rock" and UserChoice=='scissor':
        print('AI Wins')
        AIPoint+=1
    elif AIChoice=='paper' and UserChoice=='rock':
        print('AI Wins')
        AIPoint+=1
    #User Wins
    if UserChoice=='scissor' and AIChoice=='paper':
        print('User Wins')
        UserPoint+=1
    elif UserChoice=="rock" and AIChoice=='scissor':
        print('User Wins')
        UserPoint+=1
    elif UserChoice=='paper' and AIChoice=='rock':
        print('User Wins')
        UserPoint+=1

print('AI Point:' , AIPoint)
print('User Point:' , UserPoint)
print("Thanks!"+"\nBye")
