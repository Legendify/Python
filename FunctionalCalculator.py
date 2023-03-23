num1= int(input("FIRST NMUBER:"))
num2= int(input("SECOND NMUBER:"))
operation = input("OPERATION:[1.* 2./ 3.- 4.+]")
if operation == '1':
    print(num1*num2)
elif operation == '2':
    print(num1/num2)
elif operation == '3':
    print(num1-num2)
elif operation == '4':
    print(num1+num2)

