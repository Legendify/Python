num = int(input("Enter the Number:"))
a = 0 
b = 1
count = 1
sum = 0
print("Fibonacci Series: ")
for i in range(count, num):
    print(sum)
    count += 1
    a = b
    b = sum
    sum = a + b

