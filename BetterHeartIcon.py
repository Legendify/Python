from turtle import *
import time

bg = input("Enter Background Color: ")
heart = input("Enter Heart Color: ")

bgcolor(bg)
color(heart)
begin_fill()
left(50)
forward(133)
circle(50,200)
right(140)
circle(50,200)
forward(133)
time.sleep(5)
end_fill()
time.sleep(5)

#github.com/Legendify/Python