num = int(input("Enter 3 digit number:"))
num1 = 0
temp = 0
while(num > 0):
    temp = num%10
    num1 = num1*10 + temp
    num = num//10
    
print(f"reverse: {num1}")