def strong(n):
    sum = 0
    while(n>=1):
        fact = 1
        temp = n%10
        while(temp>1):
            fact = fact * temp
            temp -= 1
        n = n//10
        sum = sum + fact
    return(sum)
n = int(input("Enter a number: "))
if strong(n) == n:
    print(f"{n} is a strong number")
else:
    print(f"{n} is not a strong number")

